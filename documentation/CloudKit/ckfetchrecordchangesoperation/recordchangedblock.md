# recordChangedBlock

**Framework**: CloudKit  
**Kind**: property

The block to execute with the contents of a changed record.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var recordChangedBlock: ((CKRecord) -> Void)? { get set }
```

#### Discussion

The block returns no value and takes the following parameters:

The operation object executes this block once for each record in the zone with changes since the previous fetch request. Each time the block executes, it executes serially with respect to the other progress blocks of the operation. If no records change, the block doesn’t execute.

If you intend to use this block to process results, set it before executing the operation or submitting it to a queue.

## See Also

- [var recordWithIDWasDeletedBlock: ((CKRecord.ID) -> Void)?](ckfetchrecordchangesoperation/recordwithidwasdeletedblock.md)
  The block to execute with the ID of a deleted record.
- [var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, Data?, (any Error)?) -> Void)?](ckfetchrecordchangesoperation/fetchrecordchangescompletionblock.md)
  The block to execute when the system finishes processing all changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/recordchangedblock)*