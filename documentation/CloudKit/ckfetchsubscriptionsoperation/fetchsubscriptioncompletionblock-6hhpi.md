# fetchSubscriptionCompletionBlock

**Framework**: CloudKit  
**Kind**: property

The block to execute with the fetch results.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS ?+ - Deprecated
- watchOS 6.0+
- Swift 4.2+

## Declaration

```swift
var fetchSubscriptionCompletionBlock: (([CKSubscription.ID : CKSubscription]?, (any Error)?) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- A dictionary with keys that are the IDs of the subscriptions you request, and values that are the corresponding subscriptions.
- An error that contains information about a problem, or `nil` if the system successfully fetches the subscriptions.

The operation executes this closure only once, and it’s your only opportunity to process the results. The closure must be capable of executing on a background queue, so any tasks that require access to the main queue must redirect accordingly.

The closure reports an error of type [`CKError.Code.partialFailure`](ckerror/code/partialfailure.md) when it retrieves only some of the subscriptions successfully. The [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary of the error contains a [`CKPartialErrorsByItemIDKey`](ckpartialerrorsbyitemidkey.md) key that has a dictionary as its value. The keys of the dictionary are the IDs of the subscriptions that the operation can’t fetch, and the corresponding values are errors that contain information about the failures.

Set this property’s value before you execute the operation or submit it to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation/fetchsubscriptioncompletionblock-6hhpi)*