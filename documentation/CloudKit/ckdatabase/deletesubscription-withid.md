# deleteSubscription(withID:)

**Framework**: CloudKit  
**Kind**: method

Deletes a specific subscription and returns the deleted subscription’s identifier to an awaiting caller.

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
@discardableResult
func deleteSubscription(withID subscriptionID: CKSubscription.ID) async throws -> CKSubscription.ID
```

#### Return Value

The identifier of the deleted subscription.

#### Discussion

This method throws an error if the request fails, such as when the network is unavailable or the device doesn’t have an active iCloud account.

For information on a more convenient way to delete subscriptions, see [`modifySubscriptions(saving:deleting:)`](ckdatabase/modifysubscriptions(saving:deleting:).md).

## Parameters

- `subscriptionID`: The identifier of the subscription to delete.

## See Also

- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID]) async throws -> (saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>])](ckdatabase/modifysubscriptions(saving:deleting:).md)
  Modifies the specified subscriptions and returns the results to an awaiting caller.
- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID], completionHandler: (Result<(saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifysubscriptions(saving:deleting:completionhandler:).md)
  Modifies the specified subscriptions and delivers the results to a completion handler.
- [func save(CKSubscription, completionHandler: (CKSubscription?, (any Error)?) -> Void)](ckdatabase/save(_:completionhandler:)-9pona.md)
  Saves a specific subscription.
- [func delete(withSubscriptionID: CKSubscription.ID, completionHandler: (String?, (any Error)?) -> Void)](ckdatabase/delete(withsubscriptionid:completionhandler:).md)
  Deletes a specific subscription and delivers the deleted subscription’s identifier to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/deletesubscription(withid:))*