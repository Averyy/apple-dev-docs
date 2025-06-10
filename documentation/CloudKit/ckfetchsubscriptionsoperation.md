# CKFetchSubscriptionsOperation

**Framework**: CloudKit  
**Kind**: class

An operation for fetching subscriptions.

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
class CKFetchSubscriptionsOperation
```

#### Overview

A fetch subscriptions operation retrieves subscriptions (with IDs you already know) from iCloud and can fetch all subscriptions for the current user.

You might fetch subscriptions so you can examine or modify their parameters — for example, to adjust the delivery options for push notifications that the subscription generates.

If you assign a handler to the [`completionBlock`](https://developer.apple.com/documentation/Foundation/Operation/completionBlock) property, the operation calls it after it executes and passes it the results. Use the handler to perform any housekeeping tasks for the operation. The handler you specify should manage any failures, whether due to an error or an explicit cancellation.

## Topics

### Creating a Fetch Subscriptions Operation
- [convenience init(subscriptionIDs: [CKSubscription.ID])](ckfetchsubscriptionsoperation/init(subscriptionids:).md)
  Creates an operation for fetching the specified subscriptions.
- [init()](ckfetchsubscriptionsoperation/init.md)
  Creates an empty fetch subscriptions operation.
### Getting All Subscriptions
- [class func fetchAllSubscriptionsOperation() -> Self](ckfetchsubscriptionsoperation/fetchallsubscriptionsoperation.md)
  Returns an operation that fetches all of the user’s subscriptions.
### Configuring the Fetch Subscriptions Operation
- [var subscriptionIDs: [CKSubscription.ID]?](ckfetchsubscriptionsoperation/subscriptionids-17f4q.md)
  The IDs of the subscriptions to fetch.
### Processing the Fetch Subscription Results
- [var fetchSubscriptionCompletionBlock: (([CKSubscription.ID : CKSubscription]?, (any Error)?) -> Void)?](ckfetchsubscriptionsoperation/fetchsubscriptioncompletionblock-6hhpi.md)
  The block to execute with the fetch results.
### Instance Properties
- [var fetchSubscriptionsResultBlock: ((Result<Void, any Error>) -> Void)?](ckfetchsubscriptionsoperation/fetchsubscriptionsresultblock.md)
- [var perSubscriptionResultBlock: ((CKSubscription.ID, Result<CKSubscription, any Error>) -> Void)?](ckfetchsubscriptionsoperation/persubscriptionresultblock.md)

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

- [class CKModifySubscriptionsOperation](ckmodifysubscriptionsoperation.md)
  An operation for modifying one or more subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation)*