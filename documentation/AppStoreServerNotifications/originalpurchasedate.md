# originalPurchaseDate

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The purchase date of the transaction associated with the original transaction identifier.

**Availability**:
- App Store Server Notifications 2.0+

## Declaration

```
timestamp originalPurchaseDate
```

#### Discussion

The original purchase date is in UNIX time, in milliseconds.

## See Also

### Purchase dates
- [type purchaseDate](./purchasedate.md)
  The time that the App Store charged the customer’s account for a purchase, a restored product, a subscription, or a subscription renewal after a lapse.
- [type recentSubscriptionStartDate](./recentsubscriptionstartdate.md)
  The earliest start date of a subscription in a series of auto-renewable subscription purchases that ignores all lapses of paid service shorter than 60 days.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/originalpurchasedate)*