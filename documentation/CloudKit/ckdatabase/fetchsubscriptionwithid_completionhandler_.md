# fetchSubscriptionWithID:completionHandler:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Fetches a specific subscription and delivers it to a completion handler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (void) fetchSubscriptionWithID:(CKSubscriptionID) subscriptionID completionHandler:(void (^)(CKSubscription *subscription, NSError *error)) completionHandler;
```

## Discussion

The completion handler takes the following parameters:

- **`subscription`**: The requested subscription, or `nil` if CloudKit can’t provide that subscription.
- **`error`**: An error if a problem occurs, or `nil` if the fetch completes successfully.

For information on a more configurable way to fetch specific subscriptions, see [`CKFetchSubscriptionsOperation`](../ckfetchsubscriptionsoperation.md).

## Parameters

- `subscriptionID`: The identifier of the subscription to fetch.
- `completionHandler`: The block to execute with the fetch results.

## See Also

### Fetching Subscriptions
- [func fetchAllSubscriptions(completionHandler: ([CKSubscription]?, (any Error)?) -> Void)](./fetchallsubscriptions%28completionhandler%29.md)
  Fetches all subscriptions from the current database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/fetchsubscriptionwithid:completionhandler:)*