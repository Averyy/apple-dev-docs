# init(recordType:zoneID:)

**Framework**: CloudKit  
**Kind**: init

Creates a record in the specified zone.

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
convenience init(recordType: CKRecord.RecordType, zoneID: CKRecordZone.ID)
```

#### Discussion

Use this method to initialize a new record object with the specified ID. The newly created record contains no data.

Upon creation, record objects exist only in memory on the local device. Save the record using a [`CKModifyRecordsOperation`](ckmodifyrecordsoperation.md) object or by using the [`save(_:completionHandler:)`](ckdatabase/save(_:completionhandler:)-3tatz.md) method to transfer the record’s contents to the server.

## Parameters

- `recordType`: A record type must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.
- `zoneID`: The ID of the record zone where you want to store the record.

## See Also

- [convenience init(recordType: CKRecord.RecordType, recordID: CKRecord.ID)](ckrecord/init(recordtype:recordid:).md)
  Creates a record using an ID that you provide.
- [typealias RecordType](ckrecord/recordtype-swift.typealias.md)
  The data type that CloudKit requires for record types.
- [typealias FieldKey](ckrecord/fieldkey.md)
  The data type that CloudKit requires for record field names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/init(recordtype:zoneid:))*