# onStorefrontChange(shouldContinuePurchase:)

**Framework**: StoreKit  
**Kind**: method

A closure that determines whether the transaction continues if the device’s App Store storefront changes during a transaction.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
static func onStorefrontChange(shouldContinuePurchase: @escaping (Storefront) -> Bool) -> AdvancedCommerceProduct.PurchaseOption
```

#### Discussion

The default is `true` if you don’t include this option in the purchase options.

## Parameters

- `shouldContinuePurchase`: A closure that returns a Boolean value that determines whether the purchase continues when the storefront changes to   during the purchase process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchaseoption/onstorefrontchange(shouldcontinuepurchase:))*