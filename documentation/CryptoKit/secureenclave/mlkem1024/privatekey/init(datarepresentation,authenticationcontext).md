# init(dataRepresentation:authenticationContext:)

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
init<D>(dataRepresentation: D, authenticationContext: LAContext? = nil) throws where D : DataProtocol
```

## See Also

### Creating a private key
- [static func generate() throws -> SecureEnclave.MLKEM1024.PrivateKey](./generate%28%29.md)
  Generates a new random private key.
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](./init%28accesscontrol,authenticationcontext%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey/init(datarepresentation:authenticationcontext:))*