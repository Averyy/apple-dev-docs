---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils/tune(context:tokencount:parameters:seedtext:resetpeakmemory:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# tune(context:tokenCount:parameters:seedText:resetPeakMemory:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Measure weights, KV cache, and prefill workspace for the given model context.

## Declaration

```swift
static func tune(context: ModelContext, tokenCount: Int, parameters: GenerateParameters, seedText: String = " hello", resetPeakMemory: Bool = true) async throws -> WiredMemoryMeasurement
```

#### Discussion

This is a diagnostic helper intended to **measure** real memory usage rather than assume it. The returned values are best used to construct a ticket budget or to compare against manual estimates.

> ❗ **Important**: `Memory.peakMemory` is global. For accurate results, run this in isolation (no concurrent inference).

> **Note**: This uses the tokenizer directly to build a synthetic prompt and is best suited for text-only models. For multimodal models, use the overload that accepts a prepared `LMInput`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils/tune(context:tokencount:parameters:seedtext:resetpeakmemory:))*