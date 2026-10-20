# AUGraphDisconnectNodeInput(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Disconnects a node’s input.

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
func AUGraphDisconnectNodeInput(_ inGraph: AUGraph, _ inDestNode: AUNode, _ inDestInputNumber: UInt32) -> OSStatus
```

```c
extern OSStatus AUGraphDisconnectNodeInput(AUGraph inGraph, AUNode inDestNode, UInt32 inDestInputNumber);
```

#### Return Value

A result code.

#### Discussion

Use this function to disconnect a connection or a callback interaction.

## Parameters

- `inGraph`: 
- `inDestNode`: 
- `inDestInputNumber`: 

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
- [func AUGraphInitialize(AUGraph) -> OSStatus](./augraphinitialize%28_%29.md)
  Initializes an audio processing graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/augraphdisconnectnodeinput(_:_:_:))*