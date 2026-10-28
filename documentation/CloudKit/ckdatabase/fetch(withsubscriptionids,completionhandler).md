# fetch(withSubscriptionIDs:completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches the specified subscriptions and delivers them to a completion handler.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
@preconcurrency
func fetch(withSubscriptionIDs subscriptionIDs: [CKSubscription.ID], completionHandler: @escaping @Sendable (Result<[CKSubscription.ID : Result<CKSubscription, any Error>], any Error>) -> Void)
```

## Discussion

The completion handler takes the following parameters:

- A [`Result`](../../Swift/result.md) that contains either a dictionary of fetched subscriptions, or an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account. When present, the dictionary uses the identifiers you specify in `subscriptionIDs` as its keys. The value of each key is a [`Result`](../../Swift/result.md) that contains either the corresponding fetched subscription, or an error that describes why CloudKit can’t provide that subscription.

For information on a more configurable way to fetch specific subscriptions, see [`CKFetchSubscriptionsOperation`](../ckfetchsubscriptionsoperation.md).

## Parameters

- `subscriptionIDs`: The identifiers of the subscriptions to fetch.
- `completionHandler`: The closure to execute with the fetch results.

## See Also

### Fetching Subscriptions
- [func subscriptions(for: [CKSubscription.ID]) async throws -> [CKSubscription.ID : Result<CKSubscription, any Error>]](./subscriptions%28for%29.md)
  Fetches the specified subscriptions and returns them to an awaiting caller.
- [func subscription(for: CKSubscription.ID) async throws -> CKSubscription](./subscription%28for%29.md)
  Fetches a specific subscription and returns it to an awaiting caller.
- [func fetch(withSubscriptionID: CKSubscription.ID, completionHandler: (CKSubscription?, (any Error)?) -> Void)](./fetch%28withsubscriptionid,completionhandler%29.md)
  Fetches a specific subscription and delivers it to a completion handler.
- [func fetchAllSubscriptions(completionHandler: ([CKSubscription]?, (any Error)?) -> Void)](./fetchallsubscriptions%28completionhandler%29.md)
  Fetches all subscriptions from the current database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetch(withsubscriptionids:completionhandler:))*