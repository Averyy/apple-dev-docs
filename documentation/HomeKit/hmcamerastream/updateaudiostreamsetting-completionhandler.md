# updateAudioStreamSetting(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method

Updates an audio stream’s settings.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func updateAudioStreamSetting(_ audioStreamSetting: HMCameraAudioStreamSetting) async throws
```

## Parameters

- `audioStreamSetting`: The new audio stream configuration.
- `completion`: The block executed after processing the request.

## See Also

- [var audioStreamSetting: HMCameraAudioStreamSetting](hmcamerastream/audiostreamsetting.md)
  The stream’s current audio setting.
- [func setAudioStreamSetting(HMCameraAudioStreamSetting)](hmcamerastream/setaudiostreamsetting(_:).md)
- [enum HMCameraAudioStreamSetting](hmcameraaudiostreamsetting.md)
  The options associated with a camera’s audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastream/updateaudiostreamsetting(_:completionhandler:))*