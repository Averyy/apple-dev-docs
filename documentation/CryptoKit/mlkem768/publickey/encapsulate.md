# encapsulate()

**Framework**: Apple CryptoKit  
**Kind**: method

Generates and encapsulates a shared secret.

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
func encapsulate() throws -> KEM.EncapsulationResult
```

#### Return Value

An encapsulated shared secret, that you decapsulate by calling [`decapsulate(_:)`](mlkem768/privatekey/decapsulate(_:).md) on the corresponding private key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/publickey/encapsulate())*