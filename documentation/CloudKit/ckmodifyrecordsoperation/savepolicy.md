# savePolicy

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The policy to use when saving changes to records.

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
var savePolicy: CKModifyRecordsOperation.RecordSavePolicy { get set }
```

```objc
@property (nonatomic, assign) CKRecordSavePolicy savePolicy;
```

## Discussion

The server uses this property to determine how to proceed when saving record changes. The exact behavior depends on the policy you choose:

- Use [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](./recordsavepolicy/ifserverrecordunchanged.md) to only save a record when the change tag of the local copy matches that of the server’s copy. If the server record’s change tag is more recent, CloudKit discards the save and returns a [`CKError.Code.serverRecordChanged`](../ckerror/code/serverrecordchanged.md) error.
- Use [`CKModifyRecordsOperation.RecordSavePolicy.changedKeys`](./recordsavepolicy/changedkeys.md) to save only the fields of the record that contain changes. The server doesn’t compare record change tags when using this policy.
- Use [`CKModifyRecordsOperation.RecordSavePolicy.allKeys`](./recordsavepolicy/allkeys.md) to save every field of the record, even those without changes. The server doesn’t compare record change tags when using this policy.

If you change the property’s value, do so before you execute the operation or submit the operation to a queue. The default value is [`CKModifyRecordsOperation.RecordSavePolicy.ifServerRecordUnchanged`](./recordsavepolicy/ifserverrecordunchanged.md).

## See Also

### Configuring the Modify Record Operation
- [var recordsToSave: [CKRecord]?](./recordstosave.md)
  The records to save to the database.
- [var recordIDsToDelete: [CKRecord.ID]?](./recordidstodelete.md)
  The IDs of the records to delete permanently from the database.
- [var clientChangeTokenData: Data?](./clientchangetokendata.md)
  A token that tracks local changes to records.
- [var isAtomic: Bool](./isatomic.md)
  A Boolean value that indicates whether the entire operation fails when CloudKit can’t update one or more records in a record zone.
- [CKModifyRecordsOperation.RecordSavePolicy](./recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/savepolicy)*