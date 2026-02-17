# recordMatchedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when a record match is available.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var recordMatchedBlock: ((CKRecord.ID, Result<CKRecord, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- The ID of the record.
- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either a retrieved record, or an error that describes why CloudKit can’t retrieve the record.

After identifying and sorting the records, the query operation executes this closure once for each of the result’s records. The closure executes serially with respect to all other closures of the operation, so you can expect only one closure at a time to execute for this operation.

Set the property’s value before you execute the operation or submit it to a queue.

> ⚠️ **Warning**: Query indexes update asynchronously so they aren’t always current. If you query for records that you recently changed and don’t allow enough time for those changes to process, the query’s results may be incorrect. The results may not contain the correct records, and the records may be out of order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/recordmatchedblock-2qze7)*