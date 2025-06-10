# representedElementCategory

**Framework**: UIKit  
**Kind**: property

The type of the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var representedElementCategory: UICollectionView.ElementCategory { get }
```

#### Discussion

You can use the value in this property to distinguish whether the layout attributes are intended for a cell, supplementary view, or decoration view.

## See Also

- [var indexPath: IndexPath](uicollectionviewlayoutattributes/indexpath.md)
  The index path of the item in the collection view.
- [var representedElementKind: String?](uicollectionviewlayoutattributes/representedelementkind.md)
  The layout-specific identifier for the target view.
- [UICollectionView.ElementCategory](uicollectionview/elementcategory.md)
  Constants specifying the type of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/representedelementcategory)*