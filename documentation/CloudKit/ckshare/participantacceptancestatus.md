# CKShare.ParticipantAcceptanceStatus

**Framework**: CloudKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the status of a participant.

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
enum ParticipantAcceptanceStatus
```

```c
enum CKShareParticipantAcceptanceStatus : NSInteger;
```

## Topics

### Constants
- [CKShare.ParticipantAcceptanceStatus.unknown](./participantacceptancestatus/unknown.md)
  The participant’s status is unknown.
- [CKShare.ParticipantAcceptanceStatus.pending](./participantacceptancestatus/pending.md)
  The participant’s acceptance of the share request is pending.
- [CKShare.ParticipantAcceptanceStatus.accepted](./participantacceptancestatus/accepted.md)
  The participant accepted the share request.
- [CKShare.ParticipantAcceptanceStatus.removed](./participantacceptancestatus/removed.md)
  The system removed the participant from the share.
### Initializers
- [init?(rawValue: Int)](./participantacceptancestatus/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the Participant’s Status
- [var acceptanceStatus: CKShare.ParticipantAcceptanceStatus](./participant/acceptancestatus-swift.property.md)
  The current state of the user’s acceptance of the share.
- [CKShare.Participant.AcceptanceStatus](./participant/acceptancestatus-swift.typealias.md)
  A type that represents the acceptance status of the participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participantacceptancestatus)*