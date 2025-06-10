# encapsulate()

**Framework**: Apple CryptoKit  
**Kind**: method

Generates and encapsulates a shared secret.

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
func encapsulate() throws -> KEM.EncapsulationResult
```

#### Return Value

An encapsulated shared secret, that you decapsulate by calling [`decapsulate(_:)`](mlkem768/privatekey/decapsulate(_:).md) on the corresponding private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/publickey/encapsulate())*