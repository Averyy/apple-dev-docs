# CKQueryNotification.Reason

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate the event that triggers the notification.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum Reason
```

```c
enum CKQueryNotificationReason : NSInteger;
```

## Topics

### Constants
- [CKQueryNotification.Reason.recordCreated](./reason/recordcreated.md)
  A notification that indicates the creation of a record matching the subscription’s predicate.
- [CKQueryNotification.Reason.recordUpdated](./reason/recordupdated.md)
  A notification that indicates the update of a record matching the subscription’s predicate.
- [CKQueryNotification.Reason.recordDeleted](./reason/recorddeleted.md)
  A notification that indicates the deletion of a record matching the subscription’s predicate.
### Initializers
- [init?(rawValue: Int)](./reason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Notification Attributes
- [var queryNotificationReason: CKQueryNotification.Reason](./querynotificationreason.md)
  The event that triggers the push notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerynotification/reason)*