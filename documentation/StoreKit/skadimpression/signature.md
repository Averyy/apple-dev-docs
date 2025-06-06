# signature

**Framework**: StoreKit  
**Kind**: property

The advertising network’s cryptographic signature for the ad impression.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+

## Declaration

```swift
var signature: String { get set }
```

## Mentions

- [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md)
- [Signing and providing ads](signing-and-providing-ads.md)

#### Discussion

The ad network creates a cryptographic signature that it uses to sign ads. For instructions on generating this value, see [`Generating the signature to validate view-through ads`](generating-the-signature-to-validate-view-through-ads.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skadimpression/signature)*