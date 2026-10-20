# disconnectNodeInput(_:bus:)

**Framework**: AVFAudio  
**Kind**: method  
**Role**: Instance Method

Removes the input connection of a node on the specified bus.

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
func disconnectNodeInput(_ node: AVAudioNode, bus: AVAudioNodeBus)
```

```objc
- (void) disconnectNodeInput:(AVAudioNode *) node bus:(AVAudioNodeBus) bus;
```

## Parameters

- `node`: The audio node with the input to disconnect.
- `bus`: The destination’s input bus to disconnect.

## See Also

### Connecting and disconnecting audio nodes
- [func connectNode(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?) throws](./connectnode%28_,to,format%29.md)
- [func connectNode(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,tobus,format%29.md)
- [func connectNode(AVAudioNode, to: [AVAudioConnectionPoint], fromBus: AVAudioNodeBus, format: AVAudioFormat?) throws](./connectnode%28_,to,frombus,format%29.md)
- [func connect(AVAudioNode, to: AVAudioNode, format: AVAudioFormat?)](./connect%28_,to,format%29.md)
  Establishes a connection between two nodes.
- [func connect(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?)](./connect%28_,to,frombus,tobus,format%29.md)
  Establishes a connection between two nodes, specifying the input and output busses.
- [func disconnectNodeInput(AVAudioNode)](./disconnectnodeinput%28_%29.md)
  Removes all input connections of the node.
- [func disconnectNodeOutput(AVAudioNode)](./disconnectnodeoutput%28_%29.md)
  Removes all output connections of a node.
- [func disconnectNodeOutput(AVAudioNode, bus: AVAudioNodeBus)](./disconnectnodeoutput%28_,bus%29.md)
  Removes the output connection of a node on the specified bus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/disconnectnodeinput(_:bus:))*