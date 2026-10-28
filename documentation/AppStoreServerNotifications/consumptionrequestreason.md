# consumptionRequestReason

**Framework**: App Store Server Notifications  
**Kind**: typealias  
**Role**: Type

The customer-provided reason for a refund request.

**Availability**:
- App Store Server Notifications 2.11+

## Declaration

```
string consumptionRequestReason
```

## Possible Values

- `UNINTENDED_PURCHASE`: The customer didn’t intend to make the in-app purchase.
- `FULFILLMENT_ISSUE`: The customer had issues with receiving or using the  in-app purchase.
- `UNSATISFIED_WITH_PURCHASE`: The customer wasn’t satisfied with the in-app purchase.
- `LEGAL`: The customer requested a refund based on a legal reason.
- `OTHER`: The customer requested a refund for other reasons.

## Mentions

- [App Store Server Notifications changelog](./app-store-server-notifications-changelog.md)

## Discussion

When a customer initiates a refund request for a consumable in-app purchase or auto-renewable subscription, the App Store sends a `CONSUMPTION_REQUEST` [`notificationType`](./notificationtype.md) to your server. The notification includes the `consumptionRequestReason` in the [`data`](./data.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/consumptionrequestreason)*