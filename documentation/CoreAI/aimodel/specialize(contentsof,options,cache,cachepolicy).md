# specialize(contentsOf:options:cache:cachePolicy:)

**Framework**: Core AI  
**Kind**: method

Specializes a model for the current device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
@discardableResult
static func specialize(contentsOf modelURL: URL, options: SpecializationOptions = .default, cache: AIModelCache = .default, cachePolicy: AIModelCache.Policy = .default) async throws -> AIModel
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Return Value

The model, ready for inference on the current device.

#### Discussion

This method performs specialization on the input `.aimodel` or `.aimodelc`, storing the resulting specialized assets in the specified cache.

> **Note**: If specializing or loading the model fails.

## Parameters

- `modelURL`: The URL of a `.aimodel` or `.aimodelc` file.
- `options`: Options for the specialization process.
- `cache`: The cache to store the resulting specialized asset in.
- `cachePolicy`: The policy to apply to the resulting specialized asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel/specialize(contentsof:options:cache:cachepolicy:))*