# deleteEntry(referencedBy:)

**Framework**: Core AI  
**Kind**: method

Deletes a cache entry referenced by bookmark data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static func deleteEntry(referencedBy bookmark: Data) throws
```

#### Discussion

Use this method to delete a cache entry referenced by bookmark data previously obtained from `AIModel.bookmarkData`. Because bookmark data encodes both the specific cache instance and the entry within it, this method is static and requires no cache instance to call.

> **Note**: If no [`AIModel`](aimodel.md) instance currently references the entry, deletion happens immediately. Otherwise, an error is thrown. Deletion can only occur for an entry when the last [`AIModel`](aimodel.md) releases it.

## Parameters

- `bookmark`: Data previously obtained from `AIModel.bookmarkData`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodelcache/deleteentry(referencedby:))*