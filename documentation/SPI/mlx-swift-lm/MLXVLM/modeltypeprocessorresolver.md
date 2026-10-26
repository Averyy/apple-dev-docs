---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/modeltypeprocessorresolver"
framework: "mlx-swift-lm/MLXVLM"
---

# ModelTypeProcessorResolver

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

A reusable processor-type rule keyed by `model_type` from `config.json`.

## Declaration

```swift
struct ModelTypeProcessorResolver
```

## Topics

### Initializers
- [init(processorTypes: [String : String])](./modeltypeprocessorresolver/init%28processortypes%29.md)
### Instance Properties
- [let processorTypes: [String : String]](./modeltypeprocessorresolver/processortypes.md)
### Instance Methods
- [func processorType(for: VLMProcessorLoadingContext, declaredProcessorType: String?) throws -> String?](./modeltypeprocessorresolver/processortype%28for,declaredprocessortype%29.md)
### Default Implementations
- [VLMProcessorLoadingResolver Implementations](./modeltypeprocessorresolver/vlmprocessorloadingresolver-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- [VLMProcessorLoadingResolver](./vlmprocessorloadingresolver.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/modeltypeprocessorresolver)*