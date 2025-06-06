# fetch(withSubscriptionID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Fetches a specific subscription and delivers it to a completion handler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+
- watchOS 6.0+
- Swift 4.2+

## Declaration

```swift
@preconcurrency
func fetch(withSubscriptionID subscriptionID: CKSubscription.ID, completionHandler: @escaping (CKSubscription?, (any Error)?) -> Void)
```

#### Discussion

The completion handler takes the following parameters:

- The requested subscription, or `nil` if CloudKit can’t provide that subscription.
- An error if a problem occurs, or `nil` if the fetch completes successfully.

For information on a more convenient way to fetch specific subscriptions, see [`subscriptions(for:)`](ckdatabase/subscriptions(for:).md).

## Parameters

- `subscriptionID`: The identifier of the subscription to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

- [func subscriptions(for: [CKSubscription.ID]) async throws -> [CKSubscription.ID : Result<CKSubscription, any Error>]](ckdatabase/subscriptions(for:).md)
  Fetches the specified subscriptions and returns them to an awaiting caller.
- [func fetch(withSubscriptionIDs: [CKSubscription.ID], completionHandler: (Result<[CKSubscription.ID : Result<CKSubscription, any Error>], any Error>) -> Void)](ckdatabase/fetch(withsubscriptionids:completionhandler:).md)
  Fetches the specified subscriptions and delivers them to a completion handler.
- [func subscription(for: CKSubscription.ID) async throws -> CKSubscription](ckdatabase/subscription(for:).md)
  Fetches a specific subscription and returns it to an awaiting caller.
- [func fetchAllSubscriptions(completionHandler: ([CKSubscription]?, (any Error)?) -> Void)](ckdatabase/fetchallsubscriptions(completionhandler:).md)
  Fetches all subscriptions from the current database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withsubscriptionid:completionhandler:))*