# isAtomic

**Framework**: CloudKit  
**Kind**: property

A Boolean value that indicates whether the entire operation fails when CloudKit can’t update one or more records in a record zone.

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
var isAtomic: Bool { get set }
```

#### Discussion

Modifying records atomically prevents you from updating your data in a way that would leave it in an inconsistent state. You use atomic updates when you want to write multiple records to the same record zone. If there’s a failure to modify any of the records in a zone, CloudKit doesn’t change the other records in that same zone. The record zone must have the [`atomic`](ckrecordzone/capabilities-swift.struct/atomic.md) capability for this behavior to apply. If a record zone doesn’t support the atomic capability, setting this property has no effect.

The default value of this property is [`true`](https://developer.apple.com/documentation/swift/true), which causes all modifications within a single record zone to occur atomically. If your operation contains records in multiple record zones, a failure in one zone doesn’t prevent modifications to records in a different zone. Changing the value of this property to [`false`](https://developer.apple.com/documentation/swift/false) causes CloudKit to modify records individually, regardless of whether the record zone supports atomic modifications.

## See Also

- [var recordsToSave: [CKRecord]?](ckmodifyrecordsoperation/recordstosave.md)
  The records to save to the database.
- [var recordIDsToDelete: [CKRecord.ID]?](ckmodifyrecordsoperation/recordidstodelete.md)
  The IDs of the records to delete permanently from the database.
- [var clientChangeTokenData: Data?](ckmodifyrecordsoperation/clientchangetokendata.md)
  A token that tracks local changes to records.
- [var savePolicy: CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/savepolicy.md)
  The policy to use when saving changes to records.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/isatomic)*