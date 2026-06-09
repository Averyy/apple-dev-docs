# model(for:options:)

**Framework**: Core AI  
**Kind**: method

Returns a previously specialized model from the cache, if available.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func model(for modelURL: URL, options: SpecializationOptions) throws -> AIModel?
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Return Value

The model if a matching cache entry exists, or `nil` otherwise.

#### Discussion

If this cache holds a specialized asset from previously specializing the model at `modelURL` with the specified `options`, this method loads and returns the model. This method never performs specialization.

> **Note**: If a cache entry was found but the specialized asset failed to load.

## Parameters

- `modelURL`: The URL of an `.aimodel` file that you previously specialized.
- `options`: The specialization options to match against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/model(for:options:))*