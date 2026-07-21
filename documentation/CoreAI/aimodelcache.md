# AIModelCache

**Framework**: Core AI  
**Kind**: class

A cache that stores the specialized model artifacts for inference.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
final class AIModelCache
```

#### Overview

The cache holds the optimized, device-specific artifacts that [`AIModel`](aimodel.md) loads to execute its inference functions. Each cache entry contains a specialized asset formed from a specific `.aimodel` or `.aimodelc` and [`SpecializationOptions`](specializationoptions.md) combination.

## Topics

### Accessing the default cache
- [static let `default`: AIModelCache](aimodelcache/default.md)
  The shared cache scoped to your app bundle.
### Creating a shared cache
- [init?(appGroup: String)](aimodelcache/init(appgroup:).md)
  Creates a cache that shares specialized assets across an app group.
### Loading a specialized model
- [func model(for: URL, options: SpecializationOptions) throws -> AIModel?](aimodelcache/model(for:options:).md)
  Returns a previously specialized model from the cache, if available.
### Deleting cache entries
- [func deleteEntry(for: URL, options: SpecializationOptions) throws](aimodelcache/deleteentry(for:options:).md)
  Deletes the cache entry for a specific model and specialization options combination.
- [func deleteEntries(for: URL) throws](aimodelcache/deleteentries(for:).md)
  Deletes all cache entries for a specific model, regardless of specialization options.
- [func deleteAll() throws](aimodelcache/deleteall.md)
  Deletes all entries in the cache.
- [static func deleteEntry(referencedBy: Data) throws](aimodelcache/deleteentry(referencedby:).md)
  Deletes a cache entry referenced by bookmark data.
### Controlling cache persistence
- [AIModelCache.Policy](aimodelcache/policy.md)
  A policy that controls when the system purges specialized assets from a cache.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)
  Configure model specialization, manage cached assets, and reduce your app’s storage footprint.
- [Compiling Core AI models ahead of time](compiling-core-ai-models-ahead-of-time.md)
  Reduce on-device specialization time by compiling Core AI models at build time.
- [enum ComputeUnitKind](computeunitkind.md)
  A type of hardware compute unit available for model inference.
- [struct SpecializationOptions](specializationoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache)*