---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/convert(from:configuration:to:options:uselatest:downloadprogresshandler:progresshandler:)"
framework: "mlx-swift-lm/MLXLLM"
---

# convert(from:configuration:to:options:useLatest:downloadProgressHandler:progressHandler:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Download, quantize, and save a safetensors-backed LLM.

## Declaration

```swift
func convert(from downloader: any Downloader, configuration: ModelConfiguration, to outputDirectory: URL, options: ModelConversionOptions = .init(), useLatest: Bool = false, downloadProgressHandler: @Sendable @escaping (Progress) -> Void = { _ in }, progressHandler: @Sendable @escaping (ModelConversionProgress) -> Void = { _ in }) async throws -> ModelConversionResult
```

#### Discussion

This is the Swift equivalent of the common `mlx_lm.convert` workflow for models that are available as compatible safetensors. PyTorch `.bin` conversion is intentionally out of scope.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/convert(from:configuration:to:options:uselatest:downloadprogresshandler:progresshandler:))*