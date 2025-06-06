# subscription(for:)

**Framework**: CloudKit  
**Kind**: method

Fetches a specific subscription and returns it to an awaiting caller.

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
func subscription(for subscriptionID: CKSubscription.ID) async throws -> CKSubscription
```

#### Return Value

The fetched subscription.

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.

## Parameters

- `subscriptionID`: The identifier of the subscription to fetch.

## See Also

- [func subscriptions(for: [CKSubscription.ID]) async throws -> [CKSubscription.ID : Result<CKSubscription, any Error>]](ckdatabase/subscriptions(for:).md)
  Fetches the specified subscriptions and returns them to an awaiting caller.
- [func fetch(withSubscriptionIDs: [CKSubscription.ID], completionHandler: (Result<[CKSubscription.ID : Result<CKSubscription, any Error>], any Error>) -> Void)](ckdatabase/fetch(withsubscriptionids:completionhandler:).md)
  Fetches the specified subscriptions and delivers them to a completion handler.
- [func fetch(withSubscriptionID: CKSubscription.ID, completionHandler: (CKSubscription?, (any Error)?) -> Void)](ckdatabase/fetch(withsubscriptionid:completionhandler:).md)
  Fetches a specific subscription and delivers it to a completion handler.
- [func fetchAllSubscriptions(completionHandler: ([CKSubscription]?, (any Error)?) -> Void)](ckdatabase/fetchallsubscriptions(completionhandler:).md)
  Fetches all subscriptions from the current database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/subscription(for:))*