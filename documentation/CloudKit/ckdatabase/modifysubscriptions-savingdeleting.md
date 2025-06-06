# modifySubscriptions(saving:deleting:)

**Framework**: CloudKit  
**Kind**: method

Modifies the specified subscriptions and returns the results to an awaiting caller.

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
func modifySubscriptions(saving subscriptionsToSave: [CKSubscription], deleting subscriptionIDsToDelete: [CKSubscription.ID]) async throws -> (saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>])
```

#### Return Value

A tuple with the following named elements:

#### Discussion

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account; otherwise, the returned tuple includes any individual subscription errors.

For information on a more configurable way to modify subscriptions, see [`CKModifySubscriptionsOperation`](ckmodifysubscriptionsoperation.md).

## Parameters

- `subscriptionsToSave`: The subscriptions to save.
- `subscriptionIDsToDelete`: The identifiers of the subscriptions to permanently delete.

## See Also

- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID], completionHandler: (Result<(saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifysubscriptions(saving:deleting:completionhandler:).md)
  Modifies the specified subscriptions and delivers the results to a completion handler.
- [func save(CKSubscription, completionHandler: (CKSubscription?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-9pona.md)
  Saves a specific subscription.
- [func deleteSubscription(withID: CKSubscription.ID) async throws -> CKSubscription.ID](ckdatabase/deletesubscription(withid:).md)
  Deletes a specific subscription and returns the deleted subscription’s identifier to an awaiting caller.
- [func delete(withSubscriptionID: CKSubscription.ID, completionHandler: (String?, (any Error)?) -> Void)](ckdatabase/delete(withsubscriptionid:completionhandler:).md)
  Deletes a specific subscription and delivers the deleted subscription’s identifier to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/modifysubscriptions(saving:deleting:))*