---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils/tune(input:context:parameters:resetpeakmemory:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# tune(input:context:parameters:resetPeakMemory:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Measure weights, KV cache, and prefill workspace using a prepared input.

## Declaration

```swift
static func tune(input: LMInput, context: ModelContext, parameters: GenerateParameters, resetPeakMemory: Bool = true) async throws -> WiredMemoryMeasurement
```

#### Return Value

A measurement snapshot for weights, KV, and workspace.

#### Discussion

This overload is recommended for multimodal models because it accepts a fully prepared `LMInput` (e.g. with image/video tensors already embedded).

## Parameters

- `input`: Prepared model input from the model’s processor.
- `context`: The loaded model context.
- `parameters`: Generation parameters that control prefill behavior.
- `resetPeakMemory`: If true, resets `Memory.peakMemory` before measuring.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils/tune(input:context:parameters:resetpeakmemory:))*