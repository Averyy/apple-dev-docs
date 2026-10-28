# initWithRecordType:zoneID:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a record in the specified zone.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```objc
- (instancetype) initWithRecordType:(CKRecordType) recordType zoneID:(CKRecordZoneID *) zoneID;
```

## Return Value

An initialized record object.

## Discussion

Use this method to initialize a new record object in the specified record zone.

Upon creation, the new record contains no data and exists only in memory on the local device. Save the record using a [`CKModifyRecordsOperation`](../ckmodifyrecordsoperation.md) object or by using the [`save(_:completionHandler:)`](../ckdatabase/save%28_,completionhandler%29-3tatz.md) method of [`CKDatabase`](../ckdatabase.md) to transfer the record’s contents to the server.

## Parameters

- `recordType`: A string that represents the type of record that you want to create. You can’t change the record type after initialization. You define the record types that your app supports and use them to distinguish between records with different types of data. This parameter must not be `nil` or contain an empty string.

  A record type must consist of one or more alphanumeric characters and must start with a letter. CloudKit permits the use of underscores, but not spaces.
- `zoneID`: The ID of the record zone where you want to store the record.

## See Also

### Creating a Record
- [- initWithRecordType:](./initwithrecordtype_.md)
  Creates a new record of the specified type.
- [- initWithRecordType:recordID:](./initwithrecordtype_recordid_.md)
  Creates a record using an ID that you provide.
- [CKRecordType](../ckrecordtype.md)
  A data type that CloudKit requires for record types.
- [CKRecordTypeShare](../ckrecordtypeshare-8b6yt.md)
  The system type that identifies a share record.
- [CKRecordTypeUserRecord](../ckrecordtypeuserrecord-49k30.md)
  The system type that identifies a user record.
- [CKRecordFieldKey](../ckrecordfieldkey.md)
  A data type that CloudKit requires for record field names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/initwithrecordtype:zoneid:)*