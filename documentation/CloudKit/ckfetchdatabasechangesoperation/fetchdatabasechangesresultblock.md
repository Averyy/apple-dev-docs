# fetchDatabaseChangesResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute when the operation finishes.

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
var fetchDatabaseChangesResultBlock: ((Result<(serverChangeToken: CKServerChangeToken, moreComing: Bool), any Error>) -> Void)? { get set }
```

#### Discussion

The closure has no return value and takes the following parameter:

- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either: - A successful `Result` of - The change token to store and use in subsequent instances of [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md).
- A Boolean that indicates whether this is the final database change. If [`fetchAllChanges`](ckfetchdatabasechangesoperation/fetchallchanges.md) is [`false`](https://developer.apple.com/documentation/Swift/false), it’s the app’s responsibility to create additional instances of [`CKFetchDatabaseChangesOperation`](ckfetchdatabasechangesoperation.md) to fetch further changes.
- An error that contains information about a problem encountered retrieving the database changes.

This closure executes only once, and represents your final opportunity to process the results. The closure executes serially with respect to the other closures of the operation.

Set this property before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchdatabasechangesoperation/fetchdatabasechangesresultblock)*