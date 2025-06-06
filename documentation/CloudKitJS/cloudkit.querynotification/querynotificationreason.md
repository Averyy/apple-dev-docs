# queryNotificationReason

**Framework**: CloudKit JS  
**Kind**: property

The reason for the query notification.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute String queryNotificationReason;
```

#### Discussion

Possible values are described in [`Reasons for Query Notifications`](reasons-for-query-notifications.md).

## See Also

- [recordName](cloudkit.querynotification/recordname.md)
  The name of the record that was created, deleted, or updated.
- [recordFields](cloudkit.querynotification/recordfields.md)
  A dictionary representation of the fields that changed in the record.
- [isPublicDatabase](cloudkit.querynotification/ispublicdatabase.md)
  Boolean value indicating whether the notification is from the public database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.querynotification/querynotificationreason)*