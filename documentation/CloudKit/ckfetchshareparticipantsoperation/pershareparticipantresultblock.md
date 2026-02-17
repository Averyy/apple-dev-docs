# perShareParticipantResultBlock

**Framework**: CloudKit  
**Kind**: property

The closure to execute as the operation generates individual participants.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var perShareParticipantResultBlock: ((CKUserIdentity.LookupInfo, Result<CKShare.Participant, any Error>) -> Void)? { get set }
```

#### Discussion

This property is a closure that returns no value and has the following parameters:

- The lookup info of the share participant.
- A [`Result`](https://developer.apple.com/documentation/Swift/Result) that contains either a generated share participant, or an error that describes why CloudKit can’t generate the share participant.

The fetch operation executes this closure once for each lookup info in the [`userIdentityLookupInfos`](ckfetchshareparticipantsoperation/useridentitylookupinfos.md) property. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/pershareparticipantresultblock)*