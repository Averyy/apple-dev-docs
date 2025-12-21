# allowsParticipantsToInviteOthers

**Framework**: CloudKit  
**Kind**: property

Default value is `NO`. If set, the system sharing UI will allow the user to choose whether added participants can invite others to the share. Shares with [`CKShare.ParticipantRole.administrator`](ckshare/participantrole/administrator.md) participants will be returned as read-only to devices running OS versions prior to this role being introduced. Administrator participants on these read-only shares will be returned as [`CKShare.ParticipantRole.privateUser`](ckshare/participantrole/privateuser.md).

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var allowsParticipantsToInviteOthers: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckallowedsharingoptions/allowsparticipantstoinviteothers)*