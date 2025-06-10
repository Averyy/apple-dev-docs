# encapsulate()

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

Generates and encapsulates a shared secret.

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
func encapsulate() throws -> KEM.EncapsulationResult
```

#### Return Value

The shared secret, and its encapsulated version.

#### Discussion

Share the encapsulated secret with the person who has the [`KEMPrivateKey`](kemprivatekey.md). They use [`decapsulate(_:)`](kemprivatekey/decapsulate(_:).md) to recover the shared secret.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/kempublickey/encapsulate())*