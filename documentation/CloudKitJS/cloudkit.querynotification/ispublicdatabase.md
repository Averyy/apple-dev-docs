# isPublicDatabase

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

Boolean value indicating whether the notification is from the public database.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute Boolean isPublicDatabase;
```

#### Discussion

`true` if the notification is from the public database; otherwise, `false`.

## See Also

### Getting Record Changes
- [queryNotificationReason](./querynotificationreason.md)
  The reason for the query notification.
- [recordName](./recordname.md)
  The name of the record that was created, deleted, or updated.
- [recordFields](./recordfields.md)
  A dictionary representation of the fields that changed in the record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.querynotification/ispublicdatabase)*