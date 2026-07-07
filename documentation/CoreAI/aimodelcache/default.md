# default

**Framework**: Core AI  
**Kind**: property

The shared cache scoped to your app bundle.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static let `default`: AIModelCache
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Discussion

The shared specialized asset cache for your app bundle. The framework uses this cache by default whenever specialization happens automatically, such as during [`init(contentsOf:options:)`](aimodel/init(contentsof:options:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/default)*