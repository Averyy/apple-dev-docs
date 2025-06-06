# SecCertificateAddToKeychain(_:_:)

**Framework**: Security  
**Kind**: func

Adds a certificate to a keychain.

**Availability**:
- macOS 10.3+

## Declaration

```swift
func SecCertificateAddToKeychain(_ certificate: SecCertificate, _ keychain: SecKeychain?) -> OSStatus
```

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  To add a certificate to the login keychain, use [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) instead.

 To add a certificate to the login keychain, use [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) instead.

This function requires a certificate object, which can, for example, be created with the [`SecCertificateCreateFromData`](seccertificatecreatefromdata.md) function or obtained over a network (see [`Secure Transport`](secure-transport.md)). If the certificate has already been added to the specified keychain, the function returns [`errSecDuplicateItem`](errsecduplicateitem.md) and does not add another copy to the keychain. The function looks at the certificate data, not at the certificate object, to determine whether the certificate is a duplicate. It considers two certificates to be duplicates if they have the same primary key attributes.

##### Special Considerations

If the keychain is locked, the system asks the user for a password or other token to unlock it. This function can therefore block while waiting for user input.

## Parameters

- `certificate`: The certificate object for the certificate to add to the keychain.
- `keychain`: The keychain object for the keychain to which you want to add the certificate. Pass   to add the certificate to the default keychain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seccertificateaddtokeychain(_:_:))*