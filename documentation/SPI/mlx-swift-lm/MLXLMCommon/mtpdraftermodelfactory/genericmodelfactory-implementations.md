---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/genericmodelfactory-implementations"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenericModelFactory Implementations

**Framework**: mlx-swift-lm/MLXLMCommon  
**Role**: API Collection

## Topics

### Instance Methods
- [func configuration(id: String) -> ModelConfiguration](./configuration%28id%29.md)
  Resolve a model identifier, e.g. “mlx-community/Llama-3.2-3B-Instruct-4bit”, into a [`ModelConfiguration`](../modelconfiguration.md).
- [func contains(id: String) -> Bool](./contains%28id%29.md)
  Returns true if [`modelRegistry`](./modelregistry.md) contains a model with the id. Otherwise, false.
- [func load(from: URL, using: any TokenizerLoader) async throws -> sending ContextType](./load%28from,using%29.md)
  Load a model from a local directory, producing a [`ModelContext`](../modelcontext.md).
- [func load(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ContextType](./load%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model from a [`Downloader`](../downloader.md) and [`ModelConfiguration`](../modelconfiguration.md), producing a [`ModelContext`](../modelcontext.md).
- [func loadContainer(from: URL, using: any TokenizerLoader) async throws -> ContainerType](./loadcontainer%28from,using%29.md)
  Load a model from a local directory, producing a [`ModelContainer`](../modelcontainer.md).
- [func loadContainer(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> ContainerType](./loadcontainer%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model from a [`Downloader`](../downloader.md) and [`ModelConfiguration`](../modelconfiguration.md), producing a [`ModelContainer`](../modelcontainer.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/mtpdraftermodelfactory/genericmodelfactory-implementations)*