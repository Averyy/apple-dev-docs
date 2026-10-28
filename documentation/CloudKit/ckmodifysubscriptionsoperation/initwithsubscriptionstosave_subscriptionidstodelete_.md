# initWithSubscriptionsToSave:subscriptionIDsToDelete:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates an operation for saving and deleting the specified subscriptions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```objc
- (instancetype) initWithSubscriptionsToSave:(NSArray<CKSubscription *> *) subscriptionsToSave subscriptionIDsToDelete:(NSArray<NSString *> *) subscriptionIDsToDelete;
```

## Discussion

The subscriptions that you want to save or delete must reside in the same container. CloudKit creates a subscription if you save one that doesn’t already exist. CloudKit returns an error if you try to delete a subscription that doesn’t exist.

## Parameters

- `subscriptionsToSave`: The subscriptions to save or update. You can specify `nil` for this parameter.
- `subscriptionIDsToDelete`: The IDs of the subscriptions to delete. You can specify `nil` for this parameter.

## See Also

### Creating a Modify Subscriptions Operation
- [init()](./init%28%29.md)
  Creates an empty modify subscriptions operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/initwithsubscriptionstosave:subscriptionidstodelete:)*