# recordIDsToDelete

**Framework**: CloudKit  
**Kind**: property

The IDs of the records to delete permanently from the database.

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
var recordIDsToDelete: [CKRecord.ID]? { get set }
```

#### Discussion

An array of [`CKRecord.ID`](ckrecord/id.md) objects that identifies the records to delete. The initial value of the property is the array of record IDs that you provide to the [`initWithRecordsToSave:recordIDsToDelete:`](ckmodifyrecordsoperation/initwithrecordstosave:recordidstodelete:.md) method.

When deleting records, the operation reports progress only on the records with the IDs that you specify in this property. Deleting records can trigger the deletion of related records if there is an owner-owned relationship between the records involving a [`CKRecord.Reference`](ckrecord/reference.md) object. When additional deletions occur, CloudKit doesn’t pass them to the progress handler of the operation. For that reason, it’s important to understand the implications of the ownership model you use when you relate records to each other through a [`CKRecord.Reference`](ckrecord/reference.md) object. For more information about owner-owned relationships, see [`CKRecord.Reference`](ckrecord/reference.md).

If you intend to change the value of this property, do so before you execute the operation or submit the operation to a queue.

## See Also

- [var recordsToSave: [CKRecord]?](ckmodifyrecordsoperation/recordstosave.md)
  The records to save to the database.
- [var clientChangeTokenData: Data?](ckmodifyrecordsoperation/clientchangetokendata.md)
  A token that tracks local changes to records.
- [var isAtomic: Bool](ckmodifyrecordsoperation/isatomic.md)
  A Boolean value that indicates whether the entire operation fails when CloudKit can’t update one or more records in a record zone.
- [var savePolicy: CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/savepolicy.md)
  The policy to use when saving changes to records.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordidstodelete)*