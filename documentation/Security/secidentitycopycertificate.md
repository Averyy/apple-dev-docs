# SecIdentityCopyCertificate(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves a certificate associated with an identity.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func SecIdentityCopyCertificate(_ identityRef: SecIdentity, _ certificateRef: UnsafeMutablePointer<SecCertificate?>) -> OSStatus
```

## Mentions

- [Parsing an Identity](parsing-an-identity.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

An identity is a digital certificate together with its associated private key.

For a certificate in a keychain, you can cast the `SecCertificateRef` data type to a `SecKeychainItemRef` for use with Keychain Services functions.

## Parameters

- `identityRef`: The identity object for the identity whose certificate you wish to retrieve.
- `certificateRef`: On return, points to the certificate object associated with the specified identity. In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitycopycertificate(_:_:))*