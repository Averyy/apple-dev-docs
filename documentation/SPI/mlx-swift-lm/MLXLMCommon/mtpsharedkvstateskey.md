---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpsharedkvstateskey"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mtpSharedKVStatesKey

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: var  
**Role**: Global Variable

Target writes one `(keys, values)` tuple per `layer_type` (`"full_attention"`, `"sliding_attention"`) here, drawn from the last layer of each type. [`MTPSpeculativeTokenIterator`](./mtpspeculativetokeniterator.md) reads it and threads it to the drafter as `sharedKV`.

## Declaration

```swift
let mtpSharedKVStatesKey: LMOutput.Key<[String : (MLXArray, MLXArray)]>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpsharedkvstateskey)*