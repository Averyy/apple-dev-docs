# audioStreamSetting

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

The stream’s current audio setting.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 14.5+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var audioStreamSetting: HMCameraAudioStreamSetting { get }
```

```objc
@property (nonatomic, assign, readonly) HMCameraAudioStreamSetting audioStreamSetting;
```

## See Also

### Configuring the audio stream
- [func updateAudioStreamSetting(HMCameraAudioStreamSetting, completionHandler: ((any Error)?) -> Void)](./updateaudiostreamsetting%28_,completionhandler%29.md)
  Updates an audio stream’s settings.
- [func setAudioStreamSetting(HMCameraAudioStreamSetting)](./setaudiostreamsetting%28_%29.md)
- [enum HMCameraAudioStreamSetting](../hmcameraaudiostreamsetting.md)
  The options associated with a camera’s audio stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastream/audiostreamsetting)*