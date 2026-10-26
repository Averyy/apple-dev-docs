# CKModifySubscriptionsOperation

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An operation for modifying one or more subscriptions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class CKModifySubscriptionsOperation
```

```objc
@interface CKModifySubscriptionsOperation : CKDatabaseOperation
```

#### Overview

After you create or change the configuration of a subscription, use this operation to save those changes to the server. You can also use this operation to permanently delete subscriptions.

If you assign a handler to the [`completionBlock`](../Foundation/operation/completionblock.md) property, the operation calls it after it executes and passes it the results. Use the handler to perform any housekeeping tasks for the operation. The handler you specify should manage any failures, whether due to an error or an explicit cancellation.

## Topics

### Creating a Modify Subscriptions Operation
- [convenience init(subscriptionsToSave: [CKSubscription]?, subscriptionIDsToDelete: [CKSubscription.ID]?)](./ckmodifysubscriptionsoperation/init%28subscriptionstosave,subscriptionidstodelete%29.md)
  Creates an operation for saving and deleting the specified subscriptions.
- [init()](./ckmodifysubscriptionsoperation/init%28%29.md)
  Creates an empty modify subscriptions operation.
- [- initWithSubscriptionsToSave:subscriptionIDsToDelete:](./ckmodifysubscriptionsoperation/initwithsubscriptionstosave_subscriptionidstodelete_.md)
  Creates an operation for saving and deleting the specified subscriptions.
### Configuring the Modify Subscriptions Operation
- [var subscriptionsToSave: [CKSubscription]?](./ckmodifysubscriptionsoperation/subscriptionstosave.md)
  The subscriptions to save to the database.
- [var subscriptionIDsToDelete: [CKSubscription.ID]?](./ckmodifysubscriptionsoperation/subscriptionidstodelete-3534e.md)
  The IDs of the subscriptions that you want to delete.
- [subscriptionIDsToDelete](./ckmodifysubscriptionsoperation/subscriptionidstodelete-14x82.md)
  The IDs of the subscriptions that you want to delete.
### Processing the Modify Subscription Results
- [var modifySubscriptionsCompletionBlock: (([CKSubscription]?, [CKSubscription.ID]?, (any Error)?) -> Void)?](./ckmodifysubscriptionsoperation/modifysubscriptionscompletionblock-7l56.md)
  The closure to execute after the operation modifies the subscriptions.
- [modifySubscriptionsCompletionBlock](./ckmodifysubscriptionsoperation/modifysubscriptionscompletionblock-3v0cp.md)
  The block to execute after the operation modifies the subscriptions.
### Instance Properties
- [var modifySubscriptionsResultBlock: ((Result<Void, any Error>) -> Void)?](./ckmodifysubscriptionsoperation/modifysubscriptionsresultblock.md)
  The closure to execute after CloudKit modifies all of the subscriptions.
- [var perSubscriptionDeleteBlock: ((CKSubscription.ID, Result<Void, any Error>) -> Void)?](./ckmodifysubscriptionsoperation/persubscriptiondeleteblock-5ke2l.md)
  The closure to execute when CloudKit deletes a subscription.
- [var perSubscriptionSaveBlock: ((CKSubscription.ID, Result<CKSubscription, any Error>) -> Void)?](./ckmodifysubscriptionsoperation/persubscriptionsaveblock-8y9zn.md)
  The closure to execute when CloudKit saves a subscription.
- [perSubscriptionDeleteBlock](./ckmodifysubscriptionsoperation/persubscriptiondeleteblock-55p5p.md)
  The closure to execute when CloudKit deletes a subscription.
- [perSubscriptionSaveBlock](./ckmodifysubscriptionsoperation/persubscriptionsaveblock-1yn86.md)
  The closure to execute when CloudKit saves a subscription.

## Relationships

### Inherits From
- [CKDatabaseOperation](./ckdatabaseoperation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Subscription Management
- [class CKFetchSubscriptionsOperation](./ckfetchsubscriptionsoperation.md)
  An operation for fetching subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation)*