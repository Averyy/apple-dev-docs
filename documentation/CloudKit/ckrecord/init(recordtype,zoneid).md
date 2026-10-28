# init(recordType:zoneID:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a record in the specified zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS
- watchOS 3.0+
- Swift 4.2+ - Deprecated in 4.2

> **Deprecated**: Use [`init(recordType:recordID:)`](./init%28recordtype,recordid%29.md) instead.

## Declaration

```swift
convenience init(recordType: CKRecord.RecordType, zoneID: CKRecordZone.ID)
```

## Discussion

Use this method to initialize a new record object with the specified ID. The newly created record contains no data.

Upon creation, record objects exist only in memory on the local device. Save the record using a [`CKModifyRecordsOperation`](../ckmodifyrecordsoperation.md) object or by using the [`save(_:completionHandler:)`](../ckdatabase/save%28_,completionhandler%29-3tatz.md) method to transfer the record’s contents to the server.

## Parameters

- `recordType`: A string that represents the type of record that you want to create. You can’t change the record type after initialization. You define the record types that your app supports and use them to distinguish between records with different types of data. This parameter must not be `nil` or contain an empty string.

  A record type must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.
- `zoneID`: The ID of the record zone where you want to store the record.

## See Also

### Creating a Record
- [convenience init(recordType: CKRecord.RecordType, recordID: CKRecord.ID)](./init%28recordtype,recordid%29.md)
  Creates a record using an ID that you provide.
- [typealias RecordType](./recordtype-swift.typealias.md)
  The data type that CloudKit requires for record types.
- [typealias FieldKey](./fieldkey.md)
  The data type that CloudKit requires for record field names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/init(recordtype:zoneid:))*