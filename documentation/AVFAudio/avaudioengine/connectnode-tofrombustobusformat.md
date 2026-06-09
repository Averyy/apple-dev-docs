# connectNode(_:to:fromBus:toBus:format:)

**Framework**: AVFAudio  
**Kind**: method

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
func connectNode(_ node1: AVAudioNode, to node2: AVAudioNode, fromBus bus1: AVAudioNodeBus, toBus bus2: AVAudioNodeBus, format: AVAudioFormat?) throws
```

#### Discussion

Establish a connection between two nodes.

Nodes have input and output buses (AVAudioNodeBus). Use this method to establish one-to-one connections betweeen nodes. Connections made using this method are always one-to-one, never one-to-many or many-to-one.

Note that any pre-existing connection(s) involving the source’s output bus or the destination’s input bus will be broken.

## Parameters

- `node1`: The source node
- `node2`: The destination node
- `bus1`: The output bus on the source node
- `bus2`: The input bus on the destination node
- `format`: If non-nil, the format of the source node’s output bus is set to this format. In all cases, the format of the destination node’s input bus is set to match that of the source node’s output bus.

## See Also

- [func connectNode(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?) throws](avaudioengine/connectnode(_:to:format:).md)
- [func connectNode(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?) throws](avaudioengine/connectnode(_:to:frombus:format:).md)
- [func connect(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](avaudioengine/connect(_:to:format:).md)
  Establishes a connection between two nodes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectnode(_:to:frombus:tobus:format:))*