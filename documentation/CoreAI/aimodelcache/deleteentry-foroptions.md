# deleteEntry(for:options:)

**Framework**: Core AI  
**Kind**: method

Deletes the cache entry for a specific model and specialization options combination.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func deleteEntry(for modelURL: URL, options: SpecializationOptions) throws
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Discussion

> **Note**: If no [`AIModel`](aimodel.md) instance currently references the entry, deletion happens immediately. Otherwise, the system deletes the entry when the last [`AIModel`](aimodel.md) releases it.

## Parameters

- `modelURL`: The URL of an `.aimodel` file that you previously specialized.
- `options`: The specialization options to match against.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/deleteentry(for:options:))*