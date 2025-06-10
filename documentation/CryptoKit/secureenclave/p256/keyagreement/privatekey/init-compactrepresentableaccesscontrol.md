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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/p256/keyagreement/privatekey/init(compactrepresentable:accesscontrol:))*