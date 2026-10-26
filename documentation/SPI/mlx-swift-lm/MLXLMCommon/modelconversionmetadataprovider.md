---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionmetadataprovider"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionMetadataProvider

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Optional metadata a model wants written into converted safetensors.

## Declaration

```swift
protocol ModelConversionMetadataProvider
```

#### Overview

Model-specific metadata lets future loaders distinguish transformed MLX-native checkpoints from original upstream checkpoints without relying only on tensor shapes.

## Topics

### Instance Properties
- [var modelConversionMetadata: [String : String]](./modelconversionmetadataprovider/modelconversionmetadata.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionmetadataprovider)*