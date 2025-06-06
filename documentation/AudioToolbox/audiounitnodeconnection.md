# AudioUnitNodeConnection

**Framework**: Audio Toolbox  
**Kind**: struct

A connection between two node objects in an audio processing graph.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioUnitNodeConnection
```

## Topics

### Initializers
- [init()](audiounitnodeconnection/init.md)
- [init(sourceNode: AUNode, sourceOutputNumber: UInt32, destNode: AUNode, destInputNumber: UInt32)](audiounitnodeconnection/init(sourcenode:sourceoutputnumber:destnode:destinputnumber:).md)
### Instance Properties
- [var destInputNumber: UInt32](audiounitnodeconnection/destinputnumber.md)
- [var destNode: AUNode](audiounitnodeconnection/destnode.md)
- [var sourceNode: AUNode](audiounitnodeconnection/sourcenode.md)
- [var sourceOutputNumber: UInt32](audiounitnodeconnection/sourceoutputnumber.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias AUGraph](augraph.md)
  An opaque type representing an audio processing graph.
- [typealias AUNode](aunode.md)
  A member of an audio processing graph, associated with an audio unit.
- [struct AUNodeInteraction](aunodeinteraction.md)
  Describes the interaction between two node objects.
- [struct AUNodeRenderCallback](aunoderendercallback.md)
  A callback used to provide input to an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiounitnodeconnection)*