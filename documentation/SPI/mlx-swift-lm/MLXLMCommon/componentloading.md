---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/componentloading"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ComponentLoading

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

When a load reads the components that a model can load on first use.

## Declaration

```swift
enum ComponentLoading
```

## Topics

### Enumeration Cases
- [ComponentLoading.immediate](./componentloading/immediate.md)
  Load every component with the model, as model conversion needs.
- [ComponentLoading.onFirstUse](./componentloading/onfirstuse.md)
  Load each of [`onDemandComponents`](./modelcomponentsproviding/ondemandcomponents.md) the first time an input needs it, the way an `MLXArray` is computed only when it is evaluated. The checkpoint files must stay readable until then.
### Default Implementations
- [Equatable Implementations](./componentloading/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/componentloading)*