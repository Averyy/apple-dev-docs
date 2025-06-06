# previewSize

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The size of the drag item’s preview.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var previewSize: CGSize { get }
```

#### Discussion

You might use this property when configuring animations. If the item does not have an associated preview, this property is set to `CGSizeZero`.

## See Also

- [var sourceIndexPath: IndexPath?](uicollectionviewdropitem/sourceindexpath.md)
  The index path of the item in the collection view, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewdropitem/previewsize)*