# HMCameraStream

**Framework**: HomeKit  
**Kind**: class

An object that represents a camera’s audiovisual stream.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMCameraStream
```

## Topics

### Configuring the audio stream
- [var audioStreamSetting: HMCameraAudioStreamSetting](hmcamerastream/audiostreamsetting.md)
  The stream’s current audio setting.
- [func updateAudioStreamSetting(HMCameraAudioStreamSetting, completionHandler: ((any Error)?) -> Void)](hmcamerastream/updateaudiostreamsetting(_:completionhandler:).md)
  Updates an audio stream’s settings.
- [func setAudioStreamSetting(HMCameraAudioStreamSetting)](hmcamerastream/setaudiostreamsetting(_:).md)
- [enum HMCameraAudioStreamSetting](hmcameraaudiostreamsetting.md)
  The options associated with a camera’s audio stream.
### Initializers
- [init()](hmcamerastream/init.md)

## Relationships

### Inherits From
- [HMCameraSource](hmcamerasource.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func startStream()](hmcamerastreamcontrol/startstream.md)
  Starts the camera stream.
- [func stopStream()](hmcamerastreamcontrol/stopstream.md)
  Stops the camera stream.
- [var cameraStream: HMCameraStream?](hmcamerastreamcontrol/camerastream.md)
  The current camera stream.
- [var streamState: HMCameraStreamState](hmcamerastreamcontrol/streamstate.md)
  The current state of the camera stream.
- [enum HMCameraStreamState](hmcamerastreamstate.md)
  The states associated with a camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastream)*