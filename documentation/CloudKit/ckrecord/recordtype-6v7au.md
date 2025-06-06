# recordType

**Framework**: CloudKit  
**Kind**: property

The value that your app defines to identify the type of record.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
var recordType: CKRecord.RecordType { get }
```

#### Discussion

Use this value to differentiate between different record types in your app. The value is primarily for your benefit, so choose record types that represent the data in the corresponding records.

CloudKit provides two system-defined record types:

| Record Type | Description |
| --- | --- |
| [`CKRecordTypeUserRecord`](ckrecordtypeuserrecord-49k30.md) | Identifies records that represent users. |
| [`CKRecordTypeShare`](ckrecordtypeshare-8b6yt.md) | Identifies records that the user shares. |

## See Also

- [var recordID: CKRecord.ID](ckrecord/recordid.md)
  The unique ID of the record.
- [CKRecord.SystemType](ckrecord/systemtype.md)
  Possible values for record types of system records.
- [var creationDate: Date?](ckrecord/creationdate.md)
  The time when CloudKit first saves the record to the server.
- [var creatorUserRecordID: CKRecord.ID?](ckrecord/creatoruserrecordid.md)
  The ID of the user who creates the record.
- [var modificationDate: Date?](ckrecord/modificationdate.md)
  The most recent time that CloudKit saved the record to the server.
- [var lastModifiedUserRecordID: CKRecord.ID?](ckrecord/lastmodifieduserrecordid.md)
  The ID of the user who most recently modified the record.
- [var recordChangeTag: String?](ckrecord/recordchangetag.md)
  The server change token for the record.
- [CKRecord.ID](ckrecord/id.md)
  An object that uniquely identifies a record in a database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/recordtype-6v7au)*