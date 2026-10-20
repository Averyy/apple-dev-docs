# recordsToSave

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The records to save to the database.

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
var recordsToSave: [CKRecord]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<CKRecord *> * recordsToSave;
```

#### Discussion

The initial value of the property is the array that you provide to the [`init(recordsToSave:recordIDsToDelete:)`](./init%28recordstosave,recordidstodelete%29.md) method. You can modify this array as necessary before you execute the operation. The records must all target the same database, but can belong to different record zones.

If you intend to change the value of this property, do so before you execute the operation or submit the operation to a queue.

## See Also

### Configuring the Modify Record Operation
- [var recordIDsToDelete: [CKRecord.ID]?](./recordidstodelete.md)
  The IDs of the records to delete permanently from the database.
- [var clientChangeTokenData: Data?](./clientchangetokendata.md)
  A token that tracks local changes to records.
- [var isAtomic: Bool](./isatomic.md)
  A Boolean value that indicates whether the entire operation fails when CloudKit can’t update one or more records in a record zone.
- [var savePolicy: CKModifyRecordsOperation.RecordSavePolicy](./savepolicy.md)
  The policy to use when saving changes to records.
- [CKModifyRecordsOperation.RecordSavePolicy](./recordsavepolicy.md)
  Constants that indicate which policy to apply when saving records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/recordstosave)*