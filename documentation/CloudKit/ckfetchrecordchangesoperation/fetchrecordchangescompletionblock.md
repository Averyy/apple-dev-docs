# fetchRecordChangesCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The block to execute when the system finishes processing all changes.

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
var fetchRecordChangesCompletionBlock: ((CKServerChangeToken?, Data?, (any Error)?) -> Void)? { get set }
```

#### Discussion

The block returns no value and takes the following parameters:

When implementing this block, check the [`moreComing`](ckfetchrecordchangesoperation/morecoming.md) property of the operation object to ensure that the server was able to deliver all results. If that property is [`true`](https://developer.apple.com/documentation/Swift/true), you must create another operation object using the value in the `serverChangeToken` parameter to fetch any remaining changes.

The operation object executes this block only once at the conclusion of the operation. It executes after all individual change blocks, but before the operation’s completion block. The block executes serially with respect to the other progress blocks of the operation.

If you intend to use this block to process results, set it before executing the operation or submitting the operation object to a queue.

## See Also

- [var recordChangedBlock: ((CKRecord) -> Void)?](ckfetchrecordchangesoperation/recordchangedblock.md)
  The block to execute with the contents of a changed record.
- [var recordWithIDWasDeletedBlock: ((CKRecord.ID) -> Void)?](ckfetchrecordchangesoperation/recordwithidwasdeletedblock.md)
  The block to execute with the ID of a deleted record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation/fetchrecordchangescompletionblock)*