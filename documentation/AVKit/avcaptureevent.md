# AVCaptureEvent

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

An object that describes a user interaction with a system hardware button.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
class AVCaptureEvent
```

```objc
@interface AVCaptureEvent : NSObject
```

#### Overview

Inspect a capture event’s [`phase`](./avcaptureevent/phase.md) to determine whether the event begins, ends, or is in a canceled state.

## Topics

### Inspecting the event
- [var phase: AVCaptureEventPhase](./avcaptureevent/phase.md)
  The current phase of a capture event.
- [enum AVCaptureEventPhase](./avcaptureeventphase.md)
  Constants that indicate the phase of a system capture event.
### Playing a sound
- [var shouldPlaySound: Bool](./avcaptureevent/shouldplaysound.md)
  A Boolean value that indicates whether you must play a sound manually.
- [func play(AVCaptureEventSound) -> Bool](./avcaptureevent/play%28_%29.md)
  Plays the specified capture sound through AirPods.

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
- [class AVCaptureEventSound](./avcaptureeventsound.md)
  A sound object for a capture event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureevent)*