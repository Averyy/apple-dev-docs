# AVAudioIONode

**Framework**: AVFAudio  
**Kind**: class

An object that performs audio input or output in the engine.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioIONode
```

#### Overview

When rendering to and from an audio device in macOS, [`AVAudioInputNode`](avaudioinputnode.md) and [`AVAudioOutputNode`](avaudiooutputnode.md) communicate with the system’s default input and output devices. In iOS, they communicate with the devices appropriate to the app’s [`AVAudioSession`](avaudiosession.md) category, configurations, and user actions, such as connecting or disconnecting external devices.

In the manual rendering mode, [`AVAudioInputNode`](avaudioinputnode.md) and [`AVAudioOutputNode`](avaudiooutputnode.md) perform the input and output in the engine in response to the client’s request.

## Topics

### Getting the Audio Unit
- [var audioUnit: AudioUnit?](avaudioionode/audiounit.md)
  The node’s underlying audio unit, if any.
### Getting the I/O Latency
- [var presentationLatency: TimeInterval](avaudioionode/presentationlatency.md)
  The presentation or hardware latency, applicable when rendering to or from an audio device.
### Getting and Setting the Voice Processing State
- [func setVoiceProcessingEnabled(Bool) throws](avaudioionode/setvoiceprocessingenabled(_:).md)
  Enables or disables voice processing on the I/O node.
- [var isVoiceProcessingEnabled: Bool](avaudioionode/isvoiceprocessingenabled.md)
  A Boolean value that indicates whether voice processing is in an enabled state.

## Relationships

### Inherits From
- [AVAudioNode](avaudionode.md)
### Inherited By
- [AVAudioInputNode](avaudioinputnode.md)
- [AVAudioOutputNode](avaudiooutputnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioNode](avaudionode.md)
  An object you use for audio generation, processing, or an I/O block.
- [class AVAudioInputNode](avaudioinputnode.md)
  An object that connects to the system’s audio input.
- [class AVAudioOutputNode](avaudiooutputnode.md)
  An object that connects to the system’s audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioionode)*