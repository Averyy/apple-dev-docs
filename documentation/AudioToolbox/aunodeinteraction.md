# AUNodeInteraction

**Framework**: Audio Toolbox  
**Kind**: struct

Describes the interaction between two node objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AUNodeInteraction
```

#### Overview

This structure contains information about the interaction between two nodes (in the case of a connection), or the input to a node (in the case of a callback).

The type of the interaction is used to determine how to interpret the contents of the following union.

There may be other nodal interactions in the future, so NO ASSUMPTIONS should be made that these are the only two nodal interaction types; you must always check the nodeInteractionType and only act on those types you understand.

Arrays of these structs can be returned, the addition of new members to the nodeInteraction union will NOT change the size of this structure.

## Topics

### Initializers
- [init()](aunodeinteraction/init.md)
- [init(nodeInteractionType: UInt32, nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction)](aunodeinteraction/init(nodeinteractiontype:nodeinteraction:).md)
### Instance Properties
- [var nodeInteraction: AUNodeInteraction.__Unnamed_union_nodeInteraction](aunodeinteraction/nodeinteraction.md)
  A union providing information about a node interaction.
- [var nodeInteractionType: UInt32](aunodeinteraction/nodeinteractiontype.md)
  The interaction type.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioUnitNodeConnection](audiounitnodeconnection.md)
  A connection between two node objects in an audio processing graph.
- [typealias AUGraph](augraph.md)
  An opaque type representing an audio processing graph.
- [typealias AUNode](aunode.md)
  A member of an audio processing graph, associated with an audio unit.
- [struct AUNodeRenderCallback](aunoderendercallback.md)
  A callback used to provide input to an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aunodeinteraction)*