# updateAudioStreamSetting(_:completionHandler:)

**Framework**: HomeKit  
**Kind**: method  
**Role**: Instance Method

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
func updateAudioStreamSetting(_ audioStreamSetting: HMCameraAudioStreamSetting, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func updateAudioStreamSetting(_ audioStreamSetting: HMCameraAudioStreamSetting) async throws
```

```objc
- (void) updateAudioStreamSetting:(HMCameraAudioStreamSetting) audioStreamSetting completionHandler:(void (^)(NSError *error)) completion;
```

## Parameters

- `audioStreamSetting`: The new audio stream configuration.
- `completion`: The block executed after processing the request.

  - **error**: `nil` on success; otherwise, error object indicating the reason for failure.

## See Also

### Configuring the audio stream
- [var audioStreamSetting: HMCameraAudioStreamSetting](./audiostreamsetting.md)
  The stream’s current audio setting.
- [func setAudioStreamSetting(HMCameraAudioStreamSetting)](./setaudiostreamsetting%28_%29.md)
- [enum HMCameraAudioStreamSetting](../hmcameraaudiostreamsetting.md)
  The options associated with a camera’s audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastream/updateaudiostreamsetting(_:completionhandler:))*