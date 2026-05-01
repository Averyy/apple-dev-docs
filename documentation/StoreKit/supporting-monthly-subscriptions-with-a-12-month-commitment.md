# Supporting monthly subscriptions with a 12-month commitment

**Framework**: StoreKit

Configure, merchandise, and grant access to a monthly subscription with a 12-month commitment.

#### Overview

A *monthly subscription with a 12-month commitment* is an auto-renewable subscription that bills monthly and has a yearly commitment. The commitment automatically renews for another 12-month commitment after all 12 payments are complete, unless the customer cancels before the renewal date. By comparison, a standard annual subscription bills customers once, up front; it renews for a year, with a single up-front payment, unless the customer cancels.

Within your app, each billing period behaves like a standard monthly subscription — each period produces an independent transaction and grants one month of access. The distinction is that the customer has committed to the full year, so billing continues through all 12 periods even if the customer cancels the commitment renewal early.

Supporting a monthly subscription with a 12-month commitment involves the following steps:

- Configuring the subscription in App Store Connect, including planning for upgrades and downgrades
- Merchandising the subscription for customers to purchase
- Initiating the purchase
- Handling the transaction and entitlements
- Displaying the commitment progress

This feature requires using Xcode 26.5 SDK or later. You can deploy monthly subscriptions with 12-month commitments worldwide (except the United States and Singapore) to customers with devices running iOS 26.4, iPadOS 26.4, macOS 26.4, tvOS 26.4, and visionOS 26.4 or later.

