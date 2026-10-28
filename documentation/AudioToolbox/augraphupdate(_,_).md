# AUGraphUpdate(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Updates the state of a running audio processing graph.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: AUGraph is deprecated in favor of AVAudioEngine

## Declaration

```swift
func AUGraphUpdate(_ inGraph: AUGraph, _ outIsUpdated: UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus
```

```c
extern OSStatus AUGraphUpdate(AUGraph inGraph, Boolean *outIsUpdated);
```

## Return Value

A result code.

## Discussion

Call this function to finalize changes to an audio processing graph’s state after making calls such as [`AUGraphConnectNodeInput(_:_:_:_:_:)`](./augraphconnectnodeinput%28_,_,_,_,_%29.md).

Node connections and disconnections can be completely processed in the render notification callback of a graph, finalized by calling this function from within the callback. You can also remove nodes (apart from the head node) from within the render notification callback.

If this function returns the `kAUGraphErr_CannotDoInCurrentContext` result code, another thread was calling a function dependent on the graph’s existing state. When the competing thread completes its call, call this function again.

Audio processing graph updates are all or none. If this function encounters any errors while attempting to finalize graph events, then no pending changes are finalized.

## Parameters

- `inGraph`: 
- `outIsUpdated`: In input, pass `NULL` for synchronous (blocking) behavior, or non-`NULL` to have this function return immediately. On output, `true` if all of the edits were applied to the audio processing graph at the time of function return.

## See Also

### Audio Unit Processing Graph Services Functions
- [func AUGraphAddNode(AUGraph, UnsafePointer<AudioComponentDescription>, UnsafeMutablePointer<AUNode>) -> OSStatus](./augraphaddnode%28_,_,_%29.md)
  Adds a node to an audio processing graph.
- [func AUGraphAddRenderNotify(AUGraph, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](./augraphaddrendernotify%28_,_,_%29.md)
  Adds a render notification callback to an audio processing graph.
- [func AUGraphClearConnections(AUGraph) -> OSStatus](./augraphclearconnections%28_%29.md)
  Clears all of the interactions in an audio unit processing graph.
- [func AUGraphClose(AUGraph) -> OSStatus](./augraphclose%28_%29.md)
  Closes an audio unit processing graph.
- [func AUGraphConnectNodeInput(AUGraph, AUNode, UInt32, AUNode, UInt32) -> OSStatus](./augraphconnectnodeinput%28_,_,_,_,_%29.md)
  Connects one node’s output to another node’s input.
- [func AUGraphCountNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>) -> OSStatus](./augraphcountnodeinteractions%28_,_,_%29.md)
  Retrieves the number of interactions of an audio processing graph’s node.
- [func AUGraphDisconnectNodeInput(AUGraph, AUNode, UInt32) -> OSStatus](./augraphdisconnectnodeinput%28_,_,_%29.md)
  Disconnects a node’s input.
- [func AUGraphGetCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus](./augraphgetcpuload%28_,_%29.md)
  Obtains the short-term running average of the current CPU load of the audio processing graph.
- [func AUGraphGetIndNode(AUGraph, UInt32, UnsafeMutablePointer<AUNode>) -> OSStatus](./augraphgetindnode%28_,_,_%29.md)
  Gets the audio processing graph node at a given index.
- [func AUGraphGetInteractionInfo(AUGraph, UInt32, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus](./augraphgetinteractioninfo%28_,_,_%29.md)
  Retrieves information about a particular interaction in an audio processing graph.
- [func AUGraphGetMaxCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus](./augraphgetmaxcpuload%28_,_%29.md)
  Obtains the maximum CPU load of an audio processing graph since this call was last made or since the graph was last started.
- [func AUGraphGetNodeCount(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus](./augraphgetnodecount%28_,_%29.md)
  The number of nodes in an audio processing graph.
- [func AUGraphGetNodeInfoSubGraph(AUGraph, AUNode, UnsafeMutablePointer<AUGraph?>) -> OSStatus](./augraphgetnodeinfosubgraph%28_,_,_%29.md)
  Gets the audio processing subgraph object represented by a node.
- [func AUGraphGetNodeInteractions(AUGraph, AUNode, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus](./augraphgetnodeinteractions%28_,_,_,_%29.md)
  Retrieves information about the interactions in an audio processing graph for a given node.
- [func AUGraphGetNumberOfInteractions(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus](./augraphgetnumberofinteractions%28_,_%29.md)
  Retrieves the number of interactions for an audio processing graph.
- [AUGraphCountNodeConnections](./augraphcountnodeconnections.md)
  Deprecated in OS X v10.5. Instead, use [`AUGraphCountNodeInteractions`](./augraphcountnodeinteractions%28_,_,_%29.md).
- [AUGraphGetConnectionInfo](./augraphgetconnectioninfo.md)
  Deprecated in OS X v10.5. Instead, use [`AUGraphGetInteractionInfo`](./augraphgetinteractioninfo%28_,_,_%29.md).
- [AUGraphGetNodeConnections](./augraphgetnodeconnections.md)
  Deprecated in OS X v10.5. Instead, use [`AUGraphGetNodeInteractions`](./augraphgetnodeinteractions%28_,_,_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/augraphupdate(_:_:))*