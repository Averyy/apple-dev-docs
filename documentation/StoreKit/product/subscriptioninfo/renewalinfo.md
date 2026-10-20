# Product.SubscriptionInfo.RenewalInfo

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The renewal information for an auto-renewable subscription.

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
struct RenewalInfo
```

## Mentions

- [Merchandising win-back offers in your app](../../merchandising-win-back-offers-in-your-app.md)
- [Supporting offer codes in your app](../../supporting-offer-codes-in-your-app.md)
- [Supporting subscription offer codes in your app](../../supporting-subscription-offer-codes-in-your-app.md)
- [Testing failing subscription renewals and Apple In-App Purchases](../../testing-failing-subscription-renewals-and-in-app-purchases.md)

#### Overview

`Product.SubscriptionInfo.RenewalInfo` provides information about the next subscription renewal period. Check the [`state`](./status-swift.struct/state.md) to determine whether the subscription will be active (subscribed), expired, or in another state at the next renewal period.

## Topics

### Getting the environment
- [let environment: AppStore.Environment](./renewalinfo/environment.md)
  The server environment that signs the renewal information for an auto-renewable subscription.
### Getting the transaction ID
- [let originalTransactionID: UInt64](./renewalinfo/originaltransactionid.md)
  The transaction identifier of the original purchase.
### Identifying the account
- [var appAccountToken: UUID?](./renewalinfo/appaccounttoken.md)
  The app account token you provided during the subscription purchase, if one exists.
- [var appTransactionID: String](./renewalinfo/apptransactionid.md)
  The unique identifier of the app download transaction.
### Getting the product ID
- [let currentProductID: String](./renewalinfo/currentproductid.md)
  The subscription product ID that the customer is subscribed to.
### Getting subscription dates
- [var recentSubscriptionStartDate: Date](./renewalinfo/recentsubscriptionstartdate.md)
  The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.
- [var renewalDate: Date?](./renewalinfo/renewaldate.md)
  The UNIX time, in milliseconds, that the most recent auto-renewable subscription purchase expires.
### Getting the renewal or expiration state
- [let state: Product.SubscriptionInfo.RenewalState](./status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let autoRenewPreference: String?](./renewalinfo/autorenewpreference.md)
  The product ID of the auto-renewable subscription that will automatically renew.
- [let willAutoRenew: Bool](./renewalinfo/willautorenew.md)
  A Boolean value that indicates whether the subscription automatically renews in the next period.
- [let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?](./renewalinfo/expirationreason-swift.property.md)
  The reason the auto-renewable subscription expired.
- [Product.SubscriptionInfo.RenewalInfo.ExpirationReason](./renewalinfo/expirationreason-swift.struct.md)
  The reasons for auto-renewable subscription expirations.
### Getting offers
- [let offer: Transaction.Offer?](./renewalinfo/offer.md)
  A subscription offer that applies to the transaction at the next renewal period.
- [Transaction.Offer](../../transaction/offer-swift.struct.md)
  Discounts or promotions that apply to a transaction.
- [let eligibleWinBackOfferIDs: [String]](./renewalinfo/eligiblewinbackofferids.md)
  An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.
### Getting the renewal price and currency
- [var renewalPrice: Decimal?](./renewalinfo/renewalprice.md)
  The renewal price of the auto-renewable subscription that renews at the next billing period.
- [var currency: Locale.Currency?](./renewalinfo/currency.md)
  The currency of the subscription’s renewal price.
### Getting billing status
- [let isInBillingRetry: Bool](./renewalinfo/isinbillingretry.md)
  A Boolean value that indicates whether an auto-renewable subscription is in the billing retry period.
- [let gracePeriodExpirationDate: Date?](./renewalinfo/graceperiodexpirationdate.md)
  The date the billing grace period expires for the auto-renewable subscription.
### Getting the price increase status
- [Managing Price Increases for Auto-Renewable Subscriptions](../../managing-price-increases-for-auto-renewable-subscriptions.md)
  Identify the price increase status for auto-renewable subscriptions in your app and on your server.
- [let priceIncreaseStatus: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus](./renewalinfo/priceincreasestatus-swift.property.md)
  The status that indicates whether the auto-renewable subscription is subject to a price increase.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus](./renewalinfo/priceincreasestatus-swift.enum.md)
  Status values that indicate whether an auto-renewable subscription is subject to a price increase.
### Verifying subscription renewal information
- [let deviceVerification: Data](./renewalinfo/deviceverification.md)
  The device verification value to use to verify whether the renewal information belongs to the device.
- [let deviceVerificationNonce: UUID](./renewalinfo/deviceverificationnonce.md)
  The UUID to use to compute the device verification value.
- [let signedDate: Date](./renewalinfo/signeddate.md)
  The date that the App Store signed the JWS renewal information.
### Getting subscription renewal info in JSON format
- [var jsonRepresentation: Data](./renewalinfo/jsonrepresentation.md)
  The JSON representation of the subscription renewal information.
### Getting renewal information for Advanced Commerce API
- [let advancedCommerceInfo: Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo?](./renewalinfo/advancedcommerceinfo-swift.property.md)
  Renewal information for a subscription that uses the Advanced Commerce API.
- [Product.SubscriptionInfo.RenewalInfo.AdvancedCommerceInfo](./renewalinfo/advancedcommerceinfo-swift.struct.md)
  Renewal information for subscriptions that use the Advanced Commerce API.
### Deprecated
- [var environmentStringRepresentation: String](./renewalinfo/environmentstringrepresentation.md)
  The string representation of the server environment that signs the renewal information for an auto-renewable subscription.
- [var offerID: String?](./renewalinfo/offerid.md)
  A string that identifies an offer that applies to the next subscription period.
- [var offerType: Transaction.OfferType?](./renewalinfo/offertype.md)
  The subscription offer type for the next subscription period.
- [var currencyCode: String?](./renewalinfo/currencycode.md)
  The three-letter ISO 4217 currency code for the price of the product.
- [var offerPaymentModeStringRepresentation: String?](./renewalinfo/offerpaymentmodestringrepresentation.md)
- [var offerPeriodStringRepresentation: String?](./renewalinfo/offerperiodstringrepresentation.md)
  The string representation of the subscription offer period applied to the next billing period.
### Structures
- [Product.SubscriptionInfo.RenewalInfo.CommitmentInfo](./renewalinfo/commitmentinfo-swift.struct.md)
### Instance Properties
- [var bundleOriginalTransactionID: String?](./renewalinfo/bundleoriginaltransactionid.md)
- [var bundleProductID: String?](./renewalinfo/bundleproductid.md)
  Identifies the bundle product the next renewal is for. If the next renewal is created as part of a subscription bundle, this field will be populated with the product ID of the bundle.
- [var bundleSubscriptionGroupID: String?](./renewalinfo/bundlesubscriptiongroupid.md)
  Identifies the subscription bundle group the next renewal is for.
- [let commitmentInfo: Product.SubscriptionInfo.RenewalInfo.CommitmentInfo?](./renewalinfo/commitmentinfo-swift.property.md)
- [let renewalBillingPlanType: SubscriptionInfo.BillingPlanType?](./renewalinfo/renewalbillingplantype.md)
- [var willUnbundle: Bool](./renewalinfo/willunbundle.md)
  Whether the subscription will leave the bundle at the next renewal and renew as a standalone product.

## Relationships

### Conforms To
- [Copyable](../../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../../Swift/customdebugstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Escapable](../../../Swift/escapable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Subscription status and renewal information
- [Product.SubscriptionInfo.Status](./status-swift.struct.md)
  The renewal status information for an auto-renewable subscription.
- [typealias SubscriptionRenewalInfo](../../subscriptionrenewalinfo.md)
  Represents the renewal information for an auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalState](./renewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionRenewalState](../../subscriptionrenewalstate.md)
  The renewal states of auto-renewable subscriptions.
- [typealias SubscriptionPeriod](../../subscriptionperiod.md)
  Represents the duration of time between subscription renewals.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo)*