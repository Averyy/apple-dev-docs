# AUGraphUpdate(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Updates the state of a running audio processing graph.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Call this function to finalize changes to an audio processing graph’s state after making calls such as [`AUGraphConnectNodeInput(_:_:_:_:_:)`](augraphconnectnodeinput(_:_:_:_:_:).md).

Node connections and disconnections can be completely processed in the render notification callback of a graph, finalized by calling this function from within the callback. You can also remove nodes (apart from the head node) from within the render notification callback.

If this function returns the `kAUGraphErr_CannotDoInCurrentContext` result code, another thread was calling a function dependent on the graph’s existing state. When the competing thread completes its call, call this function again.

Audio processing graph updates are all or none. If this function encounters any errors while attempting to finalize graph events, then no pending changes are finalized.

## Parameters

- `inGraph`: 
- `outIsUpdated`: In input, pass   for synchronous (blocking) behavior, or non-  to have this function return immediately. On output,   if all of the edits were applied to the audio processing graph at the time of function return.

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/augraphupdate(_:_:))*