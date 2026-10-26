# AUGraphNewNodeSubGraph(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Creates a node object to represent a subgraph.

**Availability**:
- macOS 10.2+ - Deprecated in 27.2

> **Deprecated**: no longer supported

## Declaration

```swift
func AUGraphNewNodeSubGraph(_ inGraph: AUGraph, _ outNode: UnsafeMutablePointer<AUNode>) -> OSStatus
```

```c
extern OSStatus AUGraphNewNodeSubGraph(AUGraph inGraph, AUNode *outNode);
```

#### Return Value

A result code.

#### Discussion

This function creates a node that represents a subgraph. The subgraph can be retrieved with the [`AUGraphGetNodeInfoSubGraph(_:_:_:)`](./augraphgetnodeinfosubgraph%28_,_,_%29.md) function. The subgraph is owned by the parent graph and will be disposed when the parent graph is disposed or when the node is removed from the parent graph.

## Parameters

- `inGraph`: The AUGraph object that you want to add a subgraph to.
- `outNode`: The node that represents the subgraph.

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/augraphnewnodesubgraph(_:_:))*