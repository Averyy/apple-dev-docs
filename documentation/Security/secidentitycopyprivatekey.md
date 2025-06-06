# SecIdentityCopyPrivateKey(_:_:)

**Framework**: Security  
**Kind**: func

Retrieves the private key associated with an identity.

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
func SecIdentityCopyPrivateKey(_ identityRef: SecIdentity, _ privateKeyRef: UnsafeMutablePointer<SecKey?>) -> OSStatus
```

## Mentions

- [Parsing an Identity](parsing-an-identity.md)

#### Return Value

A result code. See [`Security Framework Result Codes`](security-framework-result-codes.md).

#### Discussion

An identity is a digital certificate together with its associated private key.

## Parameters

- `identityRef`: The identity object for the identity whose private key you wish to retrieve.
- `privateKeyRef`: On return, points to the private key object for the specified identity. The private key must be of class type  . In Objective-C, call the   function to release this object when you are finished with it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secidentitycopyprivatekey(_:_:))*