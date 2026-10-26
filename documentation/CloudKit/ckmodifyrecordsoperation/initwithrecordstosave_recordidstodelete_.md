# initWithRecordsToSave:recordIDsToDelete:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates an operation for modifying the specified records.

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
- (instancetype) initWithRecordsToSave:(NSArray<CKRecord *> *) records recordIDsToDelete:(NSArray<CKRecordID *> *) recordIDs;
```

#### Discussion

The records that you intend to save or delete must all reside in the same database, which you specify when you configure the operation. If your app saves a record in a database that doesn’t exist, the server creates the database.

## Parameters

- `records`: The records to save. You can specify `nil` for this parameter.
- `recordIDs`: The IDs of the records to delete. You can specify `nil` for this parameter.

## See Also

### Creating a Modify Record Operation
- [init()](./init%28%29.md)
  Creates an empty modify records operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/initwithrecordstosave:recordidstodelete:)*