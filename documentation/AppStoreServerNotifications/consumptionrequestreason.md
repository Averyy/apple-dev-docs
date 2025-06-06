# consumptionRequestReason

**Framework**: App Store Server Notifications  
**Kind**: typealias

The customer-provided reason for a refund request.

**Availability**:
- App Store Server Notifications 2.11+

## Declaration

```swift
string consumptionRequestReason
```

## Mentions

- [App Store Server Notifications changelog](app-store-server-notifications-changelog.md)

#### Discussion

When a customer initiates a refund request for a consumable in-app purchase or auto-renewable subscription, the App Store sends a `CONSUMPTION_REQUEST` [`notificationType`](notificationtype.md) to your server. The notification includes the `consumptionRequestReason` in the [`data`](data.md) object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/consumptionrequestreason)*