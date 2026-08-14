# isEqual(_:)

**Framework**: AVFAudio  
**Kind**: method

Indicates whether another audio channel layout is exactly equal to the current layout.

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
func isEqual(_ object: Any) -> Bool
```

#### Return Value

A value of [`true`](https://developer.apple.com/documentation/swift/true) indicates whether they are equal; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `object`: The audio channel layout object to compare.

## See Also

- [typealias AVAudioChannelCount](avaudiochannelcount.md)
  The number of audio channels.
- [var channelCount: AVAudioChannelCount](avaudiochannellayout/channelcount.md)
  The number of channels of audio data.
- [var layout: UnsafePointer<AudioChannelLayout>](avaudiochannellayout/layout.md)
  The underlying audio channel layout.
- [var layoutTag: AudioChannelLayoutTag](avaudiochannellayout/layouttag.md)
  The audio channel’s underlying layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/isequal(_:))*