---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/convert(configuration:to:options:progresshandler:)"
framework: "mlx-swift-lm/MLXLLM"
---

# convert(configuration:to:options:progressHandler:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Quantize and save a resolved local safetensors-backed LLM.

## Declaration

```swift
func convert(configuration: ResolvedModelConfiguration, to outputDirectory: URL, options: ModelConversionOptions = .init(), progressHandler: @Sendable @escaping (ModelConversionProgress) -> Void = { _ in }) async throws -> ModelConversionResult
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/convert(configuration:to:options:progresshandler:))*