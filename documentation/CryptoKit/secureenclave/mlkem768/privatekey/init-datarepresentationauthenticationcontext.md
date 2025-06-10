# init(dataRepresentation:authenticationContext:)

**Framework**: Apple CryptoKit  
**Kind**: init

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
init<D>(dataRepresentation: D, authenticationContext: LAContext? = nil) throws where D : DataProtocol
```

## See Also

- [static func generate() throws -> SecureEnclave.MLKEM768.PrivateKey](secureenclave/mlkem768/privatekey/generate.md)
  Generates a new random private key.
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/mlkem768/privatekey/init(accesscontrol:authenticationcontext:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem768/privatekey/init(datarepresentation:authenticationcontext:))*