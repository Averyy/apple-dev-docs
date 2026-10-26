---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/preparecheckpoint(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# prepareCheckpoint(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Normalize tensor names, values, and layer settings before loading the checkpoint. The default implementation calls [`sanitize(weights:metadata:)`](./sanitize%28weights,metadata%29.md).

## Declaration

```swift
func prepareCheckpoint(_ checkpoint: ModelCheckpoint) throws -> ModelCheckpoint
```

## Mentions

- [Model Compatibility](../model-compatibility.md)
- [Porting Models](../porting.md)

## Default Implementations

### BaseLanguageModel Implementations
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./preparecheckpoint%28_%29-zreu.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel/preparecheckpoint(_:))*