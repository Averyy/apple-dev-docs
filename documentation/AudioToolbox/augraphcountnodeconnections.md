# AUGraphCountNodeConnections

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Deprecated in OS X v10.5. Instead, use [`AUGraphCountNodeInteractions(_:_:_:)`](./augraphcountnodeinteractions%28_,_,_%29.md).

**Availability**:
- macOS 10.3+ - Deprecated in 10.5

## Declaration

```c
extern OSStatus AUGraphCountNodeConnections(AUGraph inGraph, AUNode inNode, UInt32 *outNumConnections);
```

#### Return Value

A result code.

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
- [AUGraphGetConnectionInfo](./augraphgetconnectioninfo.md)
  Deprecated in OS X v10.5. Instead, use [`AUGraphGetInteractionInfo(_:_:_:)`](./augraphgetinteractioninfo%28_,_,_%29.md).
- [func AUGraphGetCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus](./augraphgetcpuload%28_,_%29.md)
  Obtains the short-term running average of the current CPU load of the audio processing graph.
- [func AUGraphGetIndNode(AUGraph, UInt32, UnsafeMutablePointer<AUNode>) -> OSStatus](./augraphgetindnode%28_,_,_%29.md)
  Gets the audio processing graph node at a given index.
- [func AUGraphGetInteractionInfo(AUGraph, UInt32, UnsafeMutablePointer<AUNodeInteraction>) -> OSStatus](./augraphgetinteractioninfo%28_,_,_%29.md)
  Retrieves information about a particular interaction in an audio processing graph.
- [func AUGraphGetMaxCPULoad(AUGraph, UnsafeMutablePointer<Float32>) -> OSStatus](./augraphgetmaxcpuload%28_,_%29.md)
  Obtains the maximum CPU load of an audio processing graph since this call was last made or since the graph was last started.
- [AUGraphGetNodeConnections](./augraphgetnodeconnections.md)
  Deprecated in OS X v10.5. Instead, use [`AUGraphGetNodeInteractions(_:_:_:_:)`](./augraphgetnodeinteractions%28_,_,_,_%29.md).
- [func AUGraphGetNodeCount(AUGraph, UnsafeMutablePointer<UInt32>) -> OSStatus](./augraphgetnodecount%28_,_%29.md)
  The number of nodes in an audio processing graph.
- [AUGraphGetNodeInfo](./augraphgetnodeinfo.md)
  Deprecated in OS X v10.5. Instead, use [`AUGraphNodeInfo(_:_:_:_:)`](./augraphnodeinfo%28_,_,_,_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/augraphcountnodeconnections)*