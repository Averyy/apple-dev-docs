# fetchShareParticipantsCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute when the operation finishes.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use fetchShareParticipantsResultBlock instead

## Declaration

```swift
var fetchShareParticipantsCompletionBlock: (((any Error)?) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^fetchShareParticipantsCompletionBlock)(NSError *operationError);
```

## Discussion

The closure returns no value and takes the following parameter:

- An error that contains information about a problem, or `nil` if CloudKit successfully generates the participants.

The operation executes this closure only once. The closure executes on a background queue, so any tasks that require access to the main queue must dispatch accordingly.

The closure reports an error of type [`CKError.Code.partialFailure`](../ckerror/code/partialfailure.md) when it can’t generate some of the participants. The `userInfo` dictionary of the error contains a [`CKPartialErrorsByItemIDKey`](../ckpartialerrorsbyitemidkey.md) key that has a dictionary as its value. The keys of the dictionary identify the participants that CloudKit can’t generate, and the corresponding values are errors that contain information about the failures.

Set this property’s value before you execute the operation or submit it to a queue.

## See Also

### Processing the Operation’s Results
- [var shareParticipantFetchedBlock: ((CKShare.Participant) -> Void)?](./shareparticipantfetchedblock.md)
  The closure to execute as the operation generates individual participants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/fetchshareparticipantscompletionblock)*