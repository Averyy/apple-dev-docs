---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpsharedkvoffsetskey"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mtpSharedKVOffsetsKey

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: var  
**Role**: Global Variable

Target writes the absolute cache offset for each emitted shared-K/V layer-type here. The K/V tensors themselves may have a capped sequence axis when backed by a rotating cache, so their shape is not always the absolute RoPE/query position.

## Declaration

```swift
let mtpSharedKVOffsetsKey: LMOutput.Key<[String : Int]>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpsharedkvoffsetskey)*