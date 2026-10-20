# representedElementCategory

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The type of the item.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var representedElementCategory: UICollectionView.ElementCategory { get }
```

```objc
@property (nonatomic, readonly) UICollectionElementCategory representedElementCategory;
```

#### Discussion

You can use the value in this property to distinguish whether the layout attributes are intended for a cell, supplementary view, or decoration view.

## See Also

### Identifying the referenced item
- [var indexPath: IndexPath](./indexpath.md)
  The index path of the item in the collection view.
- [var representedElementKind: String?](./representedelementkind.md)
  The layout-specific identifier for the target view.
- [UICollectionView.ElementCategory](../uicollectionview/elementcategory.md)
  Constants specifying the type of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/representedelementcategory)*