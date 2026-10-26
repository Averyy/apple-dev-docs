---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lmoutput"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LMOutput

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

[`LanguageModel`](./languagemodel.md) step output. This is consumed internally by the [`TokenIterator`](./tokeniterator.md).

## Declaration

```swift
struct LMOutput
```

## Topics

### Structures
- [LMOutput.Key](./lmoutput/key.md)
  typed key for use in [`LMOutput.State`](./lmoutput/state-swift.struct.md)
- [LMOutput.State](./lmoutput/state-swift.struct.md)
  Dictionary of typed [`LMOutput.Key`](./lmoutput/key.md) to carry state between steps.
### Initializers
- [init(logits: MLXArray, state: LMOutput.State?)](./lmoutput/init%28logits,state%29.md)
### Instance Properties
- [let logits: MLXArray](./lmoutput/logits.md)
  logits (one hot vector of probabilities for tokens)
- [let state: State?](./lmoutput/state-swift.property.md)
  optional [`LMOutput.State`](./lmoutput/state-swift.struct.md) to carry forward into the next step


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/lmoutput)*