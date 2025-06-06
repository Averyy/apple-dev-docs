# AVAudioNode

**Framework**: AVFAudio  
**Kind**: class

An object you use for audio generation, processing, or an I/O block.

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
class AVAudioNode
```

#### Overview

An [`AVAudioEngine`](avaudioengine.md) object contains instances of audio nodes that you attach, and this base class provides common functionality. Instances of this class don’t provide useful functionality until you attach them to an engine.

Nodes have input and output busses that serve as connection points. For example, an effect has one input bus and one output bus, and a mixer has multiple input busses and one output bus.

A bus contains a format the framework expresses in terms of sample rate and channel count. Formats must match exactly when making connections between nodes, excluding [`AVAudioMixerNode`](avaudiomixernode.md) and [`AVAudioOutputNode`](avaudiooutputnode.md).

## Topics

### Configuring an Input Format Bus
- [typealias AVAudioNodeBus](avaudionodebus.md)
  The index of a bus on an audio node.
- [func inputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](avaudionode/inputformat(forbus:).md)
  Gets the input format for the bus you specify.
- [func name(forInputBus: AVAudioNodeBus) -> String?](avaudionode/name(forinputbus:).md)
  Gets the name of the input bus you specify.
- [var numberOfInputs: Int](avaudionode/numberofinputs.md)
  The number of input busses for the node.
### Creating an Output Format Bus
- [func outputFormat(forBus: AVAudioNodeBus) -> AVAudioFormat](avaudionode/outputformat(forbus:).md)
  Retrieves the output format for the bus you specify.
- [func name(forOutputBus: AVAudioNodeBus) -> String?](avaudionode/name(foroutputbus:).md)
  Retrieves the name of the output bus you specify.
- [var numberOfOutputs: Int](avaudionode/numberofoutputs.md)
  The number of output busses for the node.
### Installing and Removing an Audio Tap
- [func installTap(onBus: AVAudioNodeBus, bufferSize: AVAudioFrameCount, format: AVAudioFormat?, block: AVAudioNodeTapBlock)](avaudionode/installtap(onbus:buffersize:format:block:).md)
  Installs an audio tap on a bus you specify to record, monitor, and observe the output of the node.
- [func removeTap(onBus: AVAudioNodeBus)](avaudionode/removetap(onbus:).md)
  Removes an audio tap on a bus you specify.
- [typealias AVAudioNodeTapBlock](avaudionodetapblock.md)
  The block that receives copies of the output of an audio node.
### Getting the Audio Engine for the Node
- [var engine: AVAudioEngine?](avaudionode/engine.md)
  The audio engine that manages the node, if any.
### Getting the Latest Node Render Time
- [var lastRenderTime: AVAudioTime?](avaudionode/lastrendertime.md)
  The most recent render time.
### Getting Audio Node Properties
- [var auAudioUnit: AUAudioUnit](avaudionode/auaudiounit.md)
  An audio unit object that wraps or underlies the implementation’s audio unit.
- [var latency: TimeInterval](avaudionode/latency.md)
  The processing latency of the node, in seconds.
- [var outputPresentationLatency: TimeInterval](avaudionode/outputpresentationlatency.md)
  The maximum render pipeline latency downstream of the node, in seconds.
### Resetting the Audio Node
- [func reset()](avaudionode/reset.md)
  Clears a unit’s previous processing state.
### Constants
- [typealias AVAudioNodeCompletionHandler](avaudionodecompletionhandler.md)
  A general callback handler for an audio node.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVAudioEnvironmentNode](avaudioenvironmentnode.md)
- [AVAudioIONode](avaudioionode.md)
- [AVAudioMixerNode](avaudiomixernode.md)
- [AVAudioPlayerNode](avaudioplayernode.md)
- [AVAudioSinkNode](avaudiosinknode.md)
- [AVAudioSourceNode](avaudiosourcenode.md)
- [AVAudioUnit](avaudiounit.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioInputNode](avaudioinputnode.md)
  An object that connects to the system’s audio input.
- [class AVAudioOutputNode](avaudiooutputnode.md)
  An object that connects to the system’s audio output.
- [class AVAudioIONode](avaudioionode.md)
  An object that performs audio input or output in the engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudionode)*