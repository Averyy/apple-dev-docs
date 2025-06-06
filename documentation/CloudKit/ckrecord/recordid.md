# recordID

**Framework**: CloudKit  
**Kind**: property

The unique ID of the record.

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
@NSCopying
var recordID: CKRecord.ID { get }
```

#### Discussion

The system sets the ID of a new record at initialization time. If you use the [`init(recordType:recordID:)`](ckrecord/init(recordtype:recordid:).md) method to initialize the record, the ID derives from the [`CKRecord.ID`](ckrecord/id.md) object you provide. In all other cases, the record generates a UUID and bases its ID on that value. The ID of a record never changes during its lifetime.

When you save a new record object to the server, the server validates the uniqueness of the record, but returns an error only if the save policy calls for it. Specifically, it returns an error when the save policy is [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md), which is the default. For all other save policies, the server overwrites the contents of the existing record.

## See Also

- [var recordType: CKRecord.RecordType](ckrecord/recordtype-6v7au.md)
  The value that your app defines to identify the type of record.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/recordid)*