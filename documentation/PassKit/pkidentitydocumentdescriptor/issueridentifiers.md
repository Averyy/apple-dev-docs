# issuerIdentifiers

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Required**: Yes

A list of X.509 authority key identifiers which are accepted by the relying party.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var issuerIdentifiers: [Data] { get set }
```

#### Discussion

An empty list means any document signer certificate is acceptable.

> ⚠️ **Warning**: The number of issuer identifiers must not exceed 1,000 and the size of each identifier must not exceed 64 bytes. Your app will terminate if these conditions are not met.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitydocumentdescriptor/issueridentifiers)*