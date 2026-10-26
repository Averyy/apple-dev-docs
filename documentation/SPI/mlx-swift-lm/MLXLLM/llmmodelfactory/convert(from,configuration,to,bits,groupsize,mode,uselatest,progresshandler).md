---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/convert(from:configuration:to:bits:groupsize:mode:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLLM"
---

# convert(from:configuration:to:bits:groupSize:mode:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLLM  
**Kind**: method  
**Role**: Instance Method

Download, quantize, and save a safetensors-backed LLM.

## Declaration

```swift
func convert(from downloader: any Downloader, configuration: ModelConfiguration, to outputDirectory: URL, bits: Int? = nil, groupSize: Int? = nil, mode: QuantizationMode = .affine, useLatest: Bool = false, progressHandler: @Sendable @escaping (Progress) -> Void = { _ in }) async throws -> ModelConversionResult
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxllm/llmmodelfactory/convert(from:configuration:to:bits:groupsize:mode:uselatest:progresshandler:))*