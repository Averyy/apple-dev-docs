# init(dataRepresentation:authenticationContext:)

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
init<D>(dataRepresentation: D, authenticationContext: LAContext? = nil) throws where D : DataProtocol
```

## See Also

- [static func generate() throws -> SecureEnclave.MLKEM1024.PrivateKey](secureenclave/mlkem1024/privatekey/generate.md)
  Generates a new random private key.
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/mlkem1024/privatekey/init(accesscontrol:authenticationcontext:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey/init(datarepresentation:authenticationcontext:))*