# CKShare.ParticipantRole.administrator

**Framework**: CloudKit  
**Kind**: case

The participant has the administrator role.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
case administrator
```

#### Discussion

An administrator of a share can add and remove participants and change their permissions.

CloudKit returns shares with `administrator` participants as read-only to devices running OS versions prior to this role being introduced. CloudKit returns administrator participants on such read-only shares as [`CKShare.ParticipantRole.privateUser`](ckshare/participantrole/privateuser.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckshare/participantrole/administrator)*