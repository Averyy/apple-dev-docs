# CKFetchSubscriptionsOperation

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An operation for fetching subscriptions.

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
class CKFetchSubscriptionsOperation
```

```objc
@interface CKFetchSubscriptionsOperation : CKDatabaseOperation
```

#### Overview

A fetch subscriptions operation retrieves subscriptions (with IDs you already know) from iCloud and can fetch all subscriptions for the current user.

You might fetch subscriptions so you can examine or modify their parameters — for example, to adjust the delivery options for push notifications that the subscription generates.

If you assign a handler to the [`completionBlock`](../Foundation/operation/completionblock.md) property, the operation calls it after it executes and passes it the results. Use the handler to perform any housekeeping tasks for the operation. The handler you specify should manage any failures, whether due to an error or an explicit cancellation.

## Topics

### Creating a Fetch Subscriptions Operation
- [convenience init(subscriptionIDs: [CKSubscription.ID])](./ckfetchsubscriptionsoperation/init%28subscriptionids%29.md)
  Creates an operation for fetching the specified subscriptions.
- [init()](./ckfetchsubscriptionsoperation/init%28%29.md)
  Creates an empty fetch subscriptions operation.
- [- initWithSubscriptionIDs:](./ckfetchsubscriptionsoperation/initwithsubscriptionids_.md)
  Creates an operation for fetching the specified subscriptions.
### Getting All Subscriptions
- [class func fetchAllSubscriptionsOperation() -> Self](./ckfetchsubscriptionsoperation/fetchallsubscriptionsoperation%28%29.md)
  Returns an operation that fetches all of the user’s subscriptions.
### Configuring the Fetch Subscriptions Operation
- [var subscriptionIDs: [CKSubscription.ID]?](./ckfetchsubscriptionsoperation/subscriptionids-17f4q.md)
  The IDs of the subscriptions to fetch.
- [subscriptionIDs](./ckfetchsubscriptionsoperation/subscriptionids-714ct.md)
  The IDs of the subscriptions to fetch.
### Processing the Fetch Subscription Results
- [var fetchSubscriptionCompletionBlock: (([CKSubscription.ID : CKSubscription]?, (any Error)?) -> Void)?](./ckfetchsubscriptionsoperation/fetchsubscriptioncompletionblock-6hhpi.md)
  The block to execute with the fetch results.
- [fetchSubscriptionCompletionBlock](./ckfetchsubscriptionsoperation/fetchsubscriptioncompletionblock-207ep.md)
  The block to execute after the operation fetches the subscriptions.
### Instance Properties
- [var fetchSubscriptionsResultBlock: ((Result<Void, any Error>) -> Void)?](./ckfetchsubscriptionsoperation/fetchsubscriptionsresultblock.md)
  The closure to execute after CloudKit retrieves all of the subscriptions.
- [var perSubscriptionResultBlock: ((CKSubscription.ID, Result<CKSubscription, any Error>) -> Void)?](./ckfetchsubscriptionsoperation/persubscriptionresultblock.md)
  The closure to execute when a subscription becomes available.
- [perSubscriptionCompletionBlock](./ckfetchsubscriptionsoperation/persubscriptioncompletionblock.md)
  The closure to execute as the operation fetches individual subscriptions.

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
- [class CKModifySubscriptionsOperation](./ckmodifysubscriptionsoperation.md)
  An operation for modifying one or more subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation)*