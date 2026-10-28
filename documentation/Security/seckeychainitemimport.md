# SecKeychainItemImport

**Framework**: Security  
**Kind**: func  
**Role**: Function

Imports one or more certificates, keys, or identities and adds them to a keychain.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecItemImport(_:_:_:_:_:_:_:_:)`](./secitemimport%28_,_,_,_,_,_,_,_%29.md) instead.

## Declaration

```c
OSStatus SecKeychainItemImport(CFDataRef importedData, CFStringRef fileNameOrExtension, SecExternalFormat *inputFormat, SecExternalItemType *itemType, SecItemImportExportFlags flags, const SecKeyImportExportParameters *keyParams, SecKeychainRef importKeychain, CFArrayRef*outItems);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

When you pass this function a `CFDataRef` object containing the external representation of one or more keys, certificates, or identities, [`SecKeychainItemImport`](./seckeychainitemimport.md) attempts to determine the format and contents of the data. To ensure that this process is successful, you should specify values for one or more of the parameters `fileNameOrExtension`, `inputFormat`, and `itemType`. To have the function add the imported items to a keychain, specify a non-`NULL` value for the `importKeychain` parameter. To have the function return `SecKeychainItemRef` objects for the imported items, specify a non-`NULL` value for the `outItems` parameter.

Because the [`SecKeychainItemImport`](./seckeychainitemimport.md) function determines whether the item is PEM armored by inspecting the data, the `flags` parameter is not used in calling this function.

After the function returns, you can determine the nature of the keychain items from the values returned in the `inputFormat` and `itemType` parameters. Depending on the nature of each item, once it is imported to a keychain you can safely cast the `SecKeychainItemRef` object to a `SecKeyRef`, `SecCertificateRef`, or `SecIdentityRef` object.

Note that when you import data in PKCS12 format, typically one `SecIdentityRef` object is returned in the `outItems` parameter. The data might also include one or more `SecCertificateRef` objects. The output data will not include any `SecKeyRef` objects unless the incoming data includes a key with no matching certificate.

When the output item type is `kSecItemTypeAggregate`, you can use the [`CFGetTypeID(_:)`](../CoreFoundation/cfgettypeid%28_%29.md) function to determine the Core Foundation type of each item and the functions in `Getting Information About Keychain Services and Types` to determine the keychain item type of each item. For example, the following code determines whether the item is a certificate:

```objc
CFTypeID theID = CFGetTypeID(theItem);
if (SecCertificateGetTypeID() == theID)
```

You can pass in `NULL` for both `outItems` and `importKeychain` to determine what is inside a given external data representation. When you do, the function returns the input format and the item type without modifying the data in any way.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecItemImport(_:_:_:_:_:_:_:_:)`](./secitemimport%28_,_,_,_,_,_,_,_%29.md) instead.

## Parameters

- `importedData`: The external representation of the items to import.
- `fileNameOrExtension`: The name or extension of the file from which the external representation was obtained. Pass `NULL` if you don’t know the name or extension.
- `inputFormat`: On entry, points to the format of the external representation. Pass `kSecFormatUnknown` if you do not know the exact format. On return, points to the format that the function has determined the external representation to be in. Pass `NULL` if you don’t know the format and don’t want the format returned to you. For a list of formats, see [`SecExternalFormat`](./secexternalformat.md).
- `itemType`: On entry, points to the item type of the item or items contained in the external representation. Pass [`SecExternalItemType.itemTypeUnknown`](./secexternalitemtype/itemtypeunknown.md) if you do not know the item type. On return, points to the item type that the function has determined the external representation to contain. Pass `NULL` if you don’t know the item type and don’t want the type returned to you.
- `flags`: Unused; pass in `0`.
- `keyParams`: A pointer to a structure containing a set of input parameters for the function. If no key items are being imported, these parameters are optional and you can set the `keyParams` parameter to `NULL`. If you pass `NULL` for the `importKeychain` parameter, the `kSecKeyImportOnlyOne` bit in the `flags` field of the [`SecKeyImportExportParameters`](./seckeyimportexportparameters.md) structure is ignored. Otherwise, if the `kSecKeyImportOnlyOne` bit is set and there is more than one private key in the incoming external representation, no items are imported to the specified keychain and the error `errSecMultiplePrivKeys` is returned. The possible values for the `flags` field are described in [`SecKeyImportExportFlags`](./seckeyimportexportflags.md).
- `importKeychain`: A keychain object indicating the keychain to which the key or certificate should be imported. If you pass `NULL`, the item is not imported. Use the [`SecKeychainCopyDefault(_:)`](./seckeychaincopydefault%28_%29.md) function to get a reference to the default keychain.
- `outItems`: On return, points to an array of `SecKeychainItemRef` objects for the imported items. You must provide a valid pointer to a `CFArrayRef` object to receive this information. If you pass `NULL` for this parameter, the function does not return the imported items. You must call the `CFRelease` function to release this object when you are finished using it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemimport)*