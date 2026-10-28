# connectNode(_:to:format:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
func connectNode(_ node1: AVAudioNode, to node2: AVAudioNode, format: AVAudioFormat?) throws
```

```objc
- (BOOL) connect:(AVAudioNode *) node1 to:(AVAudioNode *) node2 format:(AVAudioFormat *) format error:(NSError **) error;
```

## Discussion

Establish a connection between two nodes

This calls connect:to:fromBus:toBus:format: using bus 0 on the source node, and bus 0 on the destination node, except in the case of a destination which is a mixer, in which case the destination is the mixer’s nextAvailableInputBus.

## See Also

### Connecting and disconnecting audio nodes
- [func connectNode(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,tobus,format%29.md)
- [func connectNode(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,format%29.md)
- [func connect(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](./connect%28_,to,format%29.md)
  Establishes a connection between two nodes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectnode(_:to:format:))*