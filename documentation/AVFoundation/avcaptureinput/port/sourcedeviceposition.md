# sourceDevicePosition

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The position of the source device providing input through this port.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var sourceDevicePosition: AVCaptureDevice.Position { get }
```

```objc
@property (nonatomic, readonly) AVCaptureDevicePosition sourceDevicePosition;
```

## Discussion

All ports contained in an [`AVCaptureInput`](../../avcaptureinput.md) object’s [`ports`](../ports.md) array have the same [`sourceDevicePosition`](./sourcedeviceposition.md) value.

When working with a microphone input in an [`AVCaptureMultiCamSession`](../../avcapturemulticamsession.md), it’s possible to record multiple microphone directions simultaneously. For example, you can record audio from the front microphone input to pair with video from the front camera, and record audio from the back microphone input to pair with video from the back camera.

By calling the input’s [`ports(for:sourceDeviceType:sourceDevicePosition:)`](../../avcapturedeviceinput/ports%28for,sourcedevicetype,sourcedeviceposition%29.md) method, you may discover additional hidden ports originating from the source audio device. These ports represent individual microphones positioned to pick up audio from one particular direction.

```swift
// Find the audio port that captures omnidirectional audio.
let omniAudioPort = audioDeviceInput.ports(for: .audio,
                                           sourceDeviceType: .builtInMicrophone,
                                           sourceDevicePosition: .unspecified).first

// Find the audio port that captures front audio.
let frontAudioPort = audioDeviceInput.ports(for: .audio,
                                            sourceDeviceType: .builtInMicrophone,
                                            sourceDevicePosition: .front).first

// Find the audio port that captures back audio.
let backAudioPort = audioDeviceInput.ports(for: .audio,
                                           sourceDeviceType: .builtInMicrophone,
                                           sourceDevicePosition: .back).first
```

## See Also

### Inspecting an input port
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the port is in an enabled state.
- [var mediaType: AVMediaType](./mediatype.md)
  The media type of the port.
- [var formatDescription: CMFormatDescription?](./formatdescription.md)
  A description of the port format.
- [var sourceDeviceType: AVCaptureDevice.DeviceType?](./sourcedevicetype.md)
  The device type of the source camera that provides data to the port.
- [var clock: CMClock?](./clock.md)
  An object that represents the capture device’s clock.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/sourcedeviceposition)*