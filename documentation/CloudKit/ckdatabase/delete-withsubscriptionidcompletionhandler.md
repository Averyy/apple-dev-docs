# delete(withSubscriptionID:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Deletes a specific subscription and delivers the deleted subscription’s identifier to a completion handler.

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
func delete(withSubscriptionID subscriptionID: CKSubscription.ID, completionHandler: @escaping (String?, (any Error)?) -> Void)
```

#### Discussion

The completion handler takes the following parameters:

- The identifier of the deleted subscription, or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully deletes the subscription.

For information on a more convenient way to delete subscriptions, see [`modifySubscriptions(saving:deleting:)`](ckdatabase/modifysubscriptions(saving:deleting:).md).

## Parameters

- `subscriptionID`: The identifier of the subscription to delete.
- `completionHandler`: The closure to execute after CloudKit deletes the subscription.

## See Also

- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID]) async throws -> (saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>])](ckdatabase/modifysubscriptions(saving:deleting:).md)
  Modifies the specified subscriptions and returns the results to an awaiting caller.
- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID], completionHandler: (Result<(saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifysubscriptions(saving:deleting:completionhandler:).md)
  Modifies the specified subscriptions and delivers the results to a completion handler.
- [func save(CKSubscription, completionHandler: (CKSubscription?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-9pona.md)
  Saves a specific subscription.
- [func deleteSubscription(withID: CKSubscription.ID) async throws -> CKSubscription.ID](ckdatabase/deletesubscription(withid:).md)
  Deletes a specific subscription and returns the deleted subscription’s identifier to an awaiting caller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/delete(withsubscriptionid:completionhandler:))*