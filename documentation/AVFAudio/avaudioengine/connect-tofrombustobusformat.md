# connect(_:to:fromBus:toBus:format:)

**Framework**: Avfaudio  
**Kind**: method

Establishes a connection between two nodes, specifying the input and output busses.

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
func connect(_ node1: AVAudioNode, to node2: AVAudioNode, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format: AVAudioFormat?)
```

#### Discussion

Audio nodes have input and output busses ([`AVAudioNodeBus`](avaudionodebus.md)). Use this method to establish connections between audio nodes. Connections are always one-to-one, never one-to-many or many-to-one.

> **Note**:  This breaks any preexisting connections that involve the source’s output bus or the destination’s input bus.

## Parameters

- `node1`: The source audio node.
- `node2`: The destination audio node.
- `bus1`: The output bus of the source audio node.
- `bus2`: The input bus of the destination audio node.
- `format`: If not  , the engine uses this value for the format of the source audio node’s output bus. In all cases, the engine matches the format of the destination audio node’s input bus to the source audio node’s output bus.

## See Also

- [func connect(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](avaudioengine/connect(_:to:format:).md)
  Establishes a connection between two nodes.
- [func disconnectNodeInput(AVAudioNode)](avaudioengine/disconnectnodeinput(_:).md)
  Removes all input connections of the node.
- [func disconnectNodeInput(AVAudioNode, bus: AVAudioNodeBus)](avaudioengine/disconnectnodeinput(_:bus:).md)
  Removes the input connection of a node on the specified bus.
- [func disconnectNodeOutput(AVAudioNode)](avaudioengine/disconnectnodeoutput(_:).md)
  Removes all output connections of a node.
- [func disconnectNodeOutput(AVAudioNode, bus: AVAudioNodeBus)](avaudioengine/disconnectnodeoutput(_:bus:).md)
  Removes the output connection of a node on the specified bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connect(_:to:frombus:tobus:format:))*