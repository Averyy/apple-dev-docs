# CKModifySubscriptionsOperation

**Framework**: CloudKit  
**Kind**: class

An operation for modifying one or more subscriptions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CKModifySubscriptionsOperation
```

#### Overview

After you create or change the configuration of a subscription, use this operation to save those changes to the server. You can also use this operation to permanently delete subscriptions.

If you assign a handler to the [`completionBlock`](https://developer.apple.com/documentation/Foundation/Operation/completionBlock) property, the operation calls it after it executes and passes it the results. Use the handler to perform any housekeeping tasks for the operation. The handler you specify should manage any failures, whether due to an error or an explicit cancellation.

## Topics

### Creating a Modify Subscriptions Operation
- [convenience init(subscriptionsToSave: [CKSubscription]?, subscriptionIDsToDelete: [CKSubscription.ID]?)](ckmodifysubscriptionsoperation/init(subscriptionstosave:subscriptionidstodelete:).md)
  Creates an operation for saving and deleting the specified subscriptions.
- [init()](ckmodifysubscriptionsoperation/init.md)
  Creates an empty modify subscriptions operation.
### Configuring the Modify Subscriptions Operation
- [var subscriptionsToSave: [CKSubscription]?](ckmodifysubscriptionsoperation/subscriptionstosave.md)
  The subscriptions to save to the database.
- [var subscriptionIDsToDelete: [CKSubscription.ID]?](ckmodifysubscriptionsoperation/subscriptionidstodelete-3534e.md)
  The IDs of the subscriptions that you want to delete.
### Processing the Modify Subscription Results
- [var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [CKSubscription.ID]?, (any Error)?) -> Void)?](ckmodifysubscriptionsoperation/modifysubscriptionscompletionblock-7l56.md)
  The closure to execute after the operation modifies the subscriptions.
### Instance Properties
- [var modifySubscriptionsResultBlock: ((Result<Void, any Error>) -> Void)?](ckmodifysubscriptionsoperation/modifysubscriptionsresultblock.md)
- [var perSubscriptionDeleteBlock: ((CKSubscription.ID, Result<Void, any Error>) -> Void)?](ckmodifysubscriptionsoperation/persubscriptiondeleteblock-5ke2l.md)
- [var perSubscriptionSaveBlock: ((CKSubscription.ID, Result<CKSubscription, any Error>) -> Void)?](ckmodifysubscriptionsoperation/persubscriptionsaveblock-8y9zn.md)

## Relationships

### Inherits From
- [CKDatabaseOperation](ckdatabaseoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class CKFetchSubscriptionsOperation](ckfetchsubscriptionsoperation.md)
  An operation for fetching subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation)*