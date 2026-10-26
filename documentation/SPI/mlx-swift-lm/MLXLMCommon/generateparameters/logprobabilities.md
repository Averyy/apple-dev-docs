---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/logprobabilities"
framework: "mlx-swift-lm/MLXLMCommon"
---

# logProbabilities

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Per-token log-probability reporting. `nil` disables reporting; `0` reports the selected token only, and a positive value also reports that many top tokens. Use [`LogProbabilityTokenLoopHandler`](../logprobabilitytokenloophandler.md) to emit these values through a custom generation loop. Only [`TokenIterator`](../tokeniterator.md) reports them; speculative iterators ignore this setting.

## Declaration

```swift
var logProbabilities: Int?
```

## Mentions

- [Observing token log probabilities](../generation-observability.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/logprobabilities)*