---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/processortyperegistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ProcessorTypeRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

## Declaration

```swift
actor ProcessorTypeRegistry
```

## Topics

### Initializers
- [init()](./processortyperegistry/init%28%29.md)
  Creates an empty registry.
- [init(creators: [String : (Data, any Tokenizer) throws -> any UserInputProcessor])](./processortyperegistry/init%28creators%29.md)
  Creates a registry with given creators.
### Instance Methods
- [func createModel(configuration: Data, processorType: String, tokenizer: any Tokenizer) throws -> sending any UserInputProcessor](./processortyperegistry/createmodel%28configuration,processortype,tokenizer%29.md)
  Given a `processorType` and configuration data instantiate a new `UserInputProcessor`.
- [func registerProcessorType(String, creator: (Data, any Tokenizer) throws -> any UserInputProcessor)](./processortyperegistry/registerprocessortype%28_,creator%29.md)
  Add a new model to the type registry.
### Default Implementations
- [Actor Implementations](./processortyperegistry/actor-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.Actor


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/processortyperegistry)*