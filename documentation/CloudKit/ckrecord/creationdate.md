# creationDate

**Framework**: CloudKit  
**Kind**: property

The time when CloudKit first saves the record to the server.

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
var creationDate: Date? { get }
```

#### Discussion

The creation date reflects the time when CloudKit creates a record on the server with the current record’s ID. For new instances of this class, the value of this property is initially `nil`. When you save the record to the server, the value updates with the creation date for the record.

## See Also

- [var recordID: CKRecord.ID](ckrecord/recordid.md)
  The unique ID of the record.
- [var recordType: CKRecord.RecordType](ckrecord/recordtype-6v7au.md)
  The value that your app defines to identify the type of record.
- [CKRecord.SystemType](ckrecord/systemtype.md)
  Possible values for record types of system records.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/creationdate)*