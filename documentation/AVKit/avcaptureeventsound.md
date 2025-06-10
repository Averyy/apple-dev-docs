# AVCaptureEventSound

**Framework**: AVKit  
**Kind**: class

A sound object for a capture event.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)

## Declaration

```swift
class AVCaptureEventSound
```

## Topics

### Creating a sound
- [init(url: URL!) throws](avcaptureeventsound/init(url:).md)
  Initializer for an AVCaptureEventSound with a custom sound.
### Accessing default sounds
- [class var cameraShutter: AVCaptureEventSound!](avcaptureeventsound/camerashutter.md)
  The default sound for photo capture.
- [class var beginVideoRecording: AVCaptureEventSound!](avcaptureeventsound/beginvideorecording.md)
  The default sound for starting a video recording.
- [class var endVideoRecording: AVCaptureEventSound!](avcaptureeventsound/endvideorecording.md)
  The default sound for ending a video recording.

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

- [Playing video content in a standard user interface](playing-video-content-in-a-standard-user-interface.md)
  Play media full screen, embedded inline, or in a floating Picture in Picture (PiP) window using a player view controller.
- [class AVPlayerViewController](avplayerviewcontroller.md)
  A view controller that displays content from a player and presents a native user interface to control playback.
- [protocol AVPlayerViewControllerDelegate](avplayerviewcontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to player view controller events.
- [class AVCaptureEventInteraction](avcaptureeventinteraction.md)
  An object that registers handlers to respond to capture events from system hardware buttons.
- [class AVCaptureEvent](avcaptureevent.md)
  An object that describes a user interaction with a system hardware button.
- [class AVInputPickerInteraction](avinputpickerinteraction.md)
  Use `AVInputPickerInteraction` to present an input picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventsound)*