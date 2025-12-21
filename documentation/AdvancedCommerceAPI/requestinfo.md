# RequestInfo

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The metadata to include in server requests.

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```swift
object RequestInfo
```

#### Discussion

You provide the `RequestInfo` in your Advanced Commerce API server requests to uniquely identify your requests. You also have the option to provide additional data in the `RequestInfo` object.

##### Include the App Account Token Optionally

You can include an `appAccountToken` in `RequestInfo` to associate an account on your system with the purchase. The App Store returns the same `appAccountToken` value in the transaction information.

If you include `appAccountToken` in the `RequestInfo`, you don’t need to include the app account token as a purchase option by adding [`appAccountToken(_:)`](https://developer.apple.com/documentation/StoreKit/Product/PurchaseOption/appAccountToken(_:)) to the product purchase options ([`purchase(options:)`](https://developer.apple.com/documentation/StoreKit/Product/purchase(options:))).

> ❗ **Important**: If you do include `appAccountToken` in the `purchase(options:)`, you must include the same app account token value in the `RequestInfo`; otherwise, the request fails.

For more information about sending API requests from your app, see [`Sending Advanced Commerce API requests from your app`](https://developer.apple.com/documentation/StoreKit/sending-advanced-commerce-api-requests-from-your-app).

##### Include the Consistency Token Optionally

The consistency token helps prevent unintended operations that might occur when the server gets multiple or overlapping requests for the same subscription.

Subscriptions receive a new consistency token in the [`advancedCommerceRenewalInfo`](https://developer.apple.com/documentation/AppStoreServerAPI/advancedCommerceRenewalInfo) object of the [`JWSRenewalInfo`](jwsrenewalinfo.md) each time the system updates the subscrpition renewal information. Include the consistency token when you use the [`SubscriptionCreateRequest`](subscriptioncreaterequest.md) operation to resubscribe to the subscription and provide the `previousTransactionID`.

Don’t include a consistency token when:

- You haven’t received a consistency token.
- You’re using the [`OneTimeChargeCreateRequest`](onetimechargecreaterequest.md) operation.
- You’re using the [`SubscriptionCreateRequest`](subscriptioncreaterequest.md) operation for an initial subscription purchase.

## See Also

- [object Descriptors](descriptors.md)
  The display name and description of a subscription product.
- [object Offer](offer.md)
  A discount offer for an auto-renewable subscription.
- [object SubscriptionModifyAddItem](subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyChangeItem](subscriptionmodifychangeitem.md)
  The data your app provides to change an item of an auto-renewable subscription.
- [object SubscriptionModifyDescriptors](subscriptionmodifydescriptors.md)
  The data your app provides to change the description and display name of an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.
- [object SubscriptionModifyRemoveItem](subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionPriceChangeItem](subscriptionpricechangeitem.md)
  The data your app provides to change a subscription price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/requestinfo)*