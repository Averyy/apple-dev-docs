# generate()

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Generates a new random private key.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
static func generate() throws -> Self
```

#### Return Value

The generated private key.

#### Discussion

Give the [`publicKey`](kemonetimeprivatekey/publickey-swift.property.md) to another person so that they can encapsulate shared secrets that you recover by calling [`decapsulate(_:)`](kemonetimeprivatekey/decapsulate(_:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemonetimeprivatekey/generate())*