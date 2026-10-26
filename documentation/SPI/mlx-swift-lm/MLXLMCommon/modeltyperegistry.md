---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelTypeRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

## Declaration

```swift
actor ModelTypeRegistry<T>
```

## Topics

### Initializers
- [init()](./modeltyperegistry/init%28%29.md)
  Creates an empty registry.
- [init(creators: [String : (Data) throws -> T])](./modeltyperegistry/init%28creators%29.md)
  Creates a registry with given creators.
### Instance Methods
- [func contains(String) -> Bool](./modeltyperegistry/contains%28_%29.md)
  Whether a creator is registered for `modelType` — i.e. this registry can instantiate that architecture. Lets a caller check support without attempting a (throwing, allocating) `createModel`, e.g. to decide before a multi-GB download whether a Hub repo’s `model_type` is runnable.
- [func createModel(configuration: Data, modelType: String) throws -> sending T](./modeltyperegistry/createmodel%28configuration,modeltype%29.md)
  Given a `modelType` and configuration data instantiate a new `LanguageModel`.
- [func loraMetadata(configurationData: Data) throws -> LoRAModelMetadata?](./modeltyperegistry/lorametadata%28configurationdata%29.md)
  Inspects the registered model’s LoRA layers without loading checkpoint weights.
- [func registerModelType(String, creator: (Data) throws -> T)](./modeltyperegistry/registermodeltype%28_,creator%29.md)
  Add a new model to the type registry.
- [func registerModelType(String, matches: (Data) -> Bool, creator: (Data) throws -> T)](./modeltyperegistry/registermodeltype%28_,matches,creator%29.md)
  Add a new model to the type registry with a predicate for ambiguous `model_type` strings shared by multiple package targets.
### Default Implementations
- [Actor Implementations](./modeltyperegistry/actor-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.Actor


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modeltyperegistry)*