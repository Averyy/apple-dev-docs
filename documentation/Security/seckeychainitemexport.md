# SecKeychainItemExport

**Framework**: Security  
**Kind**: func  
**Role**: Function

Exports one or more certificates, keys, or identities.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: Use [`SecItemExport(_:_:_:_:_:)`](./secitemexport%28_,_,_,_,_%29.md) instead.

## Declaration

```c
OSStatus SecKeychainItemExport(CFTypeRef keychainItemOrArray, SecExternalFormat outputFormat, SecItemImportExportFlags flags, const SecKeyImportExportParameters *keyParams, CFDataRef*exportedData);
```

## Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

## Discussion

This function works only with keys, certificates, and identities. An identity is the combination of a certificate and its associated private key. Although public keys are commonly stored in certificates, they can be stored separately in the keychain as well; for example, when you call the [`SecKeyCreatePair`](./seckeycreatepair.md) function to create a key pair, both the public and private keys are stored in the keychain. Use the [`SecKeychainSearchCopyNext`](./seckeychainsearchcopynext.md) function to find a key or certificate. Use the [`SecIdentitySearchCopyNext`](./secidentitysearchcopynext.md) function in the Certificate, Key, and Trust API to find an identity.

### Special Considerations

This function is deprecated in macOS 10.7 and later; use [`SecItemExport(_:_:_:_:_:)`](./secitemexport%28_,_,_,_,_%29.md) instead.

## Parameters

- `keychainItemOrArray`: The keychain item or items to export. You can export only the following types of keychain items: `SecCertificateRef`, `SecKeyRef`, and `SecIdentityRef`. If you are exporting exactly one item, you can specify a `SecKeychainItemRef` object. Otherwise this parameter is a `CFArrayRef` object containing a number of items of type `SecKeychainItemRef`.
- `outputFormat`: The format of the desired external representation for the item. Set this parameter to `kSecFormatUnknown` to use the default for that item type. Possible values for this parameter and default values are enumerated in [`SecExternalFormat`](./secexternalformat.md).
- `flags`: A flag indicating whether the exported item should have PEM armor. PEM armor refers to a way of expressing binary data as an ASCII string so that it can be transferred over text-only channels such as email. Set this flag to `kSecItemPemArmour` if you want PEM armoring.
- `keyParams`: A pointer to a structure containing a set of input parameters for the function. If no key items are being exported, these parameters are optional and you can set the `keyParams` parameter to `NULL`.
- `exportedData`: On return, points to the external representation of the keychain item or items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemexport)*