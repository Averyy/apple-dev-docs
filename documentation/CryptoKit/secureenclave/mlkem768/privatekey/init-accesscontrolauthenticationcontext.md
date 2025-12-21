# init(accessControl:authenticationContext:)

**Framework**: Apple CryptoKit  
**Kind**: init

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!, authenticationContext: LAContext? = nil) throws
```

## See Also

- [static func generate() throws -> SecureEnclave.MLKEM768.PrivateKey](secureenclave/mlkem768/privatekey/generate.md)
  Generates a new random private key.
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](secureenclave/mlkem768/privatekey/init(datarepresentation:authenticationcontext:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem768/privatekey/init(accesscontrol:authenticationcontext:))*