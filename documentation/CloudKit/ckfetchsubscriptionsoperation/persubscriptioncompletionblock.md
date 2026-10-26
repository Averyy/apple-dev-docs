# perSubscriptionCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute as the operation fetches individual subscriptions.

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
@property (nonatomic, copy, nullable) void (^)(NSString *, CKSubscription *, NSError *) perSubscriptionCompletionBlock;
```

#### Discussion

The closure returns no value and takes the following parameters:

- The ID of the subscription.
- The subscription, or `nil` if CloudKit can’t fetch the subscription.
- If CloudKit can’t fetch the subscription, this parameter provides information about the failure; otherwise, it’s `nil`.

The operation executes this closure once for each subscription ID in the [`subscriptionIDs`](./subscriptionids-714ct.md) property. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/persubscriptioncompletionblock)*