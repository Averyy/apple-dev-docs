---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodel(from:using:configuration:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadModel(from:using:configuration:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a model given a [`ModelConfiguration`](./modelconfiguration.md), downloading via a [`Downloader`](./downloader.md).

## Declaration

```swift
func loadModel(from downloader: any Downloader, using tokenizerLoader: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool = false, progressHandler: @Sendable @escaping (Progress) -> Void = { _ in }) async throws -> sending ModelContext
```

#### Return Value

A [`ModelContext`](./modelcontext.md)

#### Discussion

Returns a [`ModelContext`](./modelcontext.md) holding the model and tokenizer without an `actor` providing an isolation context.

## Parameters

- `downloader`: The [`Downloader`](./downloader.md) to use for fetching remote resources
- `tokenizerLoader`: The [`TokenizerLoader`](./tokenizerloader.md) to use for loading the tokenizer
- `configuration`: A [`ModelConfiguration`](./modelconfiguration.md)
- `useLatest`: When true, always checks the provider for the latest version
- `progressHandler`: Optional callback for progress


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodel(from:using:configuration:uselatest:progresshandler:))*