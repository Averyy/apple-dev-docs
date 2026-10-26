# recordID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The unique ID of the record.

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
@NSCopying
var recordID: CKRecord.ID { get }
```

```objc
@property (copy, readonly) CKRecordID * recordID;
```

#### Discussion

The system sets the ID of a new record at initialization time. If you use the [`init(recordType:recordID:)`](./init%28recordtype,recordid%29.md) method to initialize the record, the ID derives from the [`CKRecord.ID`](./id.md) object you provide. In all other cases, the record generates a UUID and bases its ID on that value. The ID of a record never changes during its lifetime.

When you save a new record object to the server, the server validates the uniqueness of the record, but returns an error only if the save policy calls for it. Specifically, it returns an error when the save policy is [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](../ckmodifyrecordsoperation/recordsavepolicy/ifserverrecordunchanged.md), which is the default. For all other save policies, the server overwrites the contents of the existing record.

## See Also

### Accessing the Record’s Metadata
- [var recordType: CKRecord.RecordType](./recordtype-6v7au.md)
  The value that your app defines to identify the type of record.
- [CKRecord.SystemType](./systemtype.md)
  Possible values for record types of system records.
- [var creationDate: Date?](./creationdate.md)
  The time when CloudKit first saves the record to the server.
- [var creatorUserRecordID: CKRecord.ID?](./creatoruserrecordid.md)
  The ID of the user who creates the record.
- [var modificationDate: Date?](./modificationdate.md)
  The most recent time that CloudKit saved the record to the server.
- [var lastModifiedUserRecordID: CKRecord.ID?](./lastmodifieduserrecordid.md)
  The ID of the user who most recently modified the record.
- [var recordChangeTag: String?](./recordchangetag.md)
  The server change token for the record.
- [CKRecord.ID](./id.md)
  An object that uniquely identifies a record in a database.
- [recordType](./recordtype-9s09b.md)
  The value that your app defines to identify the type of record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/recordid)*