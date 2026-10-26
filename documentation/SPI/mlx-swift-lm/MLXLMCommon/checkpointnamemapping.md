---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/checkpointnamemapping"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CheckpointNameMapping

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Ordered module-path mappings shared by tensors and per-layer quantization settings.

## Declaration

```swift
struct CheckpointNameMapping
```

## Mentions

- [Model Compatibility](./model-compatibility.md)
- [Porting Models](./porting.md)

## Topics

### Initializers
- [init([Rule])](./checkpointnamemapping/init%28_%29.md)
  Prefixes are dot-separated module paths without a trailing dot. An empty replacement removes a wrapper; an empty source adds one.
### Instance Properties
- [let rules: [Rule]](./checkpointnamemapping/rules.md)
### Instance Methods
- [func mapName(String) -> String?](./checkpointnamemapping/mapname%28_%29.md)
### Enumerations
- [CheckpointNameMapping.Rule](./checkpointnamemapping/rule.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/checkpointnamemapping)*