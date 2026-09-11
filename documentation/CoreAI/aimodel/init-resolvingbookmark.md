# init(resolvingBookmark:)

**Framework**: Core AI  
**Kind**: init

Create an `AIModel`  by resolving bookmark data pointing to its specialized asset in a cache

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init?(resolvingBookmark bookmark: Data) throws
```

#### Return Value

If the bookmark data can be resolved, the resulting `AIModel` pins and references the cache entry as the model that generated the bookmark data. If it cannot be resolved due to the specialized asset entry no longer being present nil is returned.

#### Discussion

Resolving bookmark data involves checking it is a valid bookmark, validating the associated cache and cache entry it references exists, and returning a AIModel constructed with that specialized asset contained within that entry. If any of these steps fail, nil is returned

> **Note**: If the bookmark data is malformed due to not being sourced from AIModel.bookmarkData an error is thrown

## Parameters

- `bookmark`: Data previously obtained from `AIModel.bookmarkData`.

## See Also

- [init(contentsOf: URL, options: SpecializationOptions) async throws](aimodel/init(contentsof:options:).md)
  Creates an [`AIModel`](aimodel.md) from a `.aimodel`or `.aimodelc` file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/aimodel/init(resolvingbookmark:))*