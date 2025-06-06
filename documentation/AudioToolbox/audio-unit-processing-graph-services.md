# Audio Unit Processing Graph Services

**Framework**: Audio Toolbox

Audio Unit Processing Graph Services provide interfaces for representing a set of audio units, connections between their inputs and outputs, and callbacks used to provide inputs. It also enables the embedding of sub (or child) processing graphs within parent graphs to allow for a logical organization of parts of an overall signal chain.

#### Overview

An audio processing graph object (of type `AUGraph`) is a complete description of an audio signal processing network. Audio Unit Processing Graph Services may manage the instantiated audio units if the `AUGraphOpen` function is called.

An audio processing graph object may be introspected to get complete information about all of the audio units in the graph. The various node objects (each of type `AUNode`) in the graph, each representing an audio unit or a sub graph, may be added or removed, and the interactions between them modified.

A graph object’s state can be manipulated in both the rendering thread and in other threads. Consequently, any activities that affect the state of the graph are guarded with locks and a messaging model between any calling thread and the thread upon which the graph object’s output unit is called (the render thread).

A graph object will have a single head node––an output unit. The output unit is used to both start and stop the rendering operations of a graph, and is the dispatch point for the safe manipulation of the state of the graph while it is running.

## Topics

### Audio Unit Processing Graph Services Functions
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
- [func AUGraphInitialize(AUGraph) -> OSStatus](augraphinitialize(_:).md)
  Initializes an audio processing graph.
- [func AUGraphIsInitialized(AUGraph, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](augraphisinitialized(_:_:).md)
  Determines whether an audio processing graph is initialized.
- [func AUGraphIsNodeSubGraph(AUGraph, AUNode, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](augraphisnodesubgraph(_:_:_:).md)
  Determines whether a node object represent an audio processing graph or an audio unit.
- [func AUGraphIsOpen(AUGraph, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](augraphisopen(_:_:).md)
  Determines whether an audio processing graph is open.
- [func AUGraphIsRunning(AUGraph, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](augraphisrunning(_:_:).md)
  Determines whether an audio processing graph running.
- [func AUGraphNewNodeSubGraph(AUGraph, UnsafeMutablePointer<AUNode>) -> OSStatus](augraphnewnodesubgraph(_:_:).md)
  Creates a node object to represent a subgraph.
- [func AUGraphNodeInfo(AUGraph, AUNode, UnsafeMutablePointer<AudioComponentDescription>?, UnsafeMutablePointer<AudioUnit?>?) -> OSStatus](augraphnodeinfo(_:_:_:_:).md)
  Returns information about a node object.
- [func AUGraphOpen(AUGraph) -> OSStatus](augraphopen(_:).md)
  Opens an audio processing graph.
- [func AUGraphRemoveNode(AUGraph, AUNode) -> OSStatus](augraphremovenode(_:_:).md)
  Removes a node from an audio processing graph.
- [func AUGraphRemoveRenderNotify(AUGraph, AURenderCallback, UnsafeMutableRawPointer?) -> OSStatus](augraphremoverendernotify(_:_:_:).md)
  Removes a notification callback from an audio processing graph.
- [func AUGraphSetNodeInputCallback(AUGraph, AUNode, UInt32, UnsafePointer<AURenderCallbackStruct>) -> OSStatus](augraphsetnodeinputcallback(_:_:_:_:).md)
  Sets an input callback function for a node.
- [func AUGraphStart(AUGraph) -> OSStatus](augraphstart(_:).md)
  Starts an audio processing graph.
- [func AUGraphStop(AUGraph) -> OSStatus](augraphstop(_:).md)
  Stops an audio processing graph.
- [func AUGraphUninitialize(AUGraph) -> OSStatus](augraphuninitialize(_:).md)
  Uninitializes an audio processing graph.
- [func AUGraphUpdate(AUGraph, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](augraphupdate(_:_:).md)
  Updates the state of a running audio processing graph.
- [func DisposeAUGraph(AUGraph) -> OSStatus](disposeaugraph(_:).md)
  Disposes of an audio processing graph.
- [func NewAUGraph(UnsafeMutablePointer<AUGraph?>) -> OSStatus](newaugraph(_:).md)
  Creates a new audio processing graph.
### Data Types
- [struct AudioUnitNodeConnection](audiounitnodeconnection.md)
  A connection between two node objects in an audio processing graph.
- [typealias AUGraph](augraph.md)
  An opaque type representing an audio processing graph.
- [typealias AUNode](aunode.md)
  A member of an audio processing graph, associated with an audio unit.
- [struct AUNodeInteraction](aunodeinteraction.md)
  Describes the interaction between two node objects.
- [struct AUNodeRenderCallback](aunoderendercallback.md)
  A callback used to provide input to an audio unit.
### Constants
- [kAUNodeInteraction_Connection](1537633-kaunodeinteraction-connection.md)
  The different types of node interactions.
### Result Codes
- [var kAUGraphErr_NodeNotFound: OSStatus](kaugrapherr_nodenotfound.md)
  The specified node cannot be found.
- [var kAUGraphErr_InvalidConnection: OSStatus](kaugrapherr_invalidconnection.md)
  The attempted connection between two nodes cannot be made.
- [var kAUGraphErr_OutputNodeErr: OSStatus](kaugrapherr_outputnodeerr.md)
  Audio processing graphs can only contain one output unit. This error is returned if trying to add a second output unit or if the graph’s output unit is removed while the graph is running.
- [var kAUGraphErr_CannotDoInCurrentContext: OSStatus](kaugrapherr_cannotdoincurrentcontext.md)
  To avoid spinning or waiting in the render thread (a bad idea!), many of the calls to AUGraph can return: `kAUGraphErr_CannotDoInCurrentContext`. This result is only generated when you call an AUGraph API from its render callback. It means that the lock that it required was held at that time, by another thread. If you see this result code, you can generally attempt the action again - typically the NEXT render cycle (so in the mean time the lock can be cleared), or you can delegate that call to another thread in your app. You should not spin or put-to-sleep the render thread.
- [var kAUGraphErr_InvalidAudioUnit: OSStatus](kaugrapherr_invalidaudiounit.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-unit-processing-graph-services)*