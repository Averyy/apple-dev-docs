# ShaderGraph.Edge

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

Represents a connection between two nodes in a shader graph.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Edge
```

## Topics

### Initializers
- [init(outputNode: String, outputPort: String?, inputNode: String, inputPort: String)](./edge/init%28outputnode,outputport,inputnode,inputport%29.md)
### Instance Properties
- [var from: String](./edge/from.md)
- [var inputNode: String](./edge/inputnode.md)
  The name of the node receiving the input value.
- [var inputPort: String](./edge/inputport.md)
  The name of the input port on the destination node.
- [var outputNode: String](./edge/outputnode.md)
  The name of the node providing the output value.
- [var outputPort: String?](./edge/outputport.md)
  The name of the output port on the source node.
- [var to: String](./edge/to.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/shadergraph/edge)*