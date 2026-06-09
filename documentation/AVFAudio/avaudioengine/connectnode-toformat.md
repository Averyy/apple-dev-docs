# connectNode(_:to:format:)

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
func connectNode(_ node1: AVAudioNode, to node2: AVAudioNode, format: AVAudioFormat?) throws
```

#### Discussion

Establish a connection between two nodes

This calls connect:to:fromBus:toBus:format: using bus 0 on the source node, and bus 0 on the destination node, except in the case of a destination which is a mixer, in which case the destination is the mixer’s nextAvailableInputBus.

## See Also

- [func connectNode(AVAudioNode, to: AVAudioNode, fromBus: AVAudioNodeBus, toBus: AVAudioNodeBus, format: AVAudioFormat?) throws](avaudioengine/connectnode(_:to:frombus:tobus:format:).md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioengine/connectnode(_:to:format:))*