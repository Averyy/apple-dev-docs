# layoutTag

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The audio channel’s underlying layout tag.

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
var layoutTag: AudioChannelLayoutTag { get }
```

```objc
@property (nonatomic, readonly) AudioChannelLayoutTag layoutTag;
```

## See Also

### Related Documentation
- [convenience init?(layoutTag: AudioChannelLayoutTag)](./init%28layouttag%29.md)
  Creates an audio channel layout object from a layout tag.
### Getting audio channel layout properties
- [typealias AVAudioChannelCount](../avaudiochannelcount.md)
  The number of audio channels.
- [var channelCount: AVAudioChannelCount](./channelcount.md)
  The number of channels of audio data.
- [var layout: UnsafePointer<AudioChannelLayout>](./layout.md)
  The underlying audio channel layout.
- [func isEqual(Any) -> Bool](./isequal%28_%29.md)
  Indicates whether another audio channel layout is exactly equal to the current layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiochannellayout/layouttag)*