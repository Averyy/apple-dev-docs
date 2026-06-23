# deleteEntries(for:)

**Framework**: Core AI  
**Kind**: method

Deletes all cache entries for a specific model, regardless of specialization options.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/deleteentries(for:))*