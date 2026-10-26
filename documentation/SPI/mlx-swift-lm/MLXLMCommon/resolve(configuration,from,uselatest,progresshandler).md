---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolve(configuration:from:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# resolve(configuration:from:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Resolve a [`ModelConfiguration`](./modelconfiguration.md) into a [`ResolvedModelConfiguration`](./resolvedmodelconfiguration.md) by downloading remote sources via a [`Downloader`](./downloader.md).

## Declaration

```swift
func resolve(configuration: ModelConfiguration, from downloader: any Downloader, useLatest: Bool, progressHandler: @Sendable @escaping (Progress) -> Void) async throws -> ResolvedModelConfiguration
```

#### Discussion

This handles the `.id` vs `.directory` switch for the model source and resolves [`TokenizerSource`](./tokenizersource.md) for the tokenizer.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/resolve(configuration:from:uselatest:progresshandler:))*