# currency

**Framework**: StoreKit  
**Kind**: property

The currency of the price of the product.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2, visionOS 1.1)
var currency: Locale.Currency? { get }
```

#### Discussion

The [`currency`](transaction/currency.md) property represents the currency of the product’s [`price`](transaction/price.md) that the system records at the time of purchase.

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

 For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [`currency`](transaction/currency.md) to infer the storefront. Use the [`storefront`](transaction/storefront.md) value in the transaction instead.

To access the transaction’s currency on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9, use [`currencyCode`](product/subscriptioninfo/renewalinfo/currencycode.md).

## See Also

- [var price: Decimal?](transaction/price.md)
  The price of the in-app purchase that the system records in the transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/currency)*