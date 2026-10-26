# creationDate

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The time when CloudKit first saves the record to the server.

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
var creationDate: Date? { get }
```

```objc
@property (copy, readonly, nullable) NSDate * creationDate;
```

#### Discussion

The creation date reflects the time when CloudKit creates a record on the server with the current record’s ID. For new instances of this class, the value of this property is initially `nil`. When you save the record to the server, the value updates with the creation date for the record.

## See Also

### Accessing the Record’s Metadata
- [var recordID: CKRecord.ID](./recordid.md)
  The unique ID of the record.
- [var recordType: CKRecord.RecordType](./recordtype-6v7au.md)
  The value that your app defines to identify the type of record.
- [CKRecord.SystemType](./systemtype.md)
  Possible values for record types of system records.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/creationdate)*