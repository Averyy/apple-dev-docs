# init(compactRepresentable:accessControl:authenticationContext:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a P-256 private key for key agreement with the specified access control.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init(compactRepresentable: Bool = true, accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!, authenticationContext: LAContext? = nil) throws
```

## Parameters

- `compactRepresentable`: A Boolean value that indicates whether CryptoKit creates the key with the structure to enable compact point encoding.
- `accessControl`: The protection type and flags to use when creating the associated access control object.
- `authenticationContext`: A local authentication context.

## See Also

### Creating a private key
- [init(dataRepresentation: Data, authenticationContext: LAContext?) throws](./init%28datarepresentation,authenticationcontext%29.md)
  Creates a P-256 private key for key agreement from a data representation of the key with the given authentication context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:authenticationcontext:))*