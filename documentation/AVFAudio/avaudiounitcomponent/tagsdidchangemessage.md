# AVAudioUnitComponent.TagsDidChangeMessage

**Framework**: AVFAudio  
**Kind**: struct

Type-safe notification message for audio unit component tag changes.

**Availability**:
- macOS 27.0+

## Declaration

```swift
struct TagsDidChangeMessage
```

#### Overview

This notification is posted when the user tags of an audio unit component are modified. The notification object is the `AVAudioUnitComponent` whose tags changed.

> **Note**: User tags are only supported on macOS.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../foundation/notificationcenter/asyncmessage.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var iconURL: URL?](avaudiounitcomponent/iconurl.md)
  The URL of an icon that represents the audio unit component.
- [var icon: UIImage?](avaudiounitcomponent/icon.md)
  An icon that represents the component.
- [var localizedTypeName: String](avaudiounitcomponent/localizedtypename.md)
  The localized type name of the component.
- [var allTagNames: [String]](avaudiounitcomponent/alltagnames.md)
  An array of tag names for the audio unit component.
- [var userTagNames: [String]](avaudiounitcomponent/usertagnames.md)
  An array of tags the user creates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/tagsdidchangemessage)*