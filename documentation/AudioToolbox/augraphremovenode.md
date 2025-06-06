# AUGraphRemoveNode(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Removes a node from an audio processing graph.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AUGraphRemoveNode(_ inGraph: AUGraph, _ inNode: AUNode) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Nodes can be removed in any thread context. The output node of the graph cannot be removed while the graph is running.

## Parameters

- `inGraph`: The   object that you are removing a node from.
- `inNode`: The node you want to remove.

## See Also

- [func AUGraphAddNode(AUGraph, UnsafePointer<AudioComponentDescription>, UnsafeMutablePointer<AUNode>) -> OSStatus](augraphaddnode(_:_:_:).md)
  Adds a node to an audio processing graph.
- [func AUGraphAddRenderNotify(AUGraph, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](augraphaddrendernotify(_:_:_:).md)
  Adds a render notification callback to an audio processing graph.
- [func AUGraphClearConnections(AUGraph) -> OSStatus](augraphclearconnections(_:).md)
  Clears all of the interactions in an audio unit processing graph.
- [func AUGraphClose(AUGraph) -> OSStatus](augraphclose(_:).md)
  Closes an audio unit processing graph.
- [func AUGraphConnectNodeInput(AUGraph, AUNode, UInt32, AUNode, UInt32) -> OSStatus](augraphconnectnodeinput(_:_:_:_:_:).md)
  Connects one node’s output to another node’s input.
- [func AUGraphCountNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>) -> OSStatus](augraphcountnodeinteractions(_:_:_:).md)
  Retrieves the number of interactions of an audio processing graph’s node.
- [func AUGraphDisconnectNodeInput(AUGraph, AUNode, UInt32) -> OSStatus](augraphdisconnectnodeinput(_:_:_:).md)
  Disconnects a node’s input.
- [func AUGraphGetCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus](augraphgetcpuload(_:_:).md)
  Obtains the short-term running average of the current CPU load of the audio processing graph.
- [func AUGraphGetIndNode(AUGraph, UInt32, UnsafeMutablePointer<AUNode>) -> OSStatus](augraphgetindnode(_:_:_:).md)
  Gets the audio processing graph node at a given index.
- [func AUGraphGetInteractionInfo(AUGraph, UInt32, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus](augraphgetinteractioninfo(_:_:_:).md)
  Retrieves information about a particular interaction in an audio processing graph.
- [func AUGraphGetMaxCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus](augraphgetmaxcpuload(_:_:).md)
  Obtains the maximum CPU load of an audio processing graph since this call was last made or since the graph was last started.
- [func AUGraphGetNodeCount(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus](augraphgetnodecount(_:_:).md)
  The number of nodes in an audio processing graph.
- [func AUGraphGetNodeInfoSubGraph(AUGraph, AUNode, UnsafeMutablePointer<AUGraph?>) -> OSStatus](augraphgetnodeinfosubgraph(_:_:_:).md)
  Gets the audio processing subgraph object represented by a node.
- [func AUGraphGetNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus](augraphgetnodeinteractions(_:_:_:_:).md)
  Retrieves information about the interactions in an audio processing graph for a given node.
- [func AUGraphGetNumberOfInteractions(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus](augraphgetnumberofinteractions(_:_:).md)
  Retrieves the number of interactions for an audio processing graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/augraphremovenode(_:_:))*