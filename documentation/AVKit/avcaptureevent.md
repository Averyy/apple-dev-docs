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
### Playing a sound
- [var shouldPlaySound: Bool](avcaptureevent/shouldplaysound.md)
  A Boolean value that indicates whether you must play a sound manually.
- [func play(AVCaptureEventSound) -> Bool](avcaptureevent/play(_:).md)
  Plays the specified capture sound through AirPods.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class AVCaptureEventInteraction](avcaptureeventinteraction.md)
  An object that registers handlers to respond to capture events from system hardware buttons.
- [class AVCaptureEventSound](avcaptureeventsound.md)
  A sound object for a capture event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureevent)*