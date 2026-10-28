# deleteSubscriptionWithID:completionHandler:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Deletes a specific subscription and delivers the deleted subscription’s identifier to a completion handler.

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
- (void) deleteSubscriptionWithID:(CKSubscriptionID) subscriptionID completionHandler:(void (^)(CKSubscriptionID subscriptionID, NSError *error)) completionHandler;
```

## Discussion

The completion handler takes the following parameters:

- **`subscriptionID`**: The identifier of the deleted subscription, or `nil` if there’s an error.
- **`error`**: An error if a problem occurs, or `nil` if CloudKit successfully deletes the subscription.

For information on a more configurable way to delete subscriptions, see [`CKModifySubscriptionsOperation`](../ckmodifysubscriptionsoperation.md).

## Parameters

- `subscriptionID`: The identifier of the subscription to delete.
- `completionHandler`: The block to execute after CloudKit deletes the subscription.

## See Also

### Modifying Subscriptions
- [func save(CKSubscription, completionHandler: (CKSubscription?, (any Error)?) -> Void)](./save%28_,completionhandler%29-9pona.md)
  Saves a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/deletesubscriptionwithid:completionhandler:)*