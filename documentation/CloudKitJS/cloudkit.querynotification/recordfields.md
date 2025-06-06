# recordFields

**Framework**: CloudKit JS  
**Kind**: property

A dictionary representation of the fields that changed in the record.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute Object recordFields;
```

#### Discussion

The keys are the record field names, and the values are the record field values.

## See Also

- [queryNotificationReason](cloudkit.querynotification/querynotificationreason.md)
  The reason for the query notification.
- [recordName](cloudkit.querynotification/recordname.md)
  The name of the record that was created, deleted, or updated.
- [isPublicDatabase](cloudkit.querynotification/ispublicdatabase.md)
  Boolean value indicating whether the notification is from the public database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.querynotification/recordfields)*