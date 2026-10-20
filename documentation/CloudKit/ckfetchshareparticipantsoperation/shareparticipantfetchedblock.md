# shareParticipantFetchedBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The closure to execute as the operation generates individual participants.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- macOS 10.12+ - Deprecated in 12.0
- tvOS 10.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 8.0

> **Deprecated**: Use perShareParticipantCompletionBlock instead, which surfaces per-share-participant errors

## Declaration

```swift
var shareParticipantFetchedBlock: ((CKShare.Participant) -> Void)? { get set }
```

```objc
@property (nonatomic, copy, nullable) void (^shareParticipantFetchedBlock)(CKShareParticipant *participant);
```

#### Discussion

The closure returns no value and takes the following parameters:

- The participant that the operation generates.

The operation executes this closure once for each item of user data in the [`userIdentityLookupInfos`](./useridentitylookupinfos.md) property. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.

## See Also

### Processing the Operation’s Results
- [var fetchShareParticipantsCompletionBlock: (((any Error)?) -> Void)?](./fetchshareparticipantscompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/shareparticipantfetchedblock)*