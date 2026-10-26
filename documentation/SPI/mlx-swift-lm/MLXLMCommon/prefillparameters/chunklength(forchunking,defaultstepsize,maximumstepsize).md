---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunklength(forchunking:defaultstepsize:maximumstepsize:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# chunkLength(forChunking:defaultStepSize:maximumStepSize:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

The per-forward chunk length for prefilling `count` positions, or `nil` when the prompt should go through in a single forward ([`PrefillParameters.Chunking.unchunked`](./chunking-swift.enum/unchunked.md)).

## Declaration

```swift
func chunkLength(forChunking count: Int, defaultStepSize: Int = PrefillParameters.defaultStepSize, maximumStepSize: Int? = nil) -> Int?
```

#### Discussion

`count` is the number of positions the caller intends to chunk — excluding any tail it reserves for the first sampled forward. Models pass their own `defaultStepSize` (used when [`stepSize`](./stepsize.md) is `nil`) and, if they have one, a `maximumStepSize` cap such as a sliding-window size.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/prefillparameters/chunklength(forchunking:defaultstepsize:maximumstepsize:))*