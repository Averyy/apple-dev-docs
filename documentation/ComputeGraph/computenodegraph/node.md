# ComputeNodeGraph.Node

**Framework**: Compute Graph  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
struct Node
```

## Topics

### Initializers
- [init(definition: ComputeNodeGraph.NodeDefinition, label: String?)](computenodegraph/node/init(definition:label:).md)
### Instance Properties
- [var definition: ComputeNodeGraph.NodeDefinition](computenodegraph/node/definition.md)
- [var kind: ComputeNodeGraph.Node.Kind](computenodegraph/node/kind-swift.property.md)
  Type of the node
- [var label: String?](computenodegraph/node/label.md)
  Optional user-provided label for the node
- [var metadata: ComputeNodeGraph.Metadata?](computenodegraph/node/metadata.md)
  Node metadata – data which is not needed during compilation but might be useful at edit time.
- [var uniforms: [Data?]](computenodegraph/node/uniforms.md)
  Uniform values for the node.
### Instance Methods
- [func input<V>(at: Int) -> V?](computenodegraph/node/input(at:).md)
- [func input<V>(named: String) -> V?](computenodegraph/node/input(named:).md)
- [func inputData(named: String) -> Data?](computenodegraph/node/inputdata(named:).md)
- [func setInput(String, String) -> Bool](computenodegraph/node/setinput(_:_:)-2ittk.md)
- [func setInput(String, Data) -> Bool](computenodegraph/node/setinput(_:_:)-35srn.md)
- [func setInput(String, Bool) -> Bool](computenodegraph/node/setinput(_:_:)-3yk57.md)
- [func setInput<V>(String, V) -> Bool](computenodegraph/node/setinput(_:_:)-9n5yb.md)
- [func setInput<V>(at: Int, V)](computenodegraph/node/setinput(at:_:)-95j9n.md)
- [func setInput(at: Int, Data?)](computenodegraph/node/setinput(at:_:)-9xg3z.md)
### Enumerations
- [ComputeNodeGraph.Node.Kind](computenodegraph/node/kind-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/node)*