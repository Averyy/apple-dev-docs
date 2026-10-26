---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/checkpointcomponent"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CheckpointComponent

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A checkpoint component’s serialized namespaces and runtime destination.

## Declaration

```swift
struct CheckpointComponent
```

## Mentions

- [Model Compatibility](./model-compatibility.md)
- [Porting Models](./porting.md)

## Topics

### Structures
- [CheckpointComponent.Selection](./checkpointcomponent/selection.md)
### Initializers
- [init(name: String, namespaces: [String], destination: String, excludedNamespaces: [String])](./checkpointcomponent/init%28name,namespaces,destination,excludednamespaces%29.md)
### Instance Properties
- [let destination: String](./checkpointcomponent/destination.md)
- [let excludedNamespaces: [String]](./checkpointcomponent/excludednamespaces.md)
- [let name: String](./checkpointcomponent/name.md)
- [let namespaces: [String]](./checkpointcomponent/namespaces.md)
### Instance Methods
- [func excluding(from: ModelCheckpoint) throws -> ModelCheckpoint](./checkpointcomponent/excluding%28from%29.md)
  Exclude this component when loading a sibling, including its layer settings.
- [func select(from: ModelCheckpoint, standalone: Bool) throws -> Selection](./checkpointcomponent/select%28from,standalone%29.md)
  Resolve one embedded namespace, or a root component explicitly declared by the caller. Unknown paths remain in the result for strict model validation.
### Enumerations
- [CheckpointComponent.SelectionError](./checkpointcomponent/selectionerror.md)
- [CheckpointComponent.Source](./checkpointcomponent/source.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/checkpointcomponent)*