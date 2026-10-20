# pageThumbnails(visibleParts:)

**Framework**: Assignables  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Exports thumbnails of each page such that the thumbnails contain the indicated layers.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
func pageThumbnails(visibleParts: [Self.PartID]) async -> [Self.Page.ID : Self.Page.Thumbnail]
```

## Parameters

- `visibleParts`: The lDs of layers that should be included in the thumbnail.

## Default Implementations

### MergeableDocument Implementations
- [func pageThumbnails(visibleParts: [MergeablePartsContainerPartID]) async -> [Self.Page.ID : Self.Page.Thumbnail]](./pagethumbnails%28visibleparts%29-51xw7.md)
  Exports thumbnails of each page such that the thumbnails contain the indicated layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeabledocument/pagethumbnails(visibleparts:))*