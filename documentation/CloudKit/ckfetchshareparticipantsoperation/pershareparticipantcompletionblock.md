# perShareParticipantCompletionBlock

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, nullable) void (^)(CKUserIdentityLookupInfo *, CKShareParticipant *, NSError *) perShareParticipantCompletionBlock;
```

#### Discussion

The closure returns no value and takes the following parameters:

- The lookup info of the share participant.
- The generated share participant, or `nil` if CloudKit can’t generate the share participant.
- If CloudKit can’t generate the share participant, this parameter provides information about the failure; otherwise, it’s `nil`.

The operation executes this closure once for each item of user data in the [`userIdentityLookupInfos`](./useridentitylookupinfos.md) property. Each time the closure executes, it executes serially with respect to the other closures of the operation.

If you intend to use this closure to process results, set it before you execute the operation or submit the operation to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation/pershareparticipantcompletionblock)*