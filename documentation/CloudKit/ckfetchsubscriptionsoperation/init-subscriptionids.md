# init(subscriptionIDs:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for fetching the specified subscriptions.

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
convenience init(subscriptionIDs: [CKSubscription.ID])
```

#### Discussion

After creating the operation, assign a closure to the [`fetchSubscriptionCompletionBlock`](ckfetchsubscriptionsoperation/fetchsubscriptioncompletionblock-207ep.md) property to process the results.

## Parameters

- `subscriptionIDs`: An array of strings where each one is an ID of a subscription that you want to retrieve. This parameter sets the   property’s value. If you specify  , you must set the   property before you execute the operation.

## See Also

- [init()](ckfetchsubscriptionsoperation/init.md)
  Creates an empty fetch subscriptions operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/init(subscriptionids:))*