# Understanding subscription price increase notice and consent

**Framework**: App Store Connect API  
**Role**: Article

Learn when Apple notifies subscribers of a price increase and asks for their consent, and how to keep existing subscribers on their current price.

## Overview

When a price change raises what an existing subscriber pays, Apple notifies the subscriber and, in some cases, asks them to consent to the new price. Apple sends these messages only to the subscriber who bought the subscription, not to the other people with access to it.

### Update single-seat subscription prices

For a subscription with a single seat, whether Apple asks the subscriber to consent depends on the size of the increase and on the subscriber’s country or region. For the thresholds and the countries and regions that require consent, see [Auto-renewable subscription price increase thresholds](https://developer.apple.com/help/app-store-connect/reference/in-app-purchases-and-subscriptions/auto-renewable-subscription-price-increase-thresholds).

### Preserve the current price

To keep existing subscribers on their current price, set `preserveCurrentPrice` to `true` when you create a price with [`Create a subscription price change`](./post-v1-subscriptionprices.md). When you preserve a price, subscribers don’t receive a price increase notice or consent request, and they keep paying their current price, including their current tier prices for a multiseat subscription.

Preserving a price works only when the price change that would take place if you don’t preserve the price is an increase. To check, preview the change first, as [Preview the effect of a price change](./configuring-subscription-prices-across-territories.md#Preview-the-effect-of-a-price-change) describes.

### Update multiseat subscription prices

For a multiseat subscription, Apple evaluates two prices: the price of the first seat, and the subscriber’s aggregate price, which is the total for all the seats they hold now. Changes that leave the first seat’s price alone, such as new tier prices or seat ranges, never meet the thresholds for notification or consent.

Apple asks the subscriber to consent to the new price if any of the following is true:

- The aggregate price increases, and the first seat’s price increase meets the consent thresholds for single-seat subscriptions.
- The aggregate price increases by more than 50%.
- The subscriber is in a country or region that requires consent for any price increase, and their aggregate price increases.

Otherwise, Apple notifies the subscriber of the increase without asking for consent. A change that doesn’t raise the aggregate price, such as new seat ranges that lower a subscriber’s total, requires neither consent nor an increase notice. Apple instead sends a Subscription Updated notice on the renewal date when the new price takes effect.

If a subscriber doesn’t consent by the renewal date when the new price takes effect, the subscription expires, including all of its seats. If possible, Apple notifies the people with access to the subscription that they no longer have access. If you fill seats anonymously, you’re responsible for notifying those people.

If a subscriber buys more seats while a price increase is pending, the App Store prices the added seats at the new tier prices for their position and charges the subscriber a prorated amount at purchase. When the increase requires consent, the purchase counts as consent to it. Either way, the subscriber pays the new total price starting on the renewal date when the increase takes effect.

To learn more about volume pricing tiers, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md).

## See Also

### Configuring prices and volume pricing
- [Configuring subscription prices across territories](./configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Configuring multiseat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md)
  Control whether organizations can purchase an auto-renewable subscription for multiple people, which markets offer it, and who hosts seat invitations.
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)
  Offer lower per-seat prices to groups and organizations that buy an auto-renewable subscription in larger quantities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/understanding-price-increase-notice-and-consent)*