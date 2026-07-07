# deleteEntries(for:)

**Framework**: Core AI  
**Kind**: method

Deletes all cache entries for a specific model, regardless of specialization options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func deleteEntries(for modelURL: URL) throws
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Discussion

A model may have multiple entries in the cache. For example, one with [`cpuOnly`](specializationoptions/cpuonly.md) and another with [`default`](specializationoptions/default.md). This method deletes all of them.

> **Note**: For each entry, if no [`AIModel`](aimodel.md) instance currently references it, deletion happens immediately. Otherwise, an error is thrown. Deletion can only occur for an entry when the last [`AIModel`](aimodel.md) releases it.

## Parameters

- `modelURL`: The URL of an `.aimodel` file that you previously specialized.

## See Also

- [func deleteEntry(for: URL, options: SpecializationOptions) throws](aimodelcache/deleteentry(for:options:).md)
  Deletes the cache entry for a specific model and specialization options combination.
- [func deleteAll() throws](aimodelcache/deleteall.md)
  Deletes all entries in the cache.
- [static func deleteEntry(referencedBy: Data) throws](aimodelcache/deleteentry(referencedby:).md)
  Deletes a cache entry referenced by bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/deleteentries(for:))*