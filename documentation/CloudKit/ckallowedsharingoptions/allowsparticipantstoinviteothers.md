# allowsParticipantsToInviteOthers

**Framework**: CloudKit  
**Kind**: property

Defaults to `NO`. If set, the system sharing UI will allow the user to choose whether added participants can invite others to the share. Shares with `.administrator` participants will be returned as read-only to devices running OS versions prior to the `.administrator` role being introduced. The `.administrator` participants on these read-only shares will be returned as `.privateUser`.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var allowsParticipantsToInviteOthers: Bool { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckallowedsharingoptions/allowsparticipantstoinviteothers)*