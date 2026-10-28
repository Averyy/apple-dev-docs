# collectionView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The collection view object managed by this view controller.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var collectionView: UICollectionView! { get set }
```

```objc
@property (nonatomic, strong, null_resettable) UICollectionView * collectionView;
```

## Discussion

If you assign a new collection view object to this property and that view’s data source or delegate aren’t yet set, the collection view controller makes itself the delegate or data source or both.

## See Also

### Getting the collection view
- [var collectionViewLayout: UICollectionViewLayout](./collectionviewlayout.md)
  The layout object used to initialize the collection view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/collectionview)*