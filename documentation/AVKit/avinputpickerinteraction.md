# AVInputPickerInteraction

**Framework**: AVKit  
**Kind**: class

An object that presents the system’s audio input picker so people can choose which microphone to use for recording audio.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class AVInputPickerInteraction
```

#### Overview

People expect the microphone they chose to be the one your app records with. Add an input picker interaction to a view, and your app presents the same picker the system uses, listing the audio inputs available at that moment.

Create an interaction with [`init(audioSession:)`](avinputpickerinteraction/init(audiosession:).md) to pick inputs for a specific audio session, or with [`init()`](avinputpickerinteraction/init().md) to use the shared session. Pass a session that records, or that you switch to recording, because a session in any other mode produces an empty list of inputs. Add the interaction to a view the way you add any [`UIInteraction`](https://developer.apple.com/documentation/uikit/uiinteraction), then call [`present()`](avinputpickerinteraction/present().md) from the control that offers input selection. Call [`dismiss()`](avinputpickerinteraction/dismiss().md) to take the picker away, and read [`isPresented`](avinputpickerinteraction/ispresented.md) to find out whether it’s onscreen.

Set [`delegate`](avinputpickerinteraction/delegate-swift.property.md) to a [`AVInputPickerInteraction.Delegate`](avinputpickerinteraction/delegate-swift.protocol.md) to learn when the picker begins and finishes presenting, and when it begins and finishes dismissing. The interaction reports those transitions around its own presentation, so an app that dims its interface while someone chooses an input has a place to do that work.

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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [UIInteraction](../uikit/uiinteraction.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avinputpickerinteraction)*