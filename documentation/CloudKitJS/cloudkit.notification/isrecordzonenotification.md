# isRecordZoneNotification

**Framework**: CloudKit JS  
**Kind**: property

A Boolean value indicating whether this notification is a push notification that was sent because of changes to a record zone.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute Boolean isRecordZoneNotification;
```

#### Discussion

`true` if this notification is a [`CloudKit.RecordZoneNotification`](cloudkit.recordzonenotification.md) object; otherwise, `false`.

## See Also

- [notificationType](cloudkit.notification/notificationtype.md)
  The type of notification.
- [isQueryNotification](cloudkit.notification/isquerynotification.md)
  A Boolean value indicating whether this push notification is a query notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.notification/isrecordzonenotification)*