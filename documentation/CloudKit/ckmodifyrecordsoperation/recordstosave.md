# recordsToSave

**Framework**: CloudKit  
**Kind**: property

The records to save to the database.

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
var recordsToSave: [CKRecord]? { get set }
```

#### Discussion

The initial value of the property is the array that you provide to the [`initWithRecordsToSave:recordIDsToDelete:`](ckmodifyrecordsoperation/initwithrecordstosave:recordidstodelete:.md) method. You can modify this array as necessary before you execute the operation. The records must all target the same database, but can belong to different record zones.

If you intend to change the value of this property, do so before you execute the operation or submit the operation to a queue.

## See Also

- [var recordIDsToDelete: [CKRecord.ID]?](ckmodifyrecordsoperation/recordidstodelete.md)
  The IDs of the records to delete permanently from the database.
- [var clientChangeTokenData: Data?](ckmodifyrecordsoperation/clientchangetokendata.md)
  A token that tracks local changes to records.
- [var isAtomic: Bool](ckmodifyrecordsoperation/isatomic.md)
  A Boolean value that indicates whether the entire operation fails when CloudKit can’t update one or more records in a record zone.
- [var savePolicy: CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/savepolicy.md)
  The policy to use when saving changes to records.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordstosave)*