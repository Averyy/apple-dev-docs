# collectionViewContentSize

**Framework**: UIKit  
**Kind**: property

The width and height of the collection view’s contents.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
var collectionViewContentSize: CGSize { get }
```

#### Return Value

The width and height of the collection view’s contents.

#### Discussion

Subclasses must override this property and use it to return the width and height of the collection view’s content. These values represent the width and height of all the content, not just the content that is currently visible. The collection view uses this information to configure its own content size for scrolling purposes.

The default implementation of this method returns [`CGSizeZero`](https://developer.apple.com/documentation/CoreGraphics/CGSizeZero).

## See Also

- [var collectionView: UICollectionView?](uicollectionviewlayout/collectionview.md)
  The collection view object currently using this layout object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayout/collectionviewcontentsize)*