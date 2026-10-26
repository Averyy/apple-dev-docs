---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodelcontainer(from:using:id:revision:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadModelContainer(from:using:id:revision:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Load a model given a model identifier, downloading via a [`Downloader`](./downloader.md).

## Declaration

```swift
func loadModelContainer(from downloader: any Downloader, using tokenizerLoader: any TokenizerLoader, id: String, revision: String = "main", useLatest: Bool = false, progressHandler: @Sendable @escaping (Progress) -> Void = { _ in }) async throws -> sending ModelContainer
```

#### Return Value

A [`ModelContainer`](./modelcontainer.md)

#### Discussion

Returns a [`ModelContainer`](./modelcontainer.md) holding a [`ModelContext`](./modelcontext.md) inside an actor providing isolation control for the values.

## Parameters

- `downloader`: The [`Downloader`](./downloader.md) to use for fetching remote resources
- `tokenizerLoader`: The [`TokenizerLoader`](./tokenizerloader.md) to use for loading the tokenizer
- `id`: Model identifier, e.g “mlx-community/Qwen3-4B-4bit”
- `revision`: Revision to download (defaults to “main”)
- `useLatest`: When true, always checks the provider for the latest version
- `progressHandler`: Optional callback for progress


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loadmodelcontainer(from:using:id:revision:uselatest:progresshandler:))*