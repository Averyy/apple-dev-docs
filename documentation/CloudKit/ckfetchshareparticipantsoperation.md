# CKFetchShareParticipantsOperation

**Framework**: CloudKit  
**Kind**: class

An operation that converts user identities into share participants.

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
class CKFetchShareParticipantsOperation
```

#### Overview

Participants are a fundamental part of sharing in CloudKit. A participant provides information about a user and their participation in a share, which includes their identity, acceptance status, role, and permissions. The acceptance status manages the user’s visibilty of the shared records. The role and permissions control what actions the user can perform on those records.

You don’t create participants. Instead, create an instance of [`CKUserIdentity.LookupInfo`](ckuseridentity/lookupinfo-swift.class.md) for each user. Provide the user’s email address or phone number, and then use this operation to convert them into participants that you can add to a share. CloudKit limits the number of participants in a share to 100, and each participant must have an active iCloud account.

> **Note**:  [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) provides a consistent and familiar experience for managing a share’s participants and their permissions. Only use this operation when you want to provide an app-specific approach.

 [`UICloudSharingController`](https://developer.apple.com/documentation/UIKit/UICloudSharingController) provides a consistent and familiar experience for managing a share’s participants and their permissions. Only use this operation when you want to provide an app-specific approach.

CloudKit queries iCloud for corresponding accounts as part of the operation. If it doesn’t find an account, the server updates the participant’s [`userIdentity`](ckshare/participant/useridentity.md) to reflect that by setting the [`hasiCloudAccount`](ckuseridentity/hasicloudaccount.md) property to [`false`](https://developer.apple.com/documentation/swift/false). CloudKit associates a participant with their iCloud account when they accept the share.

Anyone with the URL of a public share can become a participant in that share. For a private share, the owner manages its participants. A participant can’t accept a private share unless the owner adds them first.

To run the operation, add it to the container’s operation queue. The operation executes its callbacks on a private serial queue.

The following example demonstrates how to create the operation, configure it, and then execute it using the default container’s operation queue:

```swift
func fetchParticipants(for lookupInfos: [CKUserIdentity.LookupInfo], 
    completion: @escaping (Result<[CKShare.Participant], Error>) -> Void) {

    var participants = [CKShare.Participant]()
        
    // Create the operation using the lookup objects
    // that the caller provides to the method.
    let operation = CKFetchShareParticipantsOperation(
        userIdentityLookupInfos: lookupInfos)
        
    // Collect the participants as CloudKit generates them.
    operation.shareParticipantFetchedBlock = { participant in
        participants.append(participant)
    }
        
    // If the operation fails, return the error to the caller.
    // Otherwise, return the array of participants.
    operation.fetchShareParticipantsCompletionBlock = { error in
        if let error = error {
            completion(.failure(error))
        } else {
            completion(.success(participants))
        }
    }
        
    // Set an appropriate QoS and add the operation to the
    // container's queue to execute it.
    operation.qualityOfService = .userInitiated
    CKContainer.default().add(operation)
}
```

The operation calls [`shareParticipantFetchedBlock`](ckfetchshareparticipantsoperation/shareparticipantfetchedblock.md) once for each item you provide, and CloudKit returns the participant, or an error if it can’t generate a particpant. CloudKit also batches per-participant errors. If the operation completes with errors, it returns a [`partialFailure`](ckerror/partialfailure.md) error. The error stores the individual errors in its [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary. Use the [`CKPartialErrorsByItemIDKey`](ckpartialerrorsbyitemidkey.md) key to extract them.

## Topics

### Creating an Operation
- [init()](ckfetchshareparticipantsoperation/init.md)
  Creates an empty operation.
- [convenience init(userIdentityLookupInfos: [CKUserIdentity.LookupInfo])](ckfetchshareparticipantsoperation/init(useridentitylookupinfos:).md)
  Creates an operation for generating share participants from the specified user data.
### Configuring the Operation
- [var userIdentityLookupInfos: [CKUserIdentity.LookupInfo]?](ckfetchshareparticipantsoperation/useridentitylookupinfos.md)
  The user data for the participants.
### Processing the Operation’s Results
- [var shareParticipantFetchedBlock: ((CKShare.Participant) -> Void)?](ckfetchshareparticipantsoperation/shareparticipantfetchedblock.md)
  The closure to execute as the operation generates individual participants.
- [var fetchShareParticipantsCompletionBlock: (((any Error)?) -> Void)?](ckfetchshareparticipantsoperation/fetchshareparticipantscompletionblock.md)
  The closure to execute when the operation finishes.
### Instance Properties
- [var fetchShareParticipantsResultBlock: ((Result<Void, any Error>) -> Void)?](ckfetchshareparticipantsoperation/fetchshareparticipantsresultblock.md)
- [var perShareParticipantResultBlock: ((CKUserIdentity.LookupInfo, Result<CKShare.Participant, any Error>) -> Void)?](ckfetchshareparticipantsoperation/pershareparticipantresultblock.md)

## Relationships

### Inherits From
- [CKOperation](ckoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [CKShare.Participant](ckshare/participant.md)
  An object that describes a user’s participation in a share.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchshareparticipantsoperation)*