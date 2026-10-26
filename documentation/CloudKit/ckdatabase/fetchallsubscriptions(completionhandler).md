# fetchAllSubscriptions(completionHandler:)

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

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
func fetchAllSubscriptions(completionHandler: @escaping @Sendable ([CKSubscription]?, (any Error)?) -> Void)
```

```objc
- (void) fetchAllSubscriptionsWithCompletionHandler:(void (^)(NSArray<CKSubscription *> *subscriptions, NSError *error)) completionHandler;
```

#### Discussion

The completion handler takes the following parameters:

- The database’s subscriptions, or `nil` if CloudKit can’t provide the subscriptions.
- An error if a problem occurs, or `nil` if the fetch completes successfully.

For information on a more configurable way to fetch all subscriptions from a specific database, see [`fetchAllSubscriptionsOperation()`](../ckfetchsubscriptionsoperation/fetchallsubscriptionsoperation%28%29.md).

## Parameters

- `completionHandler`: The closure to execute with the fetch results.

## See Also

### Fetching Subscriptions
- [func subscriptions(for: [CKSubscription.ID]) async throws -> [CKSubscription.ID : Result<CKSubscription, any Error>]](./subscriptions%28for%29.md)
  Fetches the specified subscriptions and returns them to an awaiting caller.
- [func fetch(withSubscriptionIDs: [CKSubscription.ID], completionHandler: (Result<[CKSubscription.ID : Result<CKSubscription, any Error>], any Error>) -> Void)](./fetch%28withsubscriptionids,completionhandler%29.md)
  Fetches the specified subscriptions and delivers them to a completion handler.
- [func subscription(for: CKSubscription.ID) async throws -> CKSubscription](./subscription%28for%29.md)
  Fetches a specific subscription and returns it to an awaiting caller.
- [func fetch(withSubscriptionID: CKSubscription.ID, completionHandler: (CKSubscription?, (any Error)?) -> Void)](./fetch%28withsubscriptionid,completionhandler%29.md)
  Fetches a specific subscription and delivers it to a completion handler.
- [- fetchSubscriptionWithID:completionHandler:](./fetchsubscriptionwithid_completionhandler_.md)
  Fetches a specific subscription and delivers it to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetchallsubscriptions(completionhandler:))*