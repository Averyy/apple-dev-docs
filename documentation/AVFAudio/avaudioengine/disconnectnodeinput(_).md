# disconnectNodeInput(_:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Removes all input connections of the node.

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
func disconnectNodeInput(_ node: AVAudioNode)
```

```objc
- (void) disconnectNodeInput:(AVAudioNode *) node;
```

## Discussion

Connections break on each of the audio node’s input buses.

## Parameters

- `node`: The audio node with the inputs you want to disconnect.

## See Also

### Connecting and disconnecting audio nodes
- [func connectNode(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?) throws](./connectnode%28_,to,format%29.md)
- [func connectNode(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,tobus,format%29.md)
- [func connectNode(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,format%29.md)
- [func connect(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](./connect%28_,to,format%29.md)
  Establishes a connection between two nodes.
- [func connect(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?)](./connect%28_,to,frombus,tobus,format%29.md)
  Establishes a connection between two nodes, specifying the input and output busses.
- [func disconnectNodeInput(AVAudioNode, bus: AVAudioNodeBus)](./disconnectnodeinput%28_,bus%29.md)
  Removes the input connection of a node on the specified bus.
- [func disconnectNodeOutput(AVAudioNode)](./disconnectnodeoutput%28_%29.md)
  Removes all output connections of a node.
- [func disconnectNodeOutput(AVAudioNode, bus: AVAudioNodeBus)](./disconnectnodeoutput%28_,bus%29.md)
  Removes the output connection of a node on the specified bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/disconnectnodeinput(_:))*