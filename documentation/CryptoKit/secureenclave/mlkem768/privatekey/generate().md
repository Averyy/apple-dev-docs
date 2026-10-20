# generate()

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Type Method

Generates a new random private key.

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
static func generate() throws -> SecureEnclave.MLKEM768.PrivateKey
```

#### Return Value

The generated private key

#### Discussion

This method implements the required interface for the KEMPrivateKey extension, in this case invoking the initializer with a default SecAccessControl and no LAContext.

## See Also

### Creating a private key
- [init(accessControl: SecAccessControl, authenticationContext: LAContext?) throws](./init%28accesscontrol,authenticationcontext%29.md)
- [init<D>(dataRepresentation: D, authenticationContext: LAContext?) throws](./init%28datarepresentation,authenticationcontext%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/secureenclave/mlkem768/privatekey/generate())*