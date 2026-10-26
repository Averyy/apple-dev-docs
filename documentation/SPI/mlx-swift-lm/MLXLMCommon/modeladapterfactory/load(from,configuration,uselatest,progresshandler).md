---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapterfactory/load(from:configuration:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# load(from:configuration:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Loads a model adapter using a [`Downloader`](../downloader.md) and the provided model configuration.

## Declaration

```swift
func load(from downloader: any Downloader, configuration: ModelConfiguration, useLatest: Bool = false, progressHandler: @Sendable @escaping (Progress) -> Void = { _ in }) async throws -> ModelAdapter
```

#### Discussion

This method fetches the adapter configuration and weights, decodes the appropriate fine-tuning format, and initializes a `ModelAdapter` accordingly.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapterfactory/load(from:configuration:uselatest:progresshandler:))*