# shareParticipantFetchedBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute as the operation generates individual participants.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var shareParticipantFetchedBlock: ((CKShare.Participant) -> Void)? { get set }
```

#### Discussion

The closure returns no value and takes the following parameters:

- The participant that the operation generates.

The operation executes this closure once for each item of user data in the [`userIdentityLookupInfos`](ckfetchshareparticipantsoperation/useridentitylookupinfos.md) property. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.

## See Also

- [var fetchShareParticipantsCompletionBlock: (((any Error)?) -> Void)?](ckfetchshareparticipantsoperation/fetchshareparticipantscompletionblock.md)
  The closure to execute when the operation finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/shareparticipantfetchedblock)*