---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel/commitdrafterstate(target:targethidden:drafttokens:acceptedcount:finaltoken:positiondeltas:state:sampler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# commitDrafterState(target:targetHidden:draftTokens:acceptedCount:finalToken:positionDeltas:state:sampler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Reconcile tentative proposal writes with the sequence accepted by the target, then seed the next proposal if the architecture supports it.

## Declaration

```swift
func commitDrafterState(target: any LanguageModel, targetHidden: MLXArray, draftTokens: MLXArray, acceptedCount: Int, finalToken: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)
```

## Default Implementations

### StatefulMTPDrafterModel Implementations
- [func commitDrafterState(target: any LanguageModel, targetHidden: MLXArray, draftTokens: MLXArray, acceptedCount: Int, finalToken: MLXArray, positionDeltas: MLXArray?, state: inout MTPDrafterState, sampler: any LogitSampler)](./commitdrafterstate%28target,targethidden,drafttokens,acceptedcount,finaltoken,positiondeltas,state,sampler%29-2nuad.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/statefulmtpdraftermodel/commitdrafterstate(target:targethidden:drafttokens:acceptedcount:finaltoken:positiondeltas:state:sampler:))*