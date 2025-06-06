# custom(key:value:)

**Framework**: StoreKit  
**Kind**: method

Adds data for a custom key to a purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func custom(key: String, value: Data) -> Product.PurchaseOption
```

## Mentions

- [Sending Advanced Commerce API requests from your app](sending-advanced-commerce-api-requests-from-your-app.md)

#### Discussion

Use this custom option with the [`Advanced Commerce API`](https://developer.apple.com/documentation/AdvancedCommerceAPI).

## Parameters

- `key`: The key for this custom option.
- `value`: The data value you assign to this custom option.

## See Also

- [static func custom(key: String, value: String) -> Product.PurchaseOption](product/purchaseoption/custom(key:value:)-3g3nc.md)
  Adds a string for a custom key to a purchase.
- [static func custom(key: String, value: Bool) -> Product.PurchaseOption](product/purchaseoption/custom(key:value:)-8tjim.md)
  Adds a Boolean value for a custom key to a purchase.
- [static func custom(key: String, value: Double) -> Product.PurchaseOption](product/purchaseoption/custom(key:value:)-7rju9.md)
  Adds a number for a custom key to a purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/custom(key:value:)-80cvh)*