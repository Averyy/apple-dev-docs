# isEqual(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) isEqual:(id) object;
```

## Return Value

A value of [`true`](../../Swift/true.md) indicates whether they are equal; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `object`: The audio channel layout object to compare.

## See Also

### Getting audio channel layout properties
- [typealias AVAudioChannelCount](../avaudiochannelcount.md)
  The number of audio channels.
- [var channelCount: AVAudioChannelCount](./channelcount.md)
  The number of channels of audio data.
- [var layout: UnsafePointer<AudioChannelLayout>](./layout.md)
  The underlying audio channel layout.
- [var layoutTag: AudioChannelLayoutTag](./layouttag.md)
  The audio channel’s underlying layout tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/isequal(_:))*