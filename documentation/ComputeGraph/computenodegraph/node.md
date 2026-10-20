# ComputeNodeGraph.Node

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct Node
```

## Topics

### Initializers
- [init(definition: ComputeNodeGraph.NodeDefinition, label: String?)](./node/init%28definition,label%29.md)
### Instance Properties
- [var definition: ComputeNodeGraph.NodeDefinition](./node/definition.md)
- [var kind: ComputeNodeGraph.Node.Kind](./node/kind-swift.property.md)
  Type of the node
- [var label: String?](./node/label.md)
  Optional user-provided label for the node
- [var metadata: ComputeNodeGraph.Metadata?](./node/metadata.md)
  Node metadata – data which is not needed during compilation but might be useful at edit time.
- [var uniforms: [Data?]](./node/uniforms.md)
  Uniform values for the node.
### Instance Methods
- [func input<V>(at: Int) -> V?](./node/input%28at%29.md)
- [func input<V>(named: String) -> V?](./node/input%28named%29.md)
- [func inputData(named: String) -> Data?](./node/inputdata%28named%29.md)
- [func setInput(String, String) -> Bool](./node/setinput%28_,_%29-2ittk.md)
- [func setInput(String, Data) -> Bool](./node/setinput%28_,_%29-35srn.md)
- [func setInput(String, Bool) -> Bool](./node/setinput%28_,_%29-3yk57.md)
- [func setInput<V>(String, V) -> Bool](./node/setinput%28_,_%29-9n5yb.md)
- [func setInput<V>(at: Int, V)](./node/setinput%28at,_%29-95j9n.md)
- [func setInput(at: Int, Data?)](./node/setinput%28at,_%29-9xg3z.md)
### Enumerations
- [ComputeNodeGraph.Node.Kind](./node/kind-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/node)*