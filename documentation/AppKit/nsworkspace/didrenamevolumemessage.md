# NSWorkspace.DidRenameVolumeMessage

**Framework**: AppKit  
**Kind**: struct

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
struct DidRenameVolumeMessage
```

## Topics

### Initializers
- [init(localizedVolumeName: String, volumeURL: URL, oldLocalizedVolumeName: String, oldVolumeURL: URL)](nsworkspace/didrenamevolumemessage/init(localizedvolumename:volumeurl:oldlocalizedvolumename:oldvolumeurl:).md)
### Instance Properties
- [var localizedVolumeName: String](nsworkspace/didrenamevolumemessage/localizedvolumename.md)
- [var oldLocalizedVolumeName: String](nsworkspace/didrenamevolumemessage/oldlocalizedvolumename.md)
- [var oldVolumeURL: URL](nsworkspace/didrenamevolumemessage/oldvolumeurl.md)
- [var volumeURL: URL](nsworkspace/didrenamevolumemessage/volumeurl.md)
### Type Methods
- [static func makeNotification(NSWorkspace.DidRenameVolumeMessage) -> Notification](nsworkspace/didrenamevolumemessage/makenotification(_:).md)

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../Foundation/NotificationCenter/MainActorMessage.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/didrenamevolumemessage)*