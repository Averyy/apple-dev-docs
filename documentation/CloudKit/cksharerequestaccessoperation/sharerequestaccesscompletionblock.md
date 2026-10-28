# shareRequestAccessCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute after CloudKit processes all share access requests.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) void (^)(NSError *) shareRequestAccessCompletionBlock;
```

## Discussion

This property is a closure that returns no value and has the following parameter:

- An error that contains information about a problem, or `nil` if the system successfully processes the share access requests.

The closure executes only once, and represents your final opportunity to process the operation’s results. It executes after all share access request completion closures finish. The closure executes serially with respect to the other closures of the operation.

The closure reports an error of type [`CKError.Code.partialFailure`](../ckerror/code/partialfailure.md) when it processes only some of the share access requests successfully. The [`userInfo`](../../Foundation/nserror/userinfo.md) dictionary of the error contains a [`CKPartialErrorsByItemIDKey`](../ckpartialerrorsbyitemidkey.md) key that has a dictionary as its value. The keys of the dictionary are the URLs of the shares whose access requests can’t be processed by the operation. The corresponding values are errors that contain information about the failures.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksharerequestaccessoperation/sharerequestaccesscompletionblock)*