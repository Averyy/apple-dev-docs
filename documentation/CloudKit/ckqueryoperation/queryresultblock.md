# queryResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute after CloudKit retrieves all of the records.

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
var queryResultBlock: ((Result<CKQueryOperation.Cursor?, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either: - A successful `Result`, or
- An error that contains information about a problem encountered retrieving the results.

This closure executes only once, and represents your final opportunity to process the results. It executes after all of the individual record match closures. The closure executes serially with respect to the other closures of the operation.

If the number of records that the operation intends to return exceeds [`resultsLimit`](ckqueryoperation/resultslimit.md), the successful result provides a cursor that you can use to retrieve the next batch of results. You must create a separate operation using the cursor to fetch the next batch of results.

Update the value of this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/queryresultblock)*