# price

**Framework**: StoreKit  
**Kind**: property

The price of the in-app purchase that the system records in the transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 17.2, macOS 14.2, tvOS 17.2, watchOS 10.2, visionOS 1.1)
var price: Decimal? { get }
```

#### Discussion

This value represents the price of the in-app purchase, in units of the [`currency`](transaction/currency.md), that the system records in the transaction. The [`price`](transaction/price.md) value reflects all of the following:

- The price you configured in App Store Connect, which the system records on the purchase date ([`purchaseDate`](transaction/purchasedate.md)).
- The discount from a subscription offer in the [`offer`](transaction/offer-swift.property.md) property, if the transaction includes an offer.
- The [`purchasedQuantity`](transaction/purchasedquantity.md) of a consumable in-app purchase. The price value shows the total amount of the transaction for the quantity that the customer purchased.

> ❗ **Important**:  For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

 For financial and accounting purposes, use the App Store Connect reporting tools. For more information, see [`Download financial reports`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/getting-paid/download-financial-reports) and [`Overview of reporting tools`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/measure-app-performance/overview-of-reporting-tools).

The decoded payloads of [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) and the [`JWSTransaction`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransaction) strings from the App Store server APIs contain [`price`](https://developer.apple.com/documentation/AppStoreServerAPI/price) fields specified in  of the currency. StoreKit represents the [`price`](transaction/price.md) value in  of the currency. Take care not to confuse these two representations when working with both APIs.

You configure prices in App Store Connect. For more information, see [`Set a price for an in-app purchase`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-in-app-purchases/set-a-price-for-an-in-app-purchase).

## See Also

- [var currency: Locale.Currency?](transaction/currency.md)
  The currency of the price of the product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/price)*