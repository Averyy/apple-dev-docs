# custom(key:value:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

Adds a number for a custom key to a purchase.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func custom(key: String, value: Double) -> Product.PurchaseOption
```

## Discussion

This custom purchase option doesn’t have any effect.

## Parameters

- `key`: The key for this custom option.
- `value`: The numerical value you assign to this custom option.

## See Also

### Setting custom purchase options
- [static func custom(key: String, value: Data) -> Product.PurchaseOption](./custom%28key,value%29-80cvh.md)
  Adds data for a custom key to a purchase.
- [static func custom(key: String, value: String) -> Product.PurchaseOption](./custom%28key,value%29-3g3nc.md)
  Adds a string for a custom key to a purchase.
- [static func custom(key: String, value: Bool) -> Product.PurchaseOption](./custom%28key,value%29-8tjim.md)
  Adds a Boolean value for a custom key to a purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/custom(key:value:)-7rju9)*