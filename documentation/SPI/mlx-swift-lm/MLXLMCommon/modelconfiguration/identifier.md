---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/identifier"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConfiguration.Identifier

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

The backing storage for the model’s location.

## Declaration

```swift
enum Identifier
```

## Topics

### Enumeration Cases
- [ModelConfiguration.Identifier.directory(_:)](./identifier/directory%28_%29.md)
  A file system URL pointing to a local model directory.
- [ModelConfiguration.Identifier.id(_:revision:)](./identifier/id%28_,revision%29.md)
  A Hugging Face Hub repository identifier (e.g., “BAAI/bge-small-en-v1.5”).
### Default Implementations
- [Equatable Implementations](./identifier/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconfiguration/identifier)*