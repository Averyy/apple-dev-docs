# connect(_:to:format:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Establishes a connection between two nodes.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 2.0+ - Deprecated in 27.0

## Declaration

```swift
func connect(_ node1: AVAudioNode, to node2: AVAudioNode, format: AVAudioFormat?)
```

```objc
- (void) connect:(AVAudioNode *) node1 to:(AVAudioNode *) node2 format:(AVAudioFormat *) format;
```

#### Discussion

This method calls [`connect(_:to:fromBus:toBus:format:)`](./connect%28_,to,frombus,tobus,format%29.md) using bus `0` for the source audio node, and bus `0` for the destination audio node, except when a destination is a mixer, in which case, the destination is the mixer’s [`nextAvailableInputBus`](../avaudiomixernode/nextavailableinputbus.md).

## Parameters

- `node1`: The source audio node.
- `node2`: The destination audio node.
- `format`: If not `NULL`, the engine uses this value for the format of the source audio node’s output bus. In all cases, the engine matches the format of the destination audio node’s input bus to the source audio node’s output bus.

## See Also

### Connecting and disconnecting audio nodes
- [func connectNode(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?) throws](./connectnode%28_,to,format%29.md)
- [func connectNode(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,tobus,format%29.md)
- [func connectNode(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,format%29.md)
- [func connect(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?)](./connect%28_,to,frombus,tobus,format%29.md)
  Establishes a connection between two nodes, specifying the input and output busses.
- [func disconnectNodeInput(AVAudioNode)](./disconnectnodeinput%28_%29.md)
  Removes all input connections of the node.
- [func disconnectNodeInput(AVAudioNode, bus: AVAudioNodeBus)](./disconnectnodeinput%28_,bus%29.md)
  Removes the input connection of a node on the specified bus.
- [func disconnectNodeOutput(AVAudioNode)](./disconnectnodeoutput%28_%29.md)
  Removes all output connections of a node.
- [func disconnectNodeOutput(AVAudioNode, bus: AVAudioNodeBus)](./disconnectnodeoutput%28_,bus%29.md)
  Removes the output connection of a node on the specified bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connect(_:to:format:))*