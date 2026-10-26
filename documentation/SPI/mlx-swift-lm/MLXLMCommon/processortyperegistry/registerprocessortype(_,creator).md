---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/processortyperegistry/registerprocessortype(_:creator:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# registerProcessorType(_:creator:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Add a new model to the type registry.

## Declaration

```swift
func registerProcessorType(_ type: String, creator: @escaping (Data, any Tokenizer) throws -> any UserInputProcessor)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/processortyperegistry/registerprocessortype(_:creator:))*