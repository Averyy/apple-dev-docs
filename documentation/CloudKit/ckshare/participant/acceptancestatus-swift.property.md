# acceptanceStatus

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The current state of the user’s acceptance of the share.

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
var acceptanceStatus: CKShare.ParticipantAcceptanceStatus { get }
```

```objc
@property (assign, readonly) CKShareParticipantAcceptanceStatus acceptanceStatus;
```

## Discussion

This property contains the current state of the participant’s acceptance of the share. For a list of possible values, see [`CKShare.ParticipantAcceptanceStatus`](../participantacceptancestatus.md).

## See Also

### Accessing the Participant’s Status
- [CKShare.Participant.AcceptanceStatus](./acceptancestatus-swift.typealias.md)
  A type that represents the acceptance status of the participant.
- [CKShare.ParticipantAcceptanceStatus](../participantacceptancestatus.md)
  Constants that represent the status of a participant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participant/acceptancestatus-swift.property)*