# product

**Framework**: StoreKit  
**Kind**: property

The product information of the In-App Purchase the customer selects to purchase outside of the app.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 14.4+

## Declaration

```swift
let product: Product
```

## Mentions

- [Supporting promoted In-App Purchases in your app](supporting-promoted-in-app-purchases-in-your-app.md)
- [Supporting win-back offers in your app](supporting-win-back-offers-in-your-app.md)

#### Discussion

To enable users to complete the purchase they start on the App Store, call [`purchase(options:)`](product/purchase(options:).md) on this product instance.

## See Also

- [var id: Product.ID](purchaseintent/id.md)
  The product identifier of the In-App Purchase that the customer selects to purchase outside of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/purchaseintent/product)*