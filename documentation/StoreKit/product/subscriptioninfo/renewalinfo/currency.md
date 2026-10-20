# currency

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The currency of the subscription’s renewal price.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
var currency: Locale.Currency? { get }
```

#### Discussion

The [`currency`](./currency.md) value applies to the product’s [`renewalPrice`](./renewalprice.md) instance.

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [Download financial reports](https://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [Overview of reporting tools](https://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

Don’t use [`currency`](./currency.md) to infer the storefront. Use the [`storefront`](../../../transaction/storefront.md) value in the transaction instead.

To access the renewal price currency on systems earlier than iOS 16, iPadOS 16, macOS 13, tvOS 16, and watchOS 9, use [`currencyCode`](./currencycode.md).

## See Also

### Getting the renewal price and currency
- [var renewalPrice: Decimal?](./renewalprice.md)
  The renewal price of the auto-renewable subscription that renews at the next billing period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/currency)*