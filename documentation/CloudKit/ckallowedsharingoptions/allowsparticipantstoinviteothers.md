# allowsParticipantsToInviteOthers

**Framework**: CloudKit  
**Kind**: property

Default value is NO. If set, the system sharing UI allows the user to choose whether added participants can invite others to the share. CloudKit returns shares with [`CKShare.ParticipantRole.administrator`](ckshare/participantrole/administrator.md) participants as read-only to devices running OS versions prior to this role being introduced. CloudKit returns administrator participants on such read-only shares as [`CKShare.ParticipantRole.privateUser`](ckshare/participantrole/privateuser.md).

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