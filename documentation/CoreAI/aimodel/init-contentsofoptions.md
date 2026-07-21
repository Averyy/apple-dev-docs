# init(contentsOf:options:)

**Framework**: Core AI  
**Kind**: init

Creates an [`AIModel`](aimodel.md) from a `.aimodel`or `.aimodelc` file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
init(contentsOf modelURL: URL, options: SpecializationOptions = .default) async throws
```

## Mentions

- [Compiling Core AI models ahead of time](compiling-core-ai-models-ahead-of-time.md)
- [Integrating on-device AI models in your app with Core AI](integrating-on-device-ai-models-in-your-app-with-core-ai.md)
- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Discussion

This initializer specializes the model if needed, caching the result for future calls.

Specializing the model can take a significant amount of time depending on model size and the compute unit types it targets. This initializer always uses the [`default`](aimodelcache/default.md) cache.

> **Note**: If specializing or loading the model fails.

## Parameters

- `modelURL`: The URL of a `.aimodel` or `.aimodelc` file.
- `options`: Options for the specialization process.

## See Also

- [init?(resolvingBookmark: Data) throws](aimodel/init(resolvingbookmark:).md)
  Create an `AIModel`  by resolving bookmark data pointing to its specialized asset in a cache


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel/init(contentsof:options:))*