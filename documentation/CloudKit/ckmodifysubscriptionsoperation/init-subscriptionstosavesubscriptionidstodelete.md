# init(subscriptionsToSave:subscriptionIDsToDelete:)

**Framework**: CloudKit  
**Kind**: init

Creates an operation for saving and deleting the specified subscriptions.

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
convenience init(subscriptionsToSave: [CKSubscription]? = nil, subscriptionIDsToDelete: [CKSubscription.ID]? = nil)
```

#### Discussion

The subscriptions that you want to save or delete must reside in the same container. CloudKit creates a subscription if you save one that doesn’t already exist. CloudKit returns an error if you try to delete a subscription that doesn’t exist.

## Parameters

- `subscriptionsToSave`: The subscriptions to save or update. You can specify   for this parameter.
- `subscriptionIDsToDelete`: The IDs of the subscriptions to delete. You can specify   for this parameter.

## See Also

- [init()](ckmodifysubscriptionsoperation/init.md)
  Creates an empty modify subscriptions operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/init(subscriptionstosave:subscriptionidstodelete:))*