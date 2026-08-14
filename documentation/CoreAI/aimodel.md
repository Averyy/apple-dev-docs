# AIModel

**Framework**: Core AI  
**Kind**: struct

A specialized model for running inference on a device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct AIModel
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)
- [Compiling Core AI models ahead of time](compiling-core-ai-models-ahead-of-time.md)
- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)

#### Overview

An `AIModel` represents a specialized `.aimodel` asset, optimized for the current device’s hardware. You create one by loading the asset from disk:

```swift
let model = try await AIModel(contentsOf: modelURL)
```

Use [`functionDescriptor(for:)`](aimodel/functiondescriptor(for:).md) to inspect a function’s inputs and outputs, then load an [`InferenceFunction`](inferencefunction.md) to run inference.

> **Note**: The model instance is lightweight and doesn’t own weights or intermediate buffers. Those resources belong to the functions you load from it.

## Topics

### Creating a model
- [init(contentsOf: URL, options: SpecializationOptions) async throws](aimodel/init(contentsof:options:).md)
  Creates an [`AIModel`](aimodel.md) from a `.aimodel`or `.aimodelc` file.
- [init?(resolvingBookmark: Data) throws](aimodel/init(resolvingbookmark:).md)
  Create an `AIModel`  by resolving bookmark data pointing to its specialized asset in a cache
### Loading inference functions
- [func loadFunction(named: String) throws -> InferenceFunction?](aimodel/loadfunction(named:).md)
- [func functionDescriptor(for: String) -> InferenceFunctionDescriptor?](aimodel/functiondescriptor(for:).md)
  Returns a descriptor for the specified function.
- [var functionNames: [String]](aimodel/functionnames.md)
  The names of the inference functions in this model.
### Specializing a model
- [static func specialize(contentsOf: URL, options: SpecializationOptions, cache: AIModelCache, cachePolicy: AIModelCache.Policy) async throws -> AIModel](aimodel/specialize(contentsof:options:cache:cachepolicy:).md)
  Specializes a model for the current device.
### Inspecting a model
- [var bookmarkData: Data](aimodel/bookmarkdata.md)
  Create a bookmark for this AIModel’s cached specialized asset entry as serialized data.
- [static var deviceArchitectureName: String](aimodel/devicearchitecturename.md)
  The Core AI architecture name of the current device.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)
  Power your app’s intelligent features with an on-device AI model.
- [struct AIModelAsset](aimodelasset.md)
  An unspecialized source model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel)*