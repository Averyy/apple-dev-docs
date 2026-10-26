# creatorUserRecordID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The ID of the user who creates the record.

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
var creatorUserRecordID: CKRecord.ID? { get }
```

```objc
@property (copy, readonly, nullable) CKRecordID * creatorUserRecordID;
```

#### Discussion

Use this property’s value to retrieve the user record for the user who creates this record. Every user of the app has a unique user record that is empty by default. Apps can add data to the user record on behalf of the user, but don’t store sensitive data in it.

## See Also

### Accessing the Record’s Metadata
- [var recordID: CKRecord.ID](./recordid.md)
  The unique ID of the record.
- [var recordType: CKRecord.RecordType](./recordtype-6v7au.md)
  The value that your app defines to identify the type of record.
- [CKRecord.SystemType](./systemtype.md)
  Possible values for record types of system records.
- [var creationDate: Date?](./creationdate.md)
  The time when CloudKit first saves the record to the server.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/creatoruserrecordid)*