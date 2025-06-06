# onStorefrontChange(shouldContinuePurchase:)

**Framework**: StoreKit  
**Kind**: method

Indicates whether a transaction needs to continue if the App Store storefront changes on the device during the transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@preconcurrency
static func onStorefrontChange(shouldContinuePurchase: @escaping (Storefront) -> Bool) -> Product.PurchaseOption
```

#### Return Value

[`Product.PurchaseOption`](product/purchaseoption.md)

#### Discussion

The default value is `true` if this option isn’t added to the purchase.

## Parameters

- `shouldContinuePurchase`: A closure that returns a Boolean value to indicate whether the purchase needs to continue when the App Store storefront changes to the   value during a transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/purchaseoption/onstorefrontchange(shouldcontinuepurchase:))*