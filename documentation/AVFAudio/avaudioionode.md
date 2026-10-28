# AVAudioIONode

**Framework**: AVFAudio  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAudioIONode : AVAudioNode
```

## Overview

When rendering to and from an audio device in macOS, [`AVAudioInputNode`](./avaudioinputnode.md) and [`AVAudioOutputNode`](./avaudiooutputnode.md) communicate with the system’s default input and output devices. In iOS, they communicate with the devices appropriate to the app’s [`AVAudioSession`](./avaudiosession.md) category, configurations, and user actions, such as connecting or disconnecting external devices.

In the manual rendering mode, [`AVAudioInputNode`](./avaudioinputnode.md) and [`AVAudioOutputNode`](./avaudiooutputnode.md) perform the input and output in the engine in response to the client’s request.

## Topics

### Getting the Audio Unit
- [func withAudioUnit<R, E>((borrowing AudioUnit?) throws(E) -> R) throws(E) -> R](./avaudioionode/withaudiounit%28_%29-57kv.md)
  Provides scoped access to the I/O node’s AudioUnit
- [func withAudioUnit<R, E>((borrowing AudioUnit?) throws(E) -> R) throws(E) -> R](./avaudioionode/withaudiounit%28_%29-6i8ld.md)
  Provides scoped access to the I/O node’s AudioUnit
- [var audioUnit: AudioUnit?](./avaudioionode/audiounit-1bqu3.md)
- [var audioUnit: AudioUnit?](./avaudioionode/audiounit-1caha.md)
- [audioUnit](./avaudioionode/audiounit-4xtq9.md)
  The node’s underlying audio unit, if any.
### Getting the I/O latency
- [var presentationLatency: TimeInterval](./avaudioionode/presentationlatency.md)
  The presentation or hardware latency, applicable when rendering to or from an audio device.
### Enabling voice processing
- [func setVoiceProcessingEnabled(Bool) throws](./avaudioionode/setvoiceprocessingenabled%28_%29.md)
  Enables or disables voice processing on the I/O node.
- [var isVoiceProcessingEnabled: Bool](./avaudioionode/isvoiceprocessingenabled.md)
  A Boolean value that indicates whether voice processing is in an enabled state.

## Relationships

### Inherits From
- [AVAudioNode](./avaudionode.md)
### Inherited By
- [AVAudioInputNode](./avaudioinputnode.md)
- [AVAudioOutputNode](./avaudiooutputnode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Engine and nodes
- [Using voice processing](./using-voice-processing.md)
  Add voice-processing capabilities to your app by using audio engine.
- [class AVAudioEngine](./avaudioengine.md)
  An object that manages a graph of audio nodes, controls playback, and configures real-time rendering constraints.
- [class AVAudioInputNode](./avaudioinputnode.md)
  An object that connects to the system’s audio input.
- [class AVAudioOutputNode](./avaudiooutputnode.md)
  An object that connects to the system’s audio output.
- [class AVAudioNode](./avaudionode.md)
  An object you use for audio generation, processing, or an I/O block.
- [AVAudioIONodeInputBlockRealtimeSafe](./avaudioionodeinputblockrealtimesafe.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioionode)*