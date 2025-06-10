# generate()

**Framework**: Apple CryptoKit  
**Kind**: method

Generates a new random private key.

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
static func generate() throws -> SecureEnclave.MLKEM1024.PrivateKey
```

#### Return Value

The generated private key

#### Discussion

This method implements the required interface for the KEMPrivateKey extension, in this case invoking the initializer with a default SecAccessControl and no LAContext.

## See Also

- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](secureenclave/mlkem1024/privatekey/init(accesscontrol:authenticationcontext:).md)
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](secureenclave/mlkem1024/privatekey/init(datarepresentation:authenticationcontext:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem1024/privatekey/generate())*