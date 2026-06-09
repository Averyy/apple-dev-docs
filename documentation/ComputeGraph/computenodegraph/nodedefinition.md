# ComputeNodeGraph.NodeDefinition

**Framework**: ComputeGraph  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
struct NodeDefinition
```

## Topics

### Initializers
- [init(name: String, bundle: String?, inputs: [ComputeNodeGraph.PortDefinition], outputs: [ComputeNodeGraph.PortDefinition], kind: ComputeNodeGraph.NodeDefinition.Kind)](computenodegraph/nodedefinition/init(name:bundle:inputs:outputs:kind:).md)
### Instance Properties
- [var bundle: String?](computenodegraph/nodedefinition/bundle.md)
- [var inputs: [ComputeNodeGraph.PortDefinition]](computenodegraph/nodedefinition/inputs.md)
- [var kind: ComputeNodeGraph.NodeDefinition.Kind](computenodegraph/nodedefinition/kind-swift.property.md)
- [var name: String](computenodegraph/nodedefinition/name.md)
  Name of the NodeDefinition.
- [var outputs: [ComputeNodeGraph.PortDefinition]](computenodegraph/nodedefinition/outputs.md)
### Type Methods
- [static func stage(ComputeNodeGraph.Stage) -> ComputeNodeGraph.NodeDefinition?](computenodegraph/nodedefinition/stage(_:).md)
### Enumerations
- [ComputeNodeGraph.NodeDefinition.Kind](computenodegraph/nodedefinition/kind-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/nodedefinition)*