---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingcontext"
framework: "mlx-swift-lm/MLXVLM"
---

# VLMProcessorLoadingContext

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: struct  
**Role**: Structure

The model metadata available while resolving how to load a VLM processor.

## Declaration

```swift
struct VLMProcessorLoadingContext
```

#### Overview

External model packages can decode [`configurationData`](./vlmprocessorloadingcontext/configurationdata.md) into their own model configuration type without introducing a dependency from MLXVLM back to that package.

## Topics

### Initializers
- [init(modelId: String, modelType: String, configurationData: Data)](./vlmprocessorloadingcontext/init%28modelid,modeltype,configurationdata%29.md)
### Instance Properties
- [let configurationData: Data](./vlmprocessorloadingcontext/configurationdata.md)
- [let modelId: String](./vlmprocessorloadingcontext/modelid.md)
- [let modelType: String](./vlmprocessorloadingcontext/modeltype.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmprocessorloadingcontext)*