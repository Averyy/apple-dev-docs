# init(accessControl:authenticationContext:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(accessControl: SecAccessControl = SecAccessControlCreateWithFlags(nil, kSecAttrAccessibleAfterFirstUnlockThisDeviceOnly, [], nil)!, authenticationContext: LAContext? = nil) throws
```

## See Also

### Creating a private key
- [static func generate() throws -> SecureEnclave.MLKEM1024.PrivateKey](./generate%28%29.md)
  Generates a new random private key.
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](./init%28datarepresentation,authenticationcontext%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey/init(accesscontrol:authenticationcontext:))*