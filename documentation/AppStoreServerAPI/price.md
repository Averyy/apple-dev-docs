# price

**Framework**: App Store Server API  
**Kind**: typealias

The price, in milliunits, of the In-App Purchase that the system records in the transaction.

**Availability**:
- App Store Server API 1.10+

## Declaration

```swift
int64 price
```

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)

#### Discussion

This value represents the price, in milliunits of the [`currency`](https://developer.apple.com/documentation/AppStoreServerNotifications/currency), of the In-App Purchase that the system records in the transaction. One unit of the currency equals 1000 milliunits.

The `price` value reflects all of the following:

- The price you configured in App Store Connect, which the system records on the purchase date ([`purchaseDate`](purchasedate.md)).
- The discount from a subscription offer in the [`offerIdentifier`](offeridentifier.md), if the transaction includes an offer.
- The [`quantity`](quantity.md) of a consumable in-app purchase. The price value shows the total amount of the transaction for the quantity the customer purchased.

The following table shows some examples of the `price` and [`currency`](currency.md) parameters based on sample prices you might configure in App Store Connect:

| Configured price in App Store Connect | `price` parameter | `currency` parameter |
| --- | --- | --- |
| $1.99 (U.S. dollar) | 1990 | USD |
| KRW 3300 (South Korean won) | 3300000 | KRW |
| JPY 300 (Japanese yen) | 300000 | JPY |

To determine the storefront, use the [`storefront`](storefront.md) value in the transaction. Don’t use the `currency` value to infer the storefront.

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

For more information on how you set prices, see [`Set a price`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price) and [`Set a price for an in-app purchase`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [type currency](currency.md)
  The three-letter ISO 4217 currency code for the price of the product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/price)*