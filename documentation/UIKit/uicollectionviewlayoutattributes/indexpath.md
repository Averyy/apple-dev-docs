# indexPath

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The index path of the item in the collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var indexPath: IndexPath { get set }
```

```objc
@property (nonatomic, strong) NSIndexPath * indexPath;
```

## Discussion

The index path contains the index of the section and the index of the item within that section. These two values uniquely identify the position of the corresponding item in the collection view.

## See Also

### Identifying the referenced item
- [var representedElementKind: String?](./representedelementkind.md)
  The layout-specific identifier for the target view.
- [var representedElementCategory: UICollectionView.ElementCategory](./representedelementcategory.md)
  The type of the item.
- [UICollectionView.ElementCategory](../uicollectionview/elementcategory.md)
  Constants specifying the type of view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutattributes/indexpath)*