# participantRole

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The share’s participant role for the user who retrieves the metadata.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var participantRole: CKShare.ParticipantRole { get }
```

```objc
@property (assign, readonly) CKShareParticipantRole participantRole;
```

## See Also

### Accessing the Participant’s Capabilities
- [var participantPermission: CKShare.ParticipantPermission](./participantpermission.md)
  The share’s permissions for the user who retrieves the metadata.
- [var participantStatus: CKShare.ParticipantAcceptanceStatus](./participantstatus.md)
  The share’s participation status for the user who retrieves the metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/metadata/participantrole)*