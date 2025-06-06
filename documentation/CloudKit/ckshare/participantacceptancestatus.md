# CKShare.ParticipantAcceptanceStatus

**Framework**: CloudKit  
**Kind**: enum

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

## Topics

### Constants
- [CKShare.ParticipantAcceptanceStatus.unknown](ckshare/participantacceptancestatus/unknown.md)
  The participant’s status is unknown.
- [CKShare.ParticipantAcceptanceStatus.pending](ckshare/participantacceptancestatus/pending.md)
  The participant’s acceptance of the share request is pending.
- [CKShare.ParticipantAcceptanceStatus.accepted](ckshare/participantacceptancestatus/accepted.md)
  The participant accepted the share request.
- [CKShare.ParticipantAcceptanceStatus.removed](ckshare/participantacceptancestatus/removed.md)
  The system removed the participant from the share.
### Initializers
- [init?(rawValue: Int)](ckshare/participantacceptancestatus/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var acceptanceStatus: CKShare.ParticipantAcceptanceStatus](ckshare/participant/acceptancestatus-swift.property.md)
  The current state of the user’s acceptance of the share.
- [CKShare.Participant.AcceptanceStatus](ckshare/participant/acceptancestatus-swift.typealias.md)
  A type that represents the acceptance status of the participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participantacceptancestatus)*