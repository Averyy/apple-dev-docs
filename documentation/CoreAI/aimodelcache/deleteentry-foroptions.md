# deleteEntry(for:options:)

**Framework**: Core AI  
**Kind**: method

Deletes the cache entry for a specific model and specialization options combination.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func deleteEntry(for modelURL: URL, options: SpecializationOptions) throws
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Discussion

> **Note**: If no [`AIModel`](aimodel.md) instance currently references the entry, deletion happens immediately. Otherwise, an error is thrown. Deletion can only occur for an entry when the last [`AIModel`](aimodel.md) releases it.

## Parameters

- `modelURL`: The URL of an `.aimodel` file that you previously specialized.
- `options`: The specialization options to match against.

## See Also

- [func deleteEntries(for: URL) throws](aimodelcache/deleteentries(for:).md)
  Deletes all cache entries for a specific model, regardless of specialization options.
- [func deleteAll() throws](aimodelcache/deleteall.md)
  Deletes all entries in the cache.
- [static func deleteEntry(referencedBy: Data) throws](aimodelcache/deleteentry(referencedby:).md)
  Deletes a cache entry referenced by bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/deleteentry(for:options:))*