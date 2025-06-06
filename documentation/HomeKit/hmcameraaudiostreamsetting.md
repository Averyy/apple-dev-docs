# HMCameraAudioStreamSetting

**Framework**: HomeKit  
**Kind**: enum

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

## Topics

### Configuring the Audio Stream
- [HMCameraAudioStreamSetting.muted](hmcameraaudiostreamsetting/muted.md)
  The setting that mutes both incoming and outgoing audio.
- [HMCameraAudioStreamSetting.incomingAudioAllowed](hmcameraaudiostreamsetting/incomingaudioallowed.md)
  The setting that permits incoming audio.
- [HMCameraAudioStreamSetting.bidirectionalAudioAllowed](hmcameraaudiostreamsetting/bidirectionalaudioallowed.md)
  The setting that permits both incoming and outgoing audio.
### Initializers
- [init?(rawValue: UInt)](hmcameraaudiostreamsetting/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var audioStreamSetting: HMCameraAudioStreamSetting](hmcamerastream/audiostreamsetting.md)
  The stream’s current audio setting.
- [func updateAudioStreamSetting(HMCameraAudioStreamSetting, completionHandler: ((any Error)?) -> Void)](hmcamerastream/updateaudiostreamsetting(_:completionhandler:).md)
  Updates an audio stream’s settings.
- [func setAudioStreamSetting(HMCameraAudioStreamSetting)](hmcamerastream/setaudiostreamsetting(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcameraaudiostreamsetting)*