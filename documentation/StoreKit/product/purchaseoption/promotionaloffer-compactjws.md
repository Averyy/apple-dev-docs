# promotionalOffer(_:compactJWS:)

**Framework**: StoreKit  
**Kind**: method

Apply a promotional offer to a purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 26.0, macOS 26.0, tvOS 26.0, watchOS 26.0, visionOS 26.0)
static func promotionalOffer(_ offerID: String, compactJWS: String) -> [Product.PurchaseOption]
```

## Parameters

- `offerID`: The   property of the   to apply.
- `compactJWS`: The JWS signature used to validate a promotional offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/promotionaloffer(_:compactjws:))*