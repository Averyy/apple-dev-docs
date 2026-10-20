# AVCaptureEventSound

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A sound object for a capture event.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
class AVCaptureEventSound
```

```objc
@interface AVCaptureEventSound : NSObject
```

#### Overview

> ❗ **Important**: To use AirPods Camera Control, it must be available in your country or region. AirPods Camera Control is not currently available in the European Union.

## Topics

### Creating a sound
- [init(url: URL) throws](./avcaptureeventsound/init%28url%29-2a6o4.md)
  Creates a sound object for a capture event.
### Accessing default sounds
- [class var cameraShutter: AVCaptureEventSound](./avcaptureeventsound/camerashutter.md)
  The default sound for photo capture.
- [class var beginVideoRecording: AVCaptureEventSound](./avcaptureeventsound/beginvideorecording.md)
  The default sound for starting a video recording.
- [class var endVideoRecording: AVCaptureEventSound](./avcaptureeventsound/endvideorecording.md)
  The default sound for ending a video recording.
### Initializers
- [init(URL: URL) throws](./avcaptureeventsound/init%28url%29-3e9o9.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Capture events
- [class AVCaptureEventInteraction](./avcaptureeventinteraction.md)
  An object that registers handlers to respond to capture events from system hardware buttons.
- [class AVCaptureEvent](./avcaptureevent.md)
  An object that describes a user interaction with a system hardware button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventsound)*