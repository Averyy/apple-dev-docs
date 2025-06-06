# queryCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute after CloudKit retrieves all of the records.

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
var queryCompletionBlock: ((CKQueryOperation.Cursor?, (any Error)?) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- A cursor that indicates there are more results to fetch, or `nil` if there are no additional results. Use the cursor to create a new query operation when you’re ready to retrieve the next batch of results.
- An error that contains information about a problem, or `nil` if CloudKit retrieves the results successfully.

This closure executes only once, and represents your final opportunity to process the results. It executes after all of the individual record fetch closures. The closure executes serially with respect to the other closures of the operation.

If the number of records that the operation intends to return exceeds [`resultsLimit`](ckqueryoperation/resultslimit.md), the operation provides a cursor that you can use to retrieve the next batch of results. You must create a separate operation using the cursor to fetch the next batch of results.

Update the value of this property before you execute the operation or submit it to a queue.

## See Also

- [var recordFetchedBlock: ((CKRecord) -> Void)?](ckqueryoperation/recordfetchedblock.md)
  The closure to execute when a record becomes available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/querycompletionblock)*