# SecIdentityCreateWithCertificate(_:_:_:)

**Framework**: Security  
**Kind**: func

Creates a new identity for a certificate and its associated private key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func SecIdentityCreateWithCertificate(_ keychainOrArray: CFTypeRef?, _ certificateRef: SecCertificate, _ identityRef: UnsafeMutablePointer<SecIdentity?>) -> OSStatus
```

## Mentions

- [Creating an Identity](creating-an-identity.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

If the associated private key is not found in one of the specified keychains, this function fails with an appropriate error code (usually [`errSecItemNotFound`](errsecitemnotfound.md)), and does not return anything in the `identityRef` parameter.

## Parameters

- `keychainOrArray`: A reference to a keychain or an array of keychains to search for the associated private key. Specify   to search the user’s default keychain search list.
- `certificateRef`: The certificate for which you want to create an identity.
- `identityRef`: On return, an identity object for the certificate and its associated private key. In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitycreatewithcertificate(_:_:_:))*