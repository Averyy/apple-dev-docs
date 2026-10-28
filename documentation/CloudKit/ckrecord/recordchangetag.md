# recordChangeTag

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The server change token for the record.

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
var recordChangeTag: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * recordChangeTag;
```

## Discussion

When you fetch a record from the server, you get the current version of that record as it exists on the server. However, at any time after you fetch a record, other users might save a newer version of it to the server. Every time CloudKit saves a record, the server updates the record’s change token to a new value. When you save your copy of the record, the server compares your record’s token with the token on the server. If the two tokens match, the server interprets that you modified the latest version of the record and that it can apply your changes immediately. If the two tokens don’t match, the server checks your app’s save policy to determine how to proceed.

In your own code, you can use change tokens to distinguish between two different versions of the same record.

> **Note**: In some situations, setting a record as the parent of another record can cause the `recordChangeTag` to update on the parent record. This usually occurs when you save the child record.

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
- [var creatorUserRecordID: CKRecord.ID?](./creatoruserrecordid.md)
  The ID of the user who creates the record.
- [var modificationDate: Date?](./modificationdate.md)
  The most recent time that CloudKit saved the record to the server.
- [var lastModifiedUserRecordID: CKRecord.ID?](./lastmodifieduserrecordid.md)
  The ID of the user who most recently modified the record.
- [CKRecord.ID](./id.md)
  An object that uniquely identifies a record in a database.
- [recordType](./recordtype-9s09b.md)
  The value that your app defines to identify the type of record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/recordchangetag)*