---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel/preparedrafterstate(target:prompttokens:targethidden:firstbonus:positiondeltas:state:sampler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# prepareDrafterState(target:promptTokens:targetHidden:firstBonus:positionDeltas:state:sampler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Prefill drafter-owned state from the target’s prompt hidden states.

## Declaration

```swift
func prepareDrafterState(target: any LanguageModel, promptTokens: MLXArray, targetHidden: MLXArray, firstBonus: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)
```

## Default Implementations

### StatefulMTPDrafterModel Implementations
- [func prepareDrafterState(target: any LanguageModel, promptTokens: MLXArray, targetHidden: MLXArray, firstBonus: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./preparedrafterstate%28target,prompttokens,targethidden,firstbonus,positiondeltas,state,sampler%29-6ezi9.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel/preparedrafterstate(target:prompttokens:targethidden:firstbonus:positiondeltas:state:sampler:))*