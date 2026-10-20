# setAudioStreamSetting(_:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 10.0+ - Deprecated in 10.0
- iPadOS 10.0+ - Deprecated in 10.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

> **Deprecated**: Use [`updateAudioStreamSetting(_:completionHandler:)`](./updateaudiostreamsetting%28_,completionhandler%29.md) instead.

## Declaration

```swift
func setAudioStreamSetting(_ audioStreamSetting: HMCameraAudioStreamSetting)
```

```objc
- (void) setAudioStreamSetting:(HMCameraAudioStreamSetting) audioStreamSetting;
```

## Parameters

- `audioStreamSetting`: The new audio stream configuration.

## See Also

### Configuring the audio stream
- [var audioStreamSetting: HMCameraAudioStreamSetting](./audiostreamsetting.md)
  The stream’s current audio setting.
- [func updateAudioStreamSetting(HMCameraAudioStreamSetting, completionHandler: ((any Error)?) -> Void)](./updateaudiostreamsetting%28_,completionhandler%29.md)
  Updates an audio stream’s settings.
- [enum HMCameraAudioStreamSetting](../hmcameraaudiostreamsetting.md)
  The options associated with a camera’s audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastream/setaudiostreamsetting(_:))*