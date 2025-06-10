# Product.SubscriptionInfo.RenewalInfo

**Framework**: StoreKit  
**Kind**: struct

The renewal information for an auto-renewable subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct RenewalInfo
```

## Mentions

- [Supporting subscription offer codes in your app](supporting-subscription-offer-codes-in-your-app.md)
- [Merchandising win-back offers in your app](merchandising-win-back-offers-in-your-app.md)
- [Testing failing subscription renewals and In-App Purchases](testing-failing-subscription-renewals-and-in-app-purchases.md)

#### Overview

`Product.SubscriptionInfo.RenewalInfo` provides information about the next subscription renewal period. Check the [`state`](product/subscriptioninfo/status-swift.struct/state.md) to determine whether the subscription will be active (subscribed), expired, or in another state at the next renewal period.

## Topics

### Getting the environment
- [let environment: AppStore.Environment](product/subscriptioninfo/renewalinfo/environment.md)
  The server environment that signs the renewal information for an auto-renewable subscription.
### Getting the transaction ID
- [let originalTransactionID: UInt64](product/subscriptioninfo/renewalinfo/originaltransactionid.md)
  The transaction identifier of the original purchase.
### Identifying the account
- [var appAccountToken: UUID?](product/subscriptioninfo/renewalinfo/appaccounttoken.md)
  The app account token you provided during the subscription purchase, if one exists.
- [var appTransactionID: String](product/subscriptioninfo/renewalinfo/apptransactionid.md)
  The unique identifier of the app download transaction.
### Getting the product ID
- [let currentProductID: String](product/subscriptioninfo/renewalinfo/currentproductid.md)
  The subscription product ID that the customer is subscribed to.
### Getting subscription dates
- [var recentSubscriptionStartDate: Date](product/subscriptioninfo/renewalinfo/recentsubscriptionstartdate.md)
  The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.
- [var renewalDate: Date?](product/subscriptioninfo/renewalinfo/renewaldate.md)
  The UNIX time, in milliseconds, that the most recent auto-renewable subscription purchase expires.
### Getting the renewal or expiration state
- [let state: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let autoRenewPreference: String?](product/subscriptioninfo/renewalinfo/autorenewpreference.md)
  The product ID of the auto-renewable subscription that will automatically renew.
- [let willAutoRenew: Bool](product/subscriptioninfo/renewalinfo/willautorenew.md)
  A Boolean value that indicates whether the subscription automatically renews in the next period.
- [let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md)
  The reason the auto-renewable subscription expired.
- [Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct.md)
  The reasons for auto-renewable subscription expirations.
### Getting subscription offers
- [let offer: Transaction.Offer?](product/subscriptioninfo/renewalinfo/offer.md)
  A subscription offer that applies to the transaction at the next renewal period.
- [Transaction.Offer](transaction/offer-swift.struct.md)
  The subscription offers that apply to a transaction.
- [let eligibleWinBackOfferIDs: [String]](product/subscriptioninfo/renewalinfo/eligiblewinbackofferids.md)
  An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.
### Getting the renewal price and currency
- [var renewalPrice: Decimal?](product/subscriptioninfo/renewalinfo/renewalprice.md)
  The renewal price of the auto-renewable subscription that renews at the next billing period.
- [var currency: Locale.Currency?](product/subscriptioninfo/renewalinfo/currency.md)
  The currency of the subscription’s renewal price.
### Getting billing status
- [let isInBillingRetry: Bool](product/subscriptioninfo/renewalinfo/isinbillingretry.md)
  A Boolean value that indicates whether an auto-renewable subscription is in the billing retry period.
- [let gracePeriodExpirationDate: Date?](product/subscriptioninfo/renewalinfo/graceperiodexpirationdate.md)
  The date the billing grace period expires for the auto-renewable subscription.
### Getting the price increase status
- [Managing Price Increases for Auto-Renewable Subscriptions](managing-price-increases-for-auto-renewable-subscriptions.md)
  Identify the price increase status for auto-renewable subscriptions in your app and on your server.
- [let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.property.md)
  The status that indicates whether the auto-renewable subscription is subject to a price increase.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus](product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum.md)
  Status values that indicate whether an auto-renewable subscription is subject to a price increase.
### Verifying subscription renewal information
- [let deviceVerification: Data](product/subscriptioninfo/renewalinfo/deviceverification.md)
  The device verification value to use to verify whether the renewal information belongs to the device.
- [let deviceVerificationNonce: UUID](product/subscriptioninfo/renewalinfo/deviceverificationnonce.md)
  The UUID to use to compute the device verification value.
- [let signedDate: Date](product/subscriptioninfo/renewalinfo/signeddate.md)
  The date that the App Store signed the JWS renewal information.
### Getting subscription renewal info in JSON format
- [var jsonRepresentation: Data](product/subscriptioninfo/renewalinfo/jsonrepresentation.md)
  The JSON representation of the subscription renewal information.
### Getting renewal information for Advanced Commerce API
- [let advancedCommerceInfo: Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo?](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.property.md)
  Renewal information for a subscription that uses the Advanced Commerce API.
- [Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo](product/subscriptioninfo/renewalinfo/advancedcommerceinfo-swift.struct.md)
  Renewal information for subscriptions that use the Advanced Commerce API.
### Deprecated
- [var environmentStringRepresentation: String](product/subscriptioninfo/renewalinfo/environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](product/subscriptioninfo/renewalinfo/offerid.md)
  A string that identifies an offer applied to the next subscription period.
- [var offerType: Transaction.OfferType?](product/subscriptioninfo/renewalinfo/offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](product/subscriptioninfo/renewalinfo/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPaymentModeStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](product/subscriptioninfo/renewalinfo/offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Product.SubscriptionInfo.Status](product/subscriptioninfo/status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.
- [typealias SubscriptionRenewalInfo](subscriptionrenewalinfo.md)
  Represents the renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/renewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionRenewalState](subscriptionrenewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionPeriod](subscriptionperiod.md)
  Represents the duration of time between subscription renewals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo)*