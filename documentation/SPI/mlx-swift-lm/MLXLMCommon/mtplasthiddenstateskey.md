---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtplasthiddenstateskey"
framework: "mlx-swift-lm/MLXLMCommon"
---

# mtpLastHiddenStatesKey

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: var  
**Role**: Global Variable

Target writes the hidden representation required by its MTP head here. This is architecture-specific, but must match the representation used to train the paired MTP head. Qwen and Gemma assistants both publish their post-final-norm representation. The iterator threads it to the drafter unchanged as `lastHidden`.

## Declaration

```swift
let mtpLastHiddenStatesKey: LMOutput.Key<MLXArray>
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtplasthiddenstateskey)*