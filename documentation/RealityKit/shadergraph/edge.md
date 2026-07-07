# ShaderGraph.Edge

**Framework**: RealityKit  
**Kind**: struct

Represents a connection between two nodes in a shader graph.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Edge
```

## Topics

### Initializers
- [init(outputNode: String, outputPort: String?, inputNode: String, inputPort: String)](shadergraph/edge/init(outputnode:outputport:inputnode:inputport:).md)
### Instance Properties
- [var from: String](shadergraph/edge/from.md)
- [var inputNode: String](shadergraph/edge/inputnode.md)
  The name of the node receiving the input value.
- [var inputPort: String](shadergraph/edge/inputport.md)
  The name of the input port on the destination node.
- [var outputNode: String](shadergraph/edge/outputnode.md)
  The name of the node providing the output value.
- [var outputPort: String?](shadergraph/edge/outputport.md)
  The name of the output port on the source node.
- [var to: String](shadergraph/edge/to.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/edge)*