# CKQueryNotification.Reason

**Framework**: CloudKit  
**Kind**: enum

Constants that indicate the event that triggers the notification.

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
enum Reason
```

## Topics

### Constants
- [CKQueryNotification.Reason.recordCreated](ckquerynotification/reason/recordcreated.md)
  A notification that indicates the creation of a record matching the subscription’s predicate.
- [CKQueryNotification.Reason.recordUpdated](ckquerynotification/reason/recordupdated.md)
  A notification that indicates the update of a record matching the subscription’s predicate.
- [CKQueryNotification.Reason.recordDeleted](ckquerynotification/reason/recorddeleted.md)
  A notification that indicates the deletion of a record matching the subscription’s predicate.
### Initializers
- [init?(rawValue: Int)](ckquerynotification/reason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var queryNotificationReason: CKQueryNotification.Reason](ckquerynotification/querynotificationreason.md)
  The event that triggers the push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerynotification/reason)*