# SecItemExport(_:_:_:_:_:)

**Framework**: Security  
**Kind**: func

Exports one or more certificates, keys, or identities.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func SecItemExport(_ secItemOrArray: CFTypeRef, _ outputFormat: SecExternalFormat, _ flags: SecItemImportExportFlags, _ keyParams: UnsafePointer<SecItemImportExportKeyParameters>?, _ exportedData: UnsafeMutablePointer<CFData?>) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

This function works only with keys, certificates, and identities. An identity is the combination of a certificate and its associated private key. Although public keys are commonly stored in certificates, they can be stored separately in the keychain as well; for example, when you call the [`SecKeyCreatePair`](seckeycreatepair.md) function to create a key pair, both the public and private keys are stored in the keychain. Use the [`SecKeychainSearchCopyNext`](seckeychainsearchcopynext.md) function to find a key or certificate. Use the [`SecIdentitySearchCopyNext`](secidentitysearchcopynext.md) function in the Certificate, Key, and Trust API to find an identity.

## Parameters

- `secItemOrArray`: The keychain item or items to export. You can export only the following types of keychain items:  ,  , and  . If you are exporting exactly one item, you can specify a   object. Otherwise this parameter is a   object containing a number of items of type  .
- `outputFormat`: The format of the desired external representation for the item. Set this parameter to   to use the default for that item type. Possible values for this parameter and default values are enumerated in  .
- `flags`: A flag field indicating whether the exported item should have PEM armor. PEM armor refers to a way of expressing binary data as an ASCII string so that it can be transferred over text-only channels such as email. Set this flag to   if you want PEM armoring.
- `keyParams`: A pointer to a structure containing a set of input parameters for the function. If no key items are being exported, these parameters are optional and you can set the   parameter to  . For more information, see  .
- `exportedData`: On return, the variable referenced by this argument is overwritten with a   object containing the external representation of the keychain item or items. You are responsible for releasing this object by calling  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secitemexport(_:_:_:_:_:))*