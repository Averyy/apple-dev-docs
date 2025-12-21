# AVInputPickerInteraction

**Framework**: AVKit  
**Kind**: class

Use `AVInputPickerInteraction` to present an input picker.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
@MainActor
class AVInputPickerInteraction
```

## Topics

### Creating an input picker
- [init()](avinputpickerinteraction/init.md)
  Creates a new instance of AVInputPickerController using a default sharedInstance from `AVAudioSession`.
- [init(audioSession: AVAudioSession?)](avinputpickerinteraction/init(audiosession:).md)
  Creates a new instance of AVInputPickerInteraction using a specific `AVAudioSession`.
### Managing presentation
- [var isPresented: Bool](avinputpickerinteraction/ispresented.md)
  A Boolean value that indicates whether the picker is currently visible.
- [func present()](avinputpickerinteraction/present.md)
  Presents the input picker.
- [func dismiss()](avinputpickerinteraction/dismiss.md)
  Dismisses the input picker.
### Setting the delegate
- [var delegate: (any AVInputPickerInteraction.Delegate)?](avinputpickerinteraction/delegate-swift.property.md)
  The input picker view’s delegate.
- [AVInputPickerInteraction.Delegate](avinputpickerinteraction/delegate-swift.protocol.md)
  The `AVInputPickerInteractionDelegate` protocol defines methods you use to receive notifications about transitions in an `AVInputPickerInteraction` object.
### Accessing the audio session
- [var audioSession: AVAudioSession](avinputpickerinteraction/audiosession.md)
  The audio session for the picker.

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
- [Sendable](../Swift/Sendable.md)
- [UIInteraction](../UIKit/UIInteraction.md)

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
- [class AVCaptureEventSound](avcaptureeventsound.md)
  A sound object for a capture event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction)*