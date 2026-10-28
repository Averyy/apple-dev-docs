# collectionView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The collection view object currently using this layout object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var collectionView: UICollectionView? { get }
```

```objc
@property (nonatomic, readonly, nullable) UICollectionView * collectionView;
```

## Discussion

The collection view object sets the value of this property when a new layout object is assigned to it.

## See Also

### Getting the collection view information
- [var collectionViewContentSize: CGSize](./collectionviewcontentsize.md)
  The width and height of the collection view’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/collectionview)*