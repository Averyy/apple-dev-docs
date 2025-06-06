# init(compactRepresentable:accessControl:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a P-256 private key for key agreement with the specified access control.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
init(compactRepresentable: Bool = true, accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!) throws
```

## Parameters

- `compactRepresentable`: A Boolean value that indicates   whether CryptoKit creates the key with the structure to   enable compact point encoding.
- `accessControl`: The protection type and flags to use   when creating the associated access control object.

## See Also

- [init(dataRepresentation: Data) throws](secureenclave/p256/keyagreement/privatekey/init(datarepresentation:).md)
  Creates a P-256 private key for key agreement from the specified data representation.
- [init(dataRepresentation: Data, authenticationContext: LAContext?) throws](secureenclave/p256/keyagreement/privatekey/init(datarepresentation:authenticationcontext:).md)
  Creates a P-256 private key for key agreement from a data representation of the key with the given authentication context.
- [init(compactRepresentable: Bool, accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:authenticationcontext:).md)
  Creates a P-256 private key for key agreement with the specified access control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:))*