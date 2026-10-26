---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/callasfunction(_:cache:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# callAsFunction(_:cache:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Models may implement this simplified interface if they do not produce any [`LMOutput.State`](../lmoutput/state-swift.struct.md)

## Declaration

```swift
func callAsFunction(_ inputs: MLXArray, cache: [KVCache]?) -> MLXArray
```

## Default Implementations

### LanguageModel Implementations
- [func callAsFunction(MLXArray, cache: [KVCache]?) -> MLXArray](./callasfunction%28_,cache%29-5zs1m.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/callasfunction(_:cache:))*