# init(recordsToSave:recordIDsToDelete:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for modifying the specified records.

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
convenience init(recordsToSave: [CKRecord]? = nil, recordIDsToDelete: [CKRecord.ID]? = nil)
```

#### Discussion

The records that you intend to save or delete must all reside in the same database, which you specify when you configure the operation. If your app saves a record in a database that doesn’t exist, the server creates the database.

## Parameters

- `recordsToSave`: The records to save. You can specify   for this parameter.
- `recordIDsToDelete`: The IDs of the records to delete. You can specify   for this parameter.

## See Also

- [init()](ckmodifyrecordsoperation/init.md)
  Creates an empty modify records operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/init(recordstosave:recordidstodelete:))*