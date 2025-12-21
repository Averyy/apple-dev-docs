# AVCaptureDevice.InputSource

**Framework**: AVFoundation  
**Kind**: class

A distinct input source on a capture device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class InputSource
```

#### Overview

A capture device may optionally present an array of input sources that represent distinct mutually exclusive inputs to the device. For example, an audio capture device might have ADAT optical and analog input sources; a video capture device might have an HDMI or component input source.

## Topics

### Accessing properties
- [var inputSourceID: String](avcapturedevice/inputsource/inputsourceid.md)
  An identifier for an input source.
- [var localizedName: String](avcapturedevice/inputsource/localizedname.md)
  A localized, human-readable name for the input source.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var inputSources: [AVCaptureDevice.InputSource]](avcapturedevice/inputsources.md)
  An array of input sources that the device supports.
- [var activeInputSource: AVCaptureDevice.InputSource?](avcapturedevice/activeinputsource.md)
  The currently active input source of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsource)*