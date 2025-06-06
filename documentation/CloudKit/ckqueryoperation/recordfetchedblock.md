# recordFetchedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when a record becomes available.

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
var recordFetchedBlock: ((CKRecord) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- A single record that matches the search criteria.

After identifying and sorting the records, the query operation executes this closure once for each of the result’s records. The closure executes serially with respect to all other closures of the operation, so you can expect only one closure at a time to execute for this operation.

Set the property’s value before you execute the operation or submit it to a queue.

> ⚠️ **Warning**:  Query indexes update asynchronously so they aren’t always current. If you query for records that you recently changed and don’t allow enough time for those changes to process, the query’s results may be incorrect. The results may not contain the correct records, and the records may be out of order.

 Query indexes update asynchronously so they aren’t always current. If you query for records that you recently changed and don’t allow enough time for those changes to process, the query’s results may be incorrect. The results may not contain the correct records, and the records may be out of order.

## See Also

- [var queryCompletionBlock: ((CKQueryOperation.Cursor?, (any Error)?) -> Void)?](ckqueryoperation/querycompletionblock.md)
  The closure to execute after CloudKit retrieves all of the records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/recordfetchedblock)*