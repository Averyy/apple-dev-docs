# connectNode(_:to:fromBus:format:)

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
func connectNode(_ sourceNode: AVAudioNode, to destNodes: [AVAudioConnectionPoint], fromBus sourceBus: AVAudioNodeBus, format: AVAudioFormat?) throws
```

#### Discussion

Establish connections between a source node and multiple destination nodes.

Use this method to establish connections from a source node to multiple destination nodes. Connections made using this method are either one-to-one (when a single destination connection is specified) or one-to-many (when multiple connections are specified), but never many-to-one.

To incrementally add a new connection to a source node, use this method with an array of AVAudioConnectionPoint objects comprising of pre-existing connections (obtained from `outputConnectionPointsForNode:outputBus:`) and the new connection.

Note that any pre-existing connection involving the destination’s input bus will be broken. And, any pre-existing connection on source node which is not a part of the specified destination connection array will also be broken.

Also note that when the output of a node is split into multiple paths, all the paths must render at the same rate until they reach a common mixer. In other words, starting from the split node until the common mixer node where all split paths terminate, you cannot have:

- any AVAudioUnitTimeEffect
- any sample rate conversion

## Parameters

- `sourceNode`: The source node
- `destNodes`: An array of AVAudioConnectionPoint objects specifying destination nodes and busses
- `sourceBus`: The output bus on source node
- `format`: If non-nil, the format of the source node’s output bus is set to this format. In all cases, the format of the destination nodes’ input bus is set to match that of the source node’s output bus

## See Also

- [func connectNode(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?) throws](avaudioengine/connectnode(_:to:format:).md)
- [func connectNode(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?) throws](avaudioengine/connectnode(_:to:frombus:tobus:format:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectnode(_:to:frombus:format:))*