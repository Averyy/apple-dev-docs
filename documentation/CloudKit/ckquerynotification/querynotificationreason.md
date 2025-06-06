# queryNotificationReason

**Framework**: CloudKit  
**Kind**: property

The event that triggers the push notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var queryNotificationReason: CKQueryNotification.Reason { get }
```

#### Discussion

Subscription notifications result from the creation, deletion, or updating of a single record. The record in question must match the subscription’s predicate for an event to trigger.

## See Also

- [CKQueryNotification.Reason](ckquerynotification/reason.md)
  Constants that indicate the event that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerynotification/querynotificationreason)*