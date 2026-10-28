# generate()

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Type Method  
**Required**: Yes

Generates a new random private key.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static func generate() throws -> Self
```

## Return Value

The generated private key.

## Discussion

Give the [`publicKey`](./publickey-swift.property.md) to another person so that they can encapsulate shared secrets that you recover by calling [`decapsulate(_:)`](./decapsulate%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kemprivatekey/generate())*