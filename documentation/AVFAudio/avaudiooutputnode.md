# AVAudioOutputNode

**Framework**: AVFAudio  
**Kind**: class

An object that connects to the system’s audio output.

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
class AVAudioOutputNode
```

#### Overview

This node connects to the system’s audio output when rendering to or from an audio device. This node performs output in response to client’s requests when the engine is in manual rendering mode.

This audio node has one element. The format of the output scope reflects:

- The audio hardware sample rate and channel count when it connects to the hardware.
- The engine’s manual rendering mode output format (see [`manualRenderingFormat`](avaudioengine/manualrenderingformat.md)).

The format of the input scope is initially the same as that of the output, but you may set it to a different format, in which case the audio node converts.

> ❗ **Important**:  This class has no methods of its own. It overrides methods that its base classes define.

 This class has no methods of its own. It overrides methods that its base classes define.

## Relationships

### Inherits From
- [AVAudioIONode](avaudioionode.md)
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
- [class AVAudioIONode](avaudioionode.md)
  An object that performs audio input or output in the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiooutputnode)*