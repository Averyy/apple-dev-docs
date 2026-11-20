# OfferV1

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.0+

## Declaration

```
object OfferV1
```

## Properties

- `period` (string) *(required)*: **Allowed Values**: `P3D`, `P1W`, `P2W`, `P1M`, `P2M`, `P3M`, `P6M`, `P9M`, `P1Y`
- `periodCount` (int32) *(required)*: **Minimum**: `1`; **Maximum**: `12`
- `price` (price) *(required)*
- `reason` (string) *(required)*: **Allowed Values**: `ACQUISITION`, `WIN_BACK`, `RETENTION`

## See Also

### Objects
- [object Descriptors](./descriptors.md)
  The display name and description of a subscription product.
- [object Offer](./offer.md)
  A discount offer for an auto-renewable subscription.
- [object Partner](./partner.md)
  The identifier and name of a mini app partner associated with a purchase.
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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/offerv1)*