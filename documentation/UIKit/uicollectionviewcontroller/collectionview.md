# collectionView

**Framework**: UIKit  
**Kind**: property

The collection view object managed by this view controller.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var collectionView: UICollectionView! { get set }
```

#### Discussion

If you assign a new collection view object to this property and that view’s data source or delegate aren’t yet set, the collection view controller makes itself the delegate or data source or both.

## See Also

- [var collectionViewLayout: UICollectionViewLayout](uicollectionviewcontroller/collectionviewlayout.md)
  The layout object used to initialize the collection view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/collectionview)*