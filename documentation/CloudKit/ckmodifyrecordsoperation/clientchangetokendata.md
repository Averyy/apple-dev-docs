# clientChangeTokenData

**Framework**: CloudKit  
**Kind**: property

A token that tracks local changes to records.

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
var clientChangeTokenData: Data? { get set }
```

#### Discussion

The default value is `nil`.

When you modify records from a fetch operation, specify a token using this property to indicate which version of the record you most recently modified. Compare the token you supply to the token in the next record fetch to confirm the server  successfully receives the device’s most recent modify request.

If you intend to change the value of this property, do so before you execute the operation or submit the operation to a queue.

## See Also

- [var recordsToSave: [CKRecord]?](ckmodifyrecordsoperation/recordstosave.md)
  The records to save to the database.
- [var recordIDsToDelete: [CKRecord.ID]?](ckmodifyrecordsoperation/recordidstodelete.md)
  The IDs of the records to delete permanently from the database.
- [var isAtomic: Bool](ckmodifyrecordsoperation/isatomic.md)
  A Boolean value that indicates whether the entire operation fails when CloudKit can’t update one or more records in a record zone.
- [var savePolicy: CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/savepolicy.md)
  The policy to use when saving changes to records.
- [CKModifyRecordsOperation.RecordSavePolicy](ckmodifyrecordsoperation/recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/clientchangetokendata)*