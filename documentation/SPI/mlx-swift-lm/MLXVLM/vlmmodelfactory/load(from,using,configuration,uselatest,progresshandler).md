---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmmodelfactory/load(from:using:configuration:uselatest:progresshandler:)"
framework: "mlx-swift-lm/MLXVLM"
---

# load(from:using:configuration:useLatest:progressHandler:)

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: method  
**Role**: Instance Method

Inherited from `GenericModelFactory.load(from:using:configuration:useLatest:progressHandler:)`.

## Declaration

```swift
func load(from downloader: any Downloader, using tokenizerLoader: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool = false, progressHandler: @escaping @Sendable (Progress) -> Void = { _ in }) async throws -> sending Self.ContextType
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmmodelfactory/load(from:using:configuration:uselatest:progresshandler:))*