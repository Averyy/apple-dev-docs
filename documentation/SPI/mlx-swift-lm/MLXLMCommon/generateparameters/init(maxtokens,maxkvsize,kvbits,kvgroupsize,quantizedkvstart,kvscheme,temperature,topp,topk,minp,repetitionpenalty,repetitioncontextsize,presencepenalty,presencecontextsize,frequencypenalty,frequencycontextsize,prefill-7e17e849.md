---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/init(maxtokens:maxkvsize:kvbits:kvgroupsize:quantizedkvstart:kvscheme:temperature:topp:topk:minp:repetitionpenalty:repetitioncontextsize:presencepenalty:presencecontextsize:frequencypenalty:frequencycontextsize:prefillstepsize:seed:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# init(maxTokens:maxKVSize:kvBits:kvGroupSize:quantizedKVStart:kvScheme:temperature:topP:topK:minP:repetitionPenalty:repetitionContextSize:presencePenalty:presenceContextSize:frequencyPenalty:frequencyContextSize:prefillStepSize:seed:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: init  
**Role**: Initializer

> **Deprecated**: prefill now defaults to balanced chunking; use prefill.chunking = .remainder for the legacy chunk boundaries

## Declaration

```swift
init(maxTokens: Int? = nil, maxKVSize: Int? = nil, kvBits: Int? = nil, kvGroupSize: Int = 64, quantizedKVStart: Int = 0, kvScheme: String? = nil, temperature: Float = 0.6, topP: Float = 1.0, topK: Int = 0, minP: Float = 0.0, repetitionPenalty: Float? = nil, repetitionContextSize: Int = 20, presencePenalty: Float? = nil, presenceContextSize: Int = 20, frequencyPenalty: Float? = nil, frequencyContextSize: Int = 20, prefillStepSize: Int?, seed: UInt64? = nil)
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/init(maxtokens:maxkvsize:kvbits:kvgroupsize:quantizedkvstart:kvscheme:temperature:topp:topk:minp:repetitionpenalty:repetitioncontextsize:presencepenalty:presencecontextsize:frequencypenalty:frequencycontextsize:prefillstepsize:seed:))*