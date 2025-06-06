# connect(_:to:format:)

**Framework**: AVFAudio  
**Kind**: method

Establishes a connection between two nodes.

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
func connect(_ node1: AVAudioNode, to node2: AVAudioNode, format: AVAudioFormat?)
```

#### Discussion

This method calls [`connect(_:to:fromBus:toBus:format:)`](avaudioengine/connect(_:to:frombus:tobus:format:).md) using bus `0` for the source audio node, and bus `0` for the destination audio node, except when a destination is a mixer, in which case, the destination is the mixer’s [`nextAvailableInputBus`](avaudiomixernode/nextavailableinputbus.md).

## Parameters

- `node1`: The source audio node.
- `node2`: The destination audio node.
- `format`: If not  , the engine uses this value for the format of the source audio node’s output bus. In all cases, the engine matches the format of the destination audio node’s input bus to the source audio node’s output bus.

## See Also

- [func connect(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?)](avaudioengine/connect(_:to:frombus:tobus:format:).md)
  Establishes a connection between two nodes, specifying the input and output busses.
- [func disconnectNodeInput(AVAudioNode)](avaudioengine/disconnectnodeinput(_:).md)
  Removes all input connections of the node.
- [func disconnectNodeInput(AVAudioNode, bus: AVAudioNodeBus)](avaudioengine/disconnectnodeinput(_:bus:).md)
  Removes the input connection of a node on the specified bus.
- [func disconnectNodeOutput(AVAudioNode)](avaudioengine/disconnectnodeoutput(_:).md)
  Removes all output connections of a node.
- [func disconnectNodeOutput(AVAudioNode, bus: AVAudioNodeBus)](avaudioengine/disconnectnodeoutput(_:bus:).md)
  Removes the output connection of a node on the specified bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connect(_:to:format:))*