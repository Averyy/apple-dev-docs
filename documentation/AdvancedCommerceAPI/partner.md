# Partner

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The identifier and name of a mini app partner associated with a purchase.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object Partner
```

## Mentions

- [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md)

## Overview

Use the `Partner` object only if your app participates in the [Mini Apps Partner Program](https://developer.apple.com/programs/mini-apps-partner/). If it does, include a `Partner` object in the `partners` array of an item to identify the mini app partner for that purchase. If your app doesn’t participate in the program, don’t include the `partners` property in your requests.

For more information, see [Creating SKUs for the Mini Apps Partner Program](./creating-skus-for-the-mini-app-partner-program.md).

## Properties

- `id` (string) *(required)*: The unique identifier you set for the mini app partner.
- `name` (string) *(required)*: The name of the mini app partner.

## See Also

### Objects
- [object Descriptors](./descriptors.md)
  The display name and description of a subscription product.
- [object Offer](./offer.md)
  A discount offer for an auto-renewable subscription.
- [object OfferV1](./offerv1.md)
- [object RequestInfo](./requestinfo.md)
  The metadata to include in server requests.
- [object SeatPriceTier](./seatpricetier.md)
  A volume price tier for a subscription item that a customer buys as a multiseat purchase.
- [object SubscriptionModifyAddItem](./subscriptionmodifyadditem.md)
  The data your app provides to add items when it makes changes to an auto-renewable subscription.
- [object SubscriptionModifyChangeItem](./subscriptionmodifychangeitem.md)
  The data your app provides to change an item of an auto-renewable subscription.
- [object SubscriptionModifyDescriptors](./subscriptionmodifydescriptors.md)
  The data your app provides to change the description and display name of an auto-renewable subscription.
- [object SubscriptionModifyPeriodChange](./subscriptionmodifyperiodchange.md)
  The data your app provides to change the period of an auto-renewable subscription.
- [object SubscriptionModifyRemoveItem](./subscriptionmodifyremoveitem.md)
  The data your app provides to remove an item from an auto-renewable subscription.
- [object SubscriptionPriceChangeItem](./subscriptionpricechangeitem.md)
  The data your app provides to change a subscription price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/partner)*