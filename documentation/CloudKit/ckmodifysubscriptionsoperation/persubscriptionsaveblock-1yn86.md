# perSubscriptionSaveBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when CloudKit saves a subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) void (^)(NSString *, CKSubscription *, NSError *) perSubscriptionSaveBlock;
```

## Discussion

This property is a closure that returns no value and has the following parameters:

- The ID of the subscription that CloudKit saves.
- The subscription that CloudKit saves, or `nil` if CloudKit can’t save the subscription.
- If CloudKit can’t save the subscription, an error that provides information about the failure; otherwise, `nil`.

The closure executes once for each subscription in the [`subscriptionsToSave`](./subscriptionstosave.md) property. Each time the closure executes, it executes serially with respect to the other subscription completion blocks of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation/persubscriptionsaveblock-1yn86)*