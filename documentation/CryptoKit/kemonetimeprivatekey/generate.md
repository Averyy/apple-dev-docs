# generate()

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Generates a new random private key.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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