# save(_:completionHandler:)

**Framework**: CloudKit  
**Kind**: method

Saves a specific subscription.

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
func save(_ subscription: CKSubscription) async throws -> CKSubscription
```

#### Discussion

The completion handler takes the following parameters:

- The saved subscription (as it appears on the server), or `nil` if there’s an error.
- An error if a problem occurs, or `nil` if CloudKit successfully saves the subscription.

For information on a more convenient way to save subscriptions, see [`modifySubscriptions(saving:deleting:)`](ckdatabase/modifysubscriptions(saving:deleting:).md).

## Parameters

- `subscription`: The subscription to save.
- `completionHandler`: The closure to execute after CloudKit saves the subscription.

## See Also

- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID]) async throws -> (saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>])](ckdatabase/modifysubscriptions(saving:deleting:).md)
  Modifies the specified subscriptions and returns the results to an awaiting caller.
- [func modifySubscriptions(saving: [CKSubscription], deleting: [CKSubscription.ID], completionHandler: (Result<(saveResults: [CKSubscription.ID : Result<CKSubscription, any Error>], deleteResults: [CKSubscription.ID : Result<Void, any Error>]), any Error>) -> Void)](ckdatabase/modifysubscriptions(saving:deleting:completionhandler:).md)
  Modifies the specified subscriptions and delivers the results to a completion handler.
- [func deleteSubscription(withID: CKSubscription.ID) async throws -> CKSubscription.ID](ckdatabase/deletesubscription(withid:).md)
  Deletes a specific subscription and returns the deleted subscription’s identifier to an awaiting caller.
- [func delete(withSubscriptionID: CKSubscription.ID, completionHandler: (String?, (any Error)?) -> Void)](ckdatabase/delete(withsubscriptionid:completionhandler:).md)
  Deletes a specific subscription and delivers the deleted subscription’s identifier to a completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckdatabase/save(_:completionhandler:)-9pona)*