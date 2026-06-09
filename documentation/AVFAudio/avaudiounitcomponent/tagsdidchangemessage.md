# AVAudioUnitComponent.TagsDidChangeMessage

**Framework**: AVFAudio  
**Kind**: struct

Type-safe notification message for audio unit component tag changes.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
struct TagsDidChangeMessage
```

#### Overview

This notification is posted when the user tags of an audio unit component are modified. The notification object is the `AVAudioUnitComponent` whose tags changed.

> **Note**: User tags are only supported on macOS.

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../Foundation/NotificationCenter/AsyncMessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiounitcomponent/tagsdidchangemessage)*