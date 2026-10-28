---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/nexttokenlogits(_:cache:state:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# nextTokenLogits(_:cache:state:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Evaluate all input positions when only the final position’s logits are needed.

## Declaration

```swift
func nextTokenLogits(_ input: LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput
```

## Discussion

Implementations may omit earlier logit rows, but must preserve cache updates and output state. The default uses the regular forward. Scoring and speculative verification must use the regular forward when they need multiple positions.

## Default Implementations

### LanguageModel Implementations
- [func nextTokenLogits(LMInput.Text, cache: [KVCache]?, state: LMOutput.State?) -> LMOutput](./nexttokenlogits%28_,cache,state%29-69jug.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/languagemodel/nexttokenlogits(_:cache:state:))*