---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapterfactory"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelAdapterFactory

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

A factory responsible for loading and creating model adapters from configurations.

## Declaration

```swift
final class ModelAdapterFactory
```

## Topics

### Initializers
- [init(registry: ModelAdapterTypeRegistry)](./modeladapterfactory/init%28registry%29.md)
### Instance Properties
- [let registry: ModelAdapterTypeRegistry](./modeladapterfactory/registry.md)
  Registry of adapter type creators.
### Instance Methods
- [func load(from: any Downloader, configuration: ModelConfiguration, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> ModelAdapter](./modeladapterfactory/load%28from,configuration,uselatest,progresshandler%29.md)
  Loads a model adapter using a [`Downloader`](./downloader.md) and the provided model configuration.
### Type Properties
- [static let shared: ModelAdapterFactory](./modeladapterfactory/shared.md)
  Shared instance of the adapter factory.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapterfactory)*