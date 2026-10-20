# AVCaptureDevice.InputSource

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A distinct input source on a capture device.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class InputSource
```

```objc
@interface AVCaptureDeviceInputSource : NSObject
```

#### Overview

A capture device may optionally present an array of input sources that represent distinct mutually exclusive inputs to the device. For example, an audio capture device might have ADAT optical and analog input sources; a video capture device might have an HDMI or component input source.

## Topics

### Accessing properties
- [var inputSourceID: String](./inputsource/inputsourceid.md)
  An identifier for an input source.
- [var localizedName: String](./inputsource/localizedname.md)
  A localized, human-readable name for the input source.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Configuring input sources
- [var inputSources: [AVCaptureDevice.InputSource]](./inputsources.md)
  An array of input sources that the device supports.
- [var activeInputSource: AVCaptureDevice.InputSource?](./activeinputsource.md)
  The currently active input source of the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/inputsource)*