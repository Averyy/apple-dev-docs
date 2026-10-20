# HMCameraAudioStreamSetting

**Framework**: HomeKit  
**Kind**: enum  
**Role**: Enumeration

The options associated with a camera’s audio stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum HMCameraAudioStreamSetting
```

```c
enum HMCameraAudioStreamSetting : NSUInteger;
```

## Topics

### Configuring the Audio Stream
- [HMCameraAudioStreamSetting.muted](./hmcameraaudiostreamsetting/muted.md)
  The setting that mutes both incoming and outgoing audio.
- [HMCameraAudioStreamSetting.incomingAudioAllowed](./hmcameraaudiostreamsetting/incomingaudioallowed.md)
  The setting that permits incoming audio.
- [HMCameraAudioStreamSetting.bidirectionalAudioAllowed](./hmcameraaudiostreamsetting/bidirectionalaudioallowed.md)
  The setting that permits both incoming and outgoing audio.
### Initializers
- [init?(rawValue: UInt)](./hmcameraaudiostreamsetting/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring the audio stream
- [var audioStreamSetting: HMCameraAudioStreamSetting](./hmcamerastream/audiostreamsetting.md)
  The stream’s current audio setting.
- [func updateAudioStreamSetting(HMCameraAudioStreamSetting, completionHandler: ((any Error)?) -> Void)](./hmcamerastream/updateaudiostreamsetting%28_,completionhandler%29.md)
  Updates an audio stream’s settings.
- [func setAudioStreamSetting(HMCameraAudioStreamSetting)](./hmcamerastream/setaudiostreamsetting%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting)*