# AVAudioChannelLayout

**Framework**: AVFAudio  
**Kind**: class

An object that describes the roles of a set of audio channels.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioChannelLayout
```

#### Overview

The `AVAudioChannelLayout` class is a thin wrapper for Core Audio’s [`AudioChannelLayout`](https://developer.apple.com/documentation/CoreAudioTypes/AudioChannelLayout).

## Topics

### Creating an Audio Channel Layout
- [init(layout: UnsafePointer<AudioChannelLayout>)](avaudiochannellayout/init(layout:).md)
  Creates an audio channel layout object from an existing one.
- [convenience init?(layoutTag: AudioChannelLayoutTag)](avaudiochannellayout/init(layouttag:).md)
  Creates an audio channel layout object from a layout tag.
### Getting Audio Channel Layout Properties
- [typealias AVAudioChannelCount](avaudiochannelcount.md)
  The number of audio channels.
- [var channelCount: AVAudioChannelCount](avaudiochannellayout/channelcount.md)
  The number of channels of audio data.
- [var layout: UnsafePointer<AudioChannelLayout>](avaudiochannellayout/layout.md)
  The underlying audio channel layout.
- [var layoutTag: AudioChannelLayoutTag](avaudiochannellayout/layouttag.md)
  The audio channel’s underlying layout tag.
- [func isEqual(Any) -> Bool](avaudiochannellayout/isequal(_:).md)
  Indicates whether another audio channel layout is exactly equal to the current layout.

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVAudioFormat](avaudioformat.md)
  An object that describes the representation of an audio format.
- [let AVChannelLayoutKey: String](avchannellayoutkey.md)
- [Linear PCM Format Settings](linear-pcm-format-settings.md)
  The audio settings that apply to linear PCM audio formats.
- [Format Settings](format-settings.md)
  The audio settings that apply to all audio formats that the audio player and recorder classes support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout)*