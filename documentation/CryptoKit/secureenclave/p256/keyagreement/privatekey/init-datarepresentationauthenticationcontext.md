# init(dataRepresentation:authenticationContext:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-256 private key for key agreement from a data representation of the key with the given authentication context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(dataRepresentation: Data, authenticationContext: LAContext? = nil) throws
```

## Parameters

- `dataRepresentation`: A data representation of the key.
- `authenticationContext`: A local authentication context.

## See Also

- [init(dataRepresentation: Data) throws](secureenclave/p256/keyagreement/privatekey/init(datarepresentation:).md)
  Creates a P-256 private key for key agreement from the specified data representation.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl) throws](secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:).md)
  Creates a P-256 private key for key agreement with the specified access control.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:authenticationcontext:).md)
  Creates a P-256 private key for key agreement with the specified access control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(datarepresentation:authenticationcontext:))*