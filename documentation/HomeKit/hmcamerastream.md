# HMCameraStream

**Framework**: HomeKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HMCameraStream : HMCameraSource
```

## Topics

### Configuring the audio stream
- [var audioStreamSetting: HMCameraAudioStreamSetting](./hmcamerastream/audiostreamsetting.md)
  The stream’s current audio setting.
- [func updateAudioStreamSetting(HMCameraAudioStreamSetting, completionHandler: ((any Error)?) -> Void)](./hmcamerastream/updateaudiostreamsetting%28_,completionhandler%29.md)
  Updates an audio stream’s settings.
- [func setAudioStreamSetting(HMCameraAudioStreamSetting)](./hmcamerastream/setaudiostreamsetting%28_%29.md)
- [enum HMCameraAudioStreamSetting](./hmcameraaudiostreamsetting.md)
  The options associated with a camera’s audio stream.
### Initializers
- [init()](./hmcamerastream/init%28%29.md)

## Relationships

### Inherits From
- [HMCameraSource](./hmcamerasource.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Controlling the stream
- [func startStream()](./hmcamerastreamcontrol/startstream%28%29.md)
  Starts the camera stream.
- [func stopStream()](./hmcamerastreamcontrol/stopstream%28%29.md)
  Stops the camera stream.
- [var cameraStream: HMCameraStream?](./hmcamerastreamcontrol/camerastream.md)
  The current camera stream.
- [var streamState: HMCameraStreamState](./hmcamerastreamcontrol/streamstate.md)
  The current state of the camera stream.
- [enum HMCameraStreamState](./hmcamerastreamstate.md)
  The states associated with a camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcamerastream)*