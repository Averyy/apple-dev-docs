# fetchSubscriptionCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The block to execute after the operation fetches the subscriptions.

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
@property (nonatomic, copy, nullable) void (^fetchSubscriptionCompletionBlock)(NSDictionary<NSString *,CKSubscription *> *subscriptionsBySubscriptionID, NSError *operationError);
```

## Discussion

The block returns no value and takes the following parameters:

- **`subscriptionsBySubscriptionID`**: A dictionary with keys that are the IDs of the subscriptions you request, and values that are the corresponding subscriptions.
- **`operationError`**: An error that contains information about a problem, or `nil` if the system successfully fetches the subscriptions.

The operation executes this block only once, and it’s your only opportunity to process the results. The block executes on a background queue, so any tasks that require access to the main queue must dispatch accordingly.

The block reports an error of type [`CKError.Code.partialFailure`](../ckerror/code/partialfailure.md) when it retrieves only some of the subscriptions successfully. The [`userInfo`](../../Foundation/nserror/userinfo.md) dictionary of the error contains a [`CKPartialErrorsByItemIDKey`](../ckpartialerrorsbyitemidkey.md) key that has a dictionary as its value. The keys of the dictionary are the IDs of the subscriptions that the operation can’t fetch, and the corresponding values are errors that contain information about the failures.

Set this property’s value before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/fetchsubscriptioncompletionblock-207ep)*