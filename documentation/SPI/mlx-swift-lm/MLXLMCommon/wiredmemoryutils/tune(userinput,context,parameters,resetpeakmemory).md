---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils/tune(userinput:context:parameters:resetpeakmemory:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# tune(userInput:context:parameters:resetPeakMemory:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Measure weights, KV cache, and prefill workspace using a user input.

## Declaration

```swift
static func tune(userInput: UserInput, context: ModelContext, parameters: GenerateParameters, resetPeakMemory: Bool = true) async throws -> WiredMemoryMeasurement
```

#### Return Value

A measurement snapshot for weights, KV, and workspace.

#### Discussion

This is a convenience wrapper that runs the model’s processor to build a prepared `LMInput`, then delegates to the `tune(input:context:parameters:)` overload. It is especially useful for VLMs where images or videos are part of the input and significantly affect memory usage.

## Parameters

- `userInput`: High-level input (text/images/video) to be prepared.
- `context`: The loaded model context.
- `parameters`: Generation parameters that control prefill behavior.
- `resetPeakMemory`: If true, resets `Memory.peakMemory` before measuring.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils/tune(userinput:context:parameters:resetpeakmemory:))*