Use  [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) to manage the subscription life cycle on your server. Transactions are available in your app through StoreKit, and on the server through the [`App Store Server API`](https://developer.apple.com/documentation/AppStoreServerAPI) and App Store Server Notifications APIs.

This article uses the term *commitment plan* to refer to a monthly subscription with a 12-month commitment.

#### Understand the Customer Experience

The first time a customer subscribes to a monthly subscription with a 12-month commitment, the system automatically presents a one-time disclosure sheet. This sheet explains the number of monthly payments and provides cancellation guidance. The system shows it once per Apple Account, and it requires no action from you.

In subscription settings, customers see a commitment module that displays how many payments remain and when their commitment renews. A cancellation applies to the annual renewal, not to the remaining months in the commitment period. If a customer initiates cancellation, a message on the cancellation sheet reminds them of their commitment status and the number of remaining payments. After canceling, the customer can view the remaining scheduled payments for the commitment period.

#### Understand the Billing Plan Type

Every auto-renewable subscription carries a [`Product.SubscriptionInfo.BillingPlanType`](product/subscriptioninfo/billingplantype.md) value that describes how the subscription bills. There are two billing plans:

- An *up-front* billing plan type is the default for standard auto-renewable subscriptions. The subscription bills in full, up front, for the billing period.
- A *monthly* billing plan type applies only to monthly subscriptions with a 12-month commitment. The subscription bills at the monthly rate, once a month, for the duration of the commitment.

The transaction information in StoreKit and the server APIs provides the billing plan type, as follows:

| Billing Plan Type | StoreKit API | `JWSTransaction` and `JWSRenewalInfo` |
| --- | --- | --- |
| Up-front | [`upFront`](product/subscriptioninfo/billingplantype/upfront.md) | `BILLED_UPFRONT` |
| Monthly | [`monthly`](product/subscriptioninfo/billingplantype/monthly.md) | `MONTHLY` |

The product metadata, transactions, and subscription renewal information contain this value.

#### Configure the Subscription in App Store Connect

A monthly subscription with a 12-month commitment isn’t a new product type; you configure it directly on an existing yearly auto-renewable subscription in App Store Connect. The product ID and subscription group remain the same — you add a new billing plan to an existing product.

To configure the billing plan:

1. Log in to [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com/login).
2. Navigate to your app’s In-App Purchases section and select the yearly auto-renewable subscription you want to update.
3. Enable the monthly billing plan type for that product.
4. Set a monthly price per territory.

Because both the up-front annual plan and the monthly commitment plan share the same product ID, customers and your app interact with a single subscription product that now offers two billing options.

#### Manage Subscription Groups for Upgrades and Downgrades

When configuring subscriptions in App Store Connect, you place subscriptions in subscription groups. The order in which subscriptions appear in a group determine the upgrade, downgrade, and cross-grade choices that customers see for each group.

Plan changes within a subscription group follow the existing upgrade, downgrade, and crossgrade rules with a few commitment plan-specific behaviors, as follows:

- **Upgrades** are immediate. When a customer upgrades from a commitment plan to a higher-tier subscription, the commitment ends immediately and the new plan activates. Customers may receive a prorated refund for the unused portion of the commitment’s current period.
- **Downgrades** are deferred. When a customer selects a lower-tier plan, the change takes effect at the end of the current 12-month commitment. The customer continues on the commitment plan and its billing schedule until the commitment completes.
- **Cross-grades** follow timing rules that depend on the plan duration and the billing plan type of both the current and target plans. Refer to the App Store Connect documentation for crossgrade timing details.

Plan the tiers in your subscription group carefully to achieve the desired upgrade, downgrade, and cross-grade behavior.

#### Merchandise Monthly Subscriptions with 12 Month Commitments

Use the [`Product`](product.md) API to fetch information for all your In-App Purchases, including monthly subscriptions with 12-month commitments. Use this information to display a store within your app to offer In-App Purchases.

To specifically identify monthly subscriptions with 12-month commitments, check the [`pricingTerms`](product/subscriptioninfo/pricingterms-swift.property.md) property in [`SubscriptionInfo`](subscriptioninfo.md). This array returns one entry for each available billing plan. For a 1-year subscription with monthly billing enabled, it contains two entries:

- The standard annual billing plan, with `billingPlanType` equal to `.upFront`
- The monthly commitment plan, with `billingPlanType` equal to `.monthly`

By comparison, a standard subscription returns only the first entry, with the `billingPlanType` equal to `.upFront`.

Each entry in a [`pricingTerms`](product/subscriptioninfo/pricingterms-swift.property.md) object contains the following properties:

| Property | Definition |
| --- | --- |
| [`billingPlanType`](product/subscriptioninfo/pricingterms-swift.struct/billingplantype.md) | Indicates whether the plan bills upfront or monthly |
| [`commitmentInfo`](product/subscriptioninfo/pricingterms-swift.struct/commitmentinfo.md) | Commitment details including total price and number of periods |
| [`billingDisplayPrice`](product/subscriptioninfo/pricingterms-swift.struct/billingdisplayprice.md) | The price to display for the billing period |
| [`billingPeriod`](product/subscriptioninfo/pricingterms-swift.struct/billingperiod.md) | The duration of each billing period |
| [`subscriptionOffers`](product/subscriptioninfo/pricingterms-swift.struct/subscriptionoffers.md) | Subscription offers that apply to this billing plan |

The following code example filters the product’s list of pricing terms to find the billing information for the 12-month commitment:

```swift
if let commitmentTerms = product.subscription?.pricingTerms.first(where: { $0.billingPlanType == .monthly }) {
    let monthlyPrice = commitmentTerms.billingDisplayPrice
    let totalCommitmentPrice = commitmentTerms.commitmentInfo.price
    // Display both monthly and total commitment amounts to the customer before purchase.
}
```

You’re required to display both the monthly billing price and the total commitment amount to the customer before they initiate a purchase.

#### Provide Subscription Offers

Subscription offers—including introductory offers, promotional offers, win-back offers, and offer codes—are specific to each billing plan. When you fetch the pricing terms for a product, [`pricingTerms`](product/subscriptioninfo/pricingterms-swift.property.md) for a [`Product`](product.md), each entry’s [`subscriptionOffers`](product/subscriptioninfo/pricingterms-swift.struct/subscriptionoffers.md) property contains only the offers that apply to that billing plan.

To display offers for the commitment plan, read the [`subscriptionOffers`](product/subscriptioninfo/pricingterms-swift.struct/subscriptionoffers.md) property from the pricing terms entry where the [`Product.SubscriptionInfo.BillingPlanType`](product/subscriptioninfo/billingplantype.md) is [`monthly`](product/subscriptioninfo/billingplantype/monthly.md).

#### Initiate a Purchase

To initiate a purchase for a commitment plan, use the same `product.purchase(options:)` call you already use for other subscriptions. The only addition is a new purchase option, a [`Product.SubscriptionInfo.BillingPlanType`](product/subscriptioninfo/billingplantype.md) set to [`monthly`](product/subscriptioninfo/billingplantype/monthly.md), which tells StoreKit which billing plan the customer is purchasing for the subscription.

The following code example initiates a purchase for a monthly subscription with a 12-month commitment:

```swift
let result = try await product.purchase(options: [.billingPlanType(.monthly)])

switch result {
case .success(let verificationResult):
    // Verify and process the transaction.
case .pending:
    // The purchase requires action from the customer. 
case .userCancelled:
    // The customer canceled the purchase.
@unknown default:
    break
}
```

When the customer successfully completes the purchase, StoreKit delivers a new transaction through the [`Product.PurchaseResult`](product/purchaseresult.md), as shown in the code example above. Subsequent monthly renewals deliver a new transaction through the [`updates`](transaction/updates.md) sequence in [`Transaction`](transaction.md).

#### Grant Access Based on Entitlements

Each billing period in a commitment plan produces a new, independent transaction. Granting access to the monthly subscription with a 12-month commitment works the same way as for a standard monthly subscription.

The simplest way to determine entitlements in your app is to check [`currentEntitlements`](transaction/currententitlements.md), which produces a sequence of the latest transactions that entitle a customer to In-App Purchases and subscriptions.

You can also check each transaction ([`Transaction`](transaction.md)) to verify the following:

- The [`expirationDate`](transaction/expirationdate.md) property is in the future for the current billing period.
- The [`revocationDate`](transaction/revocationdate.md) property is absent.
- The [`isUpgraded`](transaction/isupgraded.md) property is `false`.

If these conditions are met, grant the customer access to the subscription for that billing period. These conditions are the same for standard subscriptions, so if your app already handles standard subscriptions, you can use the same logic.

#### Distinguish Between Period and Commitment Expiration

Transactions for commitment plans include two distinct expiration date fields. It’s important to use each field for its intended purpose, as follows:

| Field | Example Value | Purpose |
| --- | --- | --- |
| [`expirationDate`](transaction/expirationdate.md) in [`Transaction`](transaction.md) | June 30, 2026 | End of the current billing period. Use this field, as described above, to check entitlement. |
| [`expirationDate`](transaction/commitmentinfo-swift.struct/expirationdate.md) in [`Transaction.CommitmentInfo`](transaction/commitmentinfo-swift.struct.md) | December 31, 2026 | End of the full 12-month commitment. Use this field to display commitment progress. |

> **Note**: Use [`expirationDate`](transaction/expirationdate.md) in [`Transaction`](transaction.md), not [`expirationDate`](transaction/commitmentinfo-swift.struct/expirationdate.md) in [`Transaction.CommitmentInfo`](transaction/commitmentinfo-swift.struct.md), to help determine whether to grant access for the current period of a monthly subscription with a 12-month commitment.

#### Display Commitment Progress

To show customers the number of months remaining in their commitment, call [`showManageSubscriptions(in:)`](appstore/showmanagesubscriptions(in:).md) or [`showManageSubscriptions(in:subscriptionGroupID:)`](appstore/showmanagesubscriptions(in:subscriptiongroupid:).md) to open the system-provided subscription management page. The system displays the billing progress, next payment date, and commitment renewal date.

To get the same information about the subscription commitment, read the [`commitmentInfo`](transaction/commitmentinfo-swift.property.md) from the latest transaction. The following fields provide the details:

- **[`billingPeriodNumber`](transaction/commitmentinfo-swift.struct/billingperiodnumber.md)**: The current billing period number, for example: 2 of 12.
- **[`totalBillingPeriods`](transaction/commitmentinfo-swift.struct/totalbillingperiods.md)**: The total number of periods in the commitment (12).
- **[`expirationDate`](transaction/commitmentinfo-swift.struct/expirationdate.md)**: The date the full commitment ends.
- **[`price`](transaction/commitmentinfo-swift.struct/price.md)**: The total cost of the full commitment.

> **Note**:  Always use the latest transaction to get an accurate [`expirationDate`](transaction/expirationdate.md) because that date can shift if a billing issue recovers late in the commitment period.

## See Also

- [Implementing a store in your app using the StoreKit API](implementing-a-store-in-your-app-using-the-storekit-api.md)
  Offer In-App Purchases and manage entitlements using signed transactions and status information.
- [Managing the life cycle of monthly subscriptions with a 12-month commitment](managing-lifecycle-of-monthly-subscriptions-with-a-12-month-commitment-.md)
  Handle renewals, cancellations, billing issues, refund requests, and price changes, and test subscriptions with a commitment plan.
- [struct Product](product.md)
  Information about a product that you configure in App Store Connect.
- [Product.SubscriptionInfo](product/subscriptioninfo.md)
  Information about an auto-renewable subscription, such as its status, period, subscription group, and subscription offer details.
- [typealias SubscriptionInfo](subscriptioninfo.md)
  Information about an auto-renewable subscription.
- [typealias SubscriptionStatus](subscriptionstatus.md)
  Represents the renewal status information for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/supporting-monthly-subscriptions-with-a-12-month-commitment)*