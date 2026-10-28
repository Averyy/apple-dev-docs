---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodel(from:using:id:revision:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadModel(from:using:id:revision:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a model given a model identifier, downloading via a [`Downloader`](./downloader.md).

## Declaration

```swift
func loadModel(from downloader: any Downloader, using tokenizerLoader: any TokenizerLoader, id: String, revision: String = "main", useLatest: Bool = false, progressHandler: @Sendable @escaping (Progress) -> Void = { _ in }) async throws -> sending ModelContext
```

## Return Value

A [`ModelContext`](./modelcontext.md)

## Discussion

Returns a [`ModelContext`](./modelcontext.md) holding the model and tokenizer without an `actor` providing an isolation context.

## Parameters

- `downloader`: The [`Downloader`](./downloader.md) to use for fetching remote resources
- `tokenizerLoader`: The [`TokenizerLoader`](./tokenizerloader.md) to use for loading the tokenizer
- `id`: Model identifier, e.g “mlx-community/Qwen3-4B-4bit”
- `revision`: Revision to download (defaults to “main”)
- `useLatest`: When true, always checks the provider for the latest version
- `progressHandler`: Optional callback for progress


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodel(from:using:id:revision:uselatest:progresshandler:))*