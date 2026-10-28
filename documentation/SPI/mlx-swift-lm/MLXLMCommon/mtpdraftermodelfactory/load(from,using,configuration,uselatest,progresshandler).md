---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/load(from:using:configuration:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# load(from:using:configuration:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Load a model from a [`Downloader`](../downloader.md) and [`ModelConfiguration`](../modelconfiguration.md), producing a [`ModelContext`](../modelcontext.md).

## Declaration

```swift
func load(from downloader: any Downloader, using tokenizerLoader: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool = false, progressHandler: @Sendable @escaping (Progress) -> Void = { _ in }) async throws -> sending ContextType
```

## Discussion

This resolves the configuration (downloading remote sources via the downloader) and then loads the model from local files.

## See Also

### Related Documentation
- [func loadModel(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContext](../loadmodel%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model given a [`ModelConfiguration`](../modelconfiguration.md), downloading via a [`Downloader`](../downloader.md).
- [func loadModelContainer(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContainer](../loadmodelcontainer%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model given a [`ModelConfiguration`](../modelconfiguration.md), downloading via a [`Downloader`](../downloader.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/load(from:using:configuration:uselatest:progresshandler:))*