# representedElementKind

**Framework**: UIKit  
**Kind**: property

The layout-specific identifier for the target view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var representedElementKind: String? { get }
```

#### Discussion

You can use the value in this property to identify the specific purpose of the supplementary or decoration view associated with the attributes. This property is `nil` if the [`representedElementCategory`](uicollectionviewlayoutattributes/representedelementcategory.md) property contains the value [`UICollectionView.ElementCategory.cell`](uicollectionview/elementcategory/cell.md).

## See Also

- [var indexPath: IndexPath](uicollectionviewlayoutattributes/indexpath.md)
  The index path of the item in the collection view.
- [var representedElementCategory: UICollectionView.ElementCategory](uicollectionviewlayoutattributes/representedelementcategory.md)
  The type of the item.
- [UICollectionView.ElementCategory](uicollectionview/elementcategory.md)
  Constants specifying the type of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/representedelementkind)*