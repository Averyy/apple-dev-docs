# CPPlaybackConfiguration

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPPlaybackConfiguration
```

#### Overview

> **Note**: The preferred presentation of playback may be used to prepare the system for playback of that content.

## Topics

### Initializers
- [init?(coder: NSCoder)](cpplaybackconfiguration/init(coder:).md)
- [init(preferredPresentation: CPPlaybackConfiguration.Presentation, playbackAction: CPPlaybackConfiguration.Action, elapsedTime: CMTime, duration: CMTime)](cpplaybackconfiguration/init(preferredpresentation:playbackaction:elapsedtime:duration:).md)
  Initialize a description of the playable media content that is represented by template items.
### Instance Properties
- [var duration: CMTime](cpplaybackconfiguration/duration.md)
  The total duration of the media content as a CMTime value. Provide 0 if the duration of the content is unknown or unavailable, for example in live-streaming content.
- [var elapsedTime: CMTime](cpplaybackconfiguration/elapsedtime.md)
  The elapsed playback time as a CMTime value.
- [var playbackAction: CPPlaybackConfiguration.Action](cpplaybackconfiguration/playbackaction.md)
  The playback action to perform on this item, such as play, pause, or replay.
- [var preferredPresentation: CPPlaybackConfiguration.Presentation](cpplaybackconfiguration/preferredpresentation.md)
  The style of media presentation shown after selecting the item.
### Enumerations
- [CPPlaybackConfiguration.Action](cpplaybackconfiguration/action.md)
  The playback action to perform on the item.
- [CPPlaybackConfiguration.Presentation](cpplaybackconfiguration/presentation.md)
  The style of media presentation shown after selecting the item.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpplaybackconfiguration)*