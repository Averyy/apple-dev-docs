# AIModel

**Framework**: Core AI  
**Kind**: struct  
**Role**: Structure

A specialized model for running inference on a device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct AIModel
```

## Mentions

- [Managing model specialization and caching](./managing-model-specialization-and-caching.md)
- [Compiling Core AI models ahead of time](./compiling-core-ai-models-ahead-of-time.md)
- [Integrating on-device AI models in your app with Core AI](./integrating-on-device-ai-models-in-your-app-with-core-ai.md)

## Overview

An `AIModel` represents a specialized `.aimodel` asset, optimized for the current device’s hardware. You create one by loading the asset from disk:

```swift
let model = try await AIModel(contentsOf: modelURL)
```

Use [`functionDescriptor(for:)`](./aimodel/functiondescriptor%28for%29.md) to inspect a function’s inputs and outputs, then load an [`InferenceFunction`](./inferencefunction.md) to run inference.

> **Note**: The model instance is lightweight and doesn’t own weights or intermediate buffers. Those resources belong to the functions you load from it.

## Topics

### Creating a model
- [init(contentsOf: URL, options: SpecializationOptions) async throws](./aimodel/init%28contentsof,options%29.md)
  Creates an [`AIModel`](./aimodel.md) from a `.aimodel`or `.aimodelc` file.
- [init?(resolvingBookmark: Data) throws](./aimodel/init%28resolvingbookmark%29.md)
  Create an `AIModel`  by resolving bookmark data pointing to its specialized asset in a cache
### Loading inference functions
- [func loadFunction(named: String) throws -> InferenceFunction?](./aimodel/loadfunction%28named%29.md)
- [func functionDescriptor(for: String) -> InferenceFunctionDescriptor?](./aimodel/functiondescriptor%28for%29.md)
  Returns a descriptor for the specified function.
- [var functionNames: [String]](./aimodel/functionnames.md)
  The names of the inference functions in this model.
### Specializing a model
- [static func specialize(contentsOf: URL, options: SpecializationOptions, cache: AIModelCache, cachePolicy: AIModelCache.Policy) async throws -> AIModel](./aimodel/specialize%28contentsof,options,cache,cachepolicy%29.md)
  Specializes a model for the current device.
### Inspecting a model
- [var bookmarkData: Data](./aimodel/bookmarkdata.md)
  Create a bookmark for this AIModel’s cached specialized asset entry as serialized data.
- [static var deviceArchitectureName: String](./aimodel/devicearchitecturename.md)
  The Core AI architecture name of the current device.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Essentials
- [Integrating on-device AI models in your app with Core AI](./integrating-on-device-ai-models-in-your-app-with-core-ai.md)
  Power your app’s intelligent features with an on-device AI model.
- [struct AIModelAsset](./aimodelasset.md)
  An unspecialized source model asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel)*