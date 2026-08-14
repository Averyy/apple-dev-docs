# modifyRecordsResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute after CloudKit modifies all of the records.

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
var modifyRecordsResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameter:

- A [`Result`](https://developer.apple.com/documentation/swift/result) that contains either: - A successful `Result`, or
- An error that contains information about a problem encountered modifying the records.

The closure executes only once, and represents your final opportunity to process the operation’s results. It executes after all record progress closures and record completion closures finish. The closure executes serially with respect to the other closures of the operation.

Although this closure executes after the modification of records completes, it executes prior to the indexing of queries for those modified records. Therefore, if a query executes in this completion closure, the results of that query might not include the changes from this operation. Conversely, records that CloudKit fetches in the completion closure are up to date with the changes from the associated operation.

Update the value of this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation/modifyrecordsresultblock)*