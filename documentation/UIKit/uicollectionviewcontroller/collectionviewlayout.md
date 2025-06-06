# collectionViewLayout

**Framework**: UIKit  
**Kind**: property

The layout object used to initialize the collection view controller.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var collectionViewLayout: UICollectionViewLayout { get }
```

#### Discussion

This property contains the layout object you passed to the [`init(collectionViewLayout:)`](uicollectionviewcontroller/init(collectionviewlayout:).md) method. The layout object in this property isn’t updated to reflect changes to the collection view itself. You can use this property to refer to the layout object you originally configured the collection view to use.

## See Also

- [var collectionView: UICollectionView!](uicollectionviewcontroller/collectionview.md)
  The collection view object managed by this view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/collectionviewlayout)*