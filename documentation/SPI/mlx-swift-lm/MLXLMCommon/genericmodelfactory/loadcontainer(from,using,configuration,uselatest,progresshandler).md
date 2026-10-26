---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/genericmodelfactory/loadcontainer(from:using:configuration:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# loadContainer(from:using:configuration:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Load a model from a [`Downloader`](../downloader.md) and [`ModelConfiguration`](../modelconfiguration.md), producing a [`ModelContainer`](../modelcontainer.md).

## Declaration

```swift
func loadContainer(from downloader: any Downloader, using tokenizerLoader: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool = false, progressHandler: @Sendable @escaping (Progress) -> Void = { _ in }) async throws -> ContainerType
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/genericmodelfactory/loadcontainer(from:using:configuration:uselatest:progresshandler:))*