# indexPath

**Framework**: UIKit  
**Kind**: property

The index path of the item in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var indexPath: IndexPath { get set }
```

#### Discussion

The index path contains the index of the section and the index of the item within that section. These two values uniquely identify the position of the corresponding item in the collection view.

## See Also

- [var representedElementKind: String?](uicollectionviewlayoutattributes/representedelementkind.md)
  The layout-specific identifier for the target view.
- [var representedElementCategory: UICollectionView.ElementCategory](uicollectionviewlayoutattributes/representedelementcategory.md)
  The type of the item.
- [UICollectionView.ElementCategory](uicollectionview/elementcategory.md)
  Constants specifying the type of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/indexpath)*