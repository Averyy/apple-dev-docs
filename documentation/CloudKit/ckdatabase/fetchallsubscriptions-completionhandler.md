# fetchAllSubscriptions(completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches all subscriptions from the current database.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func allSubscriptions() async throws -> [CKSubscription]
```

#### Discussion

The completion handler takes the following parameters:

- The database’s subscriptions, or `nil` if CloudKit can’t provide the subscriptions.
- An error if a problem occurs, or `nil` if the fetch completes successfully.

For information on a more configurable way to fetch all subscriptions from a specific database, see [`fetchAllSubscriptionsOperation()`](ckfetchsubscriptionsoperation/fetchallsubscriptionsoperation().md).

## Parameters

- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func subscriptions(for: [CKSubscription.ID]) async throws -> [CKSubscription.ID : Result<CKSubscription, any Error>]](ckdatabase/subscriptions(for:).md)
  Fetches the specified subscriptions and returns them to an awaiting caller.
- [func fetch(withSubscriptionIDs: [CKSubscription.ID], completionHandler: (Result<[CKSubscription.ID : Result<CKSubscription, any Error>], any Error>) -> Void)](ckdatabase/fetch(withsubscriptionids:completionhandler:).md)
  Fetches the specified subscriptions and delivers them to a completion handler.
- [func subscription(for: CKSubscription.ID) async throws -> CKSubscription](ckdatabase/subscription(for:).md)
  Fetches a specific subscription and returns it to an awaiting caller.
- [func fetch(withSubscriptionID: CKSubscription.ID, completionHandler: (CKSubscription?, (any Error)?) -> Void)](ckdatabase/fetch(withsubscriptionid:completionhandler:).md)
  Fetches a specific subscription and delivers it to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetchallsubscriptions(completionhandler:))*