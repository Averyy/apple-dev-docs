# CKRecord.SystemType

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Possible values for record types of system records.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS
- watchOS 3.0+
- Swift 4.2+

## Declaration

```swift
enum SystemType
```

## Topics

### Types of System Records
- [static let share: CKRecord.RecordType](./systemtype/share.md)
  A string that represents the record type for CloudKit share records.
- [static let userRecord: CKRecord.RecordType](./systemtype/userrecord.md)
  A string that represents the record type for CloudKit user records.

## See Also

### Accessing the Record’s Metadata
- [var recordID: CKRecord.ID](./recordid.md)
  The unique ID of the record.
- [var recordType: CKRecord.RecordType](./recordtype-6v7au.md)
  The value that your app defines to identify the type of record.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/systemtype)*