# fetchRecordsResultBlock

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
var fetchRecordsResultBlock: ((Result<Void, any Error>) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameter:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either: - A successful `Result`, or
- An error that contains information about a problem encountered retrieving the records.

The fetch operation executes this closure only once. The closure executes after all of the individual progress closures, but before the operation’s completion closure. The closure executes serially with respect to the other progress closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation/fetchrecordsresultblock)*