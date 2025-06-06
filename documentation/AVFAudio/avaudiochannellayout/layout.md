# layout

**Framework**: AVFAudio  
**Kind**: property

The underlying audio channel layout.

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
var layout: UnsafePointer<AudioChannelLayout> { get }
```

## See Also

- [init(layout: UnsafePointer<AudioChannelLayout>)](avaudiochannellayout/init(layout:).md)
  Creates an audio channel layout object from an existing one.
- [typealias AVAudioChannelCount](avaudiochannelcount.md)
  The number of audio channels.
- [var channelCount: AVAudioChannelCount](avaudiochannellayout/channelcount.md)
  The number of channels of audio data.
- [var layoutTag: AudioChannelLayoutTag](avaudiochannellayout/layouttag.md)
  The audio channel’s underlying layout tag.
- [func isEqual(Any) -> Bool](avaudiochannellayout/isequal(_:).md)
  Indicates whether another audio channel layout is exactly equal to the current layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/layout)*