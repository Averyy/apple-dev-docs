# AVCaptureEvent

**Framework**: AVKit  
**Kind**: class

An object that describes a user interaction with a system hardware button.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
class AVCaptureEvent
```

#### Overview

Inspect a capture event’s [`phase`](avcaptureevent/phase.md) to determine whether the event begins, ends, or is in a canceled state.

## Topics

### Inspecting the event
- [var phase: AVCaptureEventPhase](avcaptureevent/phase.md)
  The current phase of a capture event.
- [enum AVCaptureEventPhase](avcaptureeventphase.md)
  Constants that indicate the phase of a system capture event.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureevent)*