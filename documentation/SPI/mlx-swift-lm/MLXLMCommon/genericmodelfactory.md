---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/genericmodelfactory"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenericModelFactory

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for code that can load models.

## Declaration

```swift
protocol GenericModelFactory<ContextType, ContainerType> : Sendable
```

## Overview

See concrete implementations in:

- `LLMModelFactory`
- `VLMModelFactory`
- `EmbedderModelFactory`

or, if loading LLM/VLMs, use the free functions:

- [`loadModel(from:using:configuration:useLatest:progressHandler:)`](./loadmodel%28from,using,configuration,uselatest,progresshandler%29.md)
- [`loadModelContainer(from:using:configuration:useLatest:progressHandler:)`](./loadmodelcontainer%28from,using,configuration,uselatest,progresshandler%29.md)

or variants.

## Topics

### Associated Types
- [associatedtype ContainerType : Sendable](./genericmodelfactory/containertype.md)
- [associatedtype ContextType](./genericmodelfactory/contexttype.md)
### Instance Properties
- [var modelRegistry: AbstractModelRegistry](./genericmodelfactory/modelregistry.md)
### Instance Methods
- [func configuration(id: String) -> ModelConfiguration](./genericmodelfactory/configuration%28id%29.md)
  Resolve a model identifier, e.g. “mlx-community/Llama-3.2-3B-Instruct-4bit”, into a [`ModelConfiguration`](./modelconfiguration.md).
- [func contains(id: String) -> Bool](./genericmodelfactory/contains%28id%29.md)
  Returns true if [`modelRegistry`](./genericmodelfactory/modelregistry.md) contains a model with the id. Otherwise, false.
- [func load(from: URL, using: any TokenizerLoader) async throws -> sending ContextType](./genericmodelfactory/load%28from,using%29.md)
  Load a model from a local directory, producing a [`ModelContext`](./modelcontext.md).
- [func load(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ContextType](./genericmodelfactory/load%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model from a [`Downloader`](./downloader.md) and [`ModelConfiguration`](./modelconfiguration.md), producing a [`ModelContext`](./modelcontext.md).
- [func loadContainer(from: URL, using: any TokenizerLoader) async throws -> ContainerType](./genericmodelfactory/loadcontainer%28from,using%29.md)
  Load a model from a local directory, producing a [`ModelContainer`](./modelcontainer.md).
- [func loadContainer(from: any Downloader, using: any TokenizerLoader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> ContainerType](./genericmodelfactory/loadcontainer%28from,using,configuration,uselatest,progresshandler%29.md)
  Load a model from a [`Downloader`](./downloader.md) and [`ModelConfiguration`](./modelconfiguration.md), producing a [`ModelContainer`](./modelcontainer.md).

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [MTPDrafterModelFactory](./mtpdraftermodelfactory.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/genericmodelfactory)*