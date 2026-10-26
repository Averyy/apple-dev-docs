---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapterfactory/registry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# registry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Registry of adapter type creators.

## Declaration

```swift
let registry: ModelAdapterTypeRegistry
```

#### Discussion

You can register custom adapter types as follows:

```swift
let registry = ModelAdapterFactory.shared.registry
let adapterType = "my-adapter"
let adapterCreator = MyAdapterContainer.from(directory:)
registry.registerAdapterType(adapterType, creator: adapterCreator)
```

This allows the factory to load your custom adapter from automatically when the matching type is found in a configuration file.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeladapterfactory/registry)*