# deleteAll()

**Framework**: Core AI  
**Kind**: method

Deletes all entries in the cache.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func deleteAll() throws
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Discussion

Use this method to reclaim storage when the app no longer needs any of its specialized models, or to reset the cache during testing.

> **Note**: For each entry, if no [`AIModel`](aimodel.md) instance currently references it, deletion happens immediately. Otherwise, an error is thrown. Deletion can only occur for an entry when the last [`AIModel`](aimodel.md) releases it.

## See Also

- [func deleteEntry(for: URL, options: SpecializationOptions) throws](aimodelcache/deleteentry(for:options:).md)
  Deletes the cache entry for a specific model and specialization options combination.
- [func deleteEntries(for: URL) throws](aimodelcache/deleteentries(for:).md)
  Deletes all cache entries for a specific model, regardless of specialization options.
- [static func deleteEntry(referencedBy: Data) throws](aimodelcache/deleteentry(referencedby:).md)
  Deletes a cache entry referenced by bookmark data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/deleteall())*