# apply(_:)

**Framework**: UIKit  
**Kind**: method

Applies the specified layout attributes to the view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func apply(_ layoutAttributes: UICollectionViewLayoutAttributes)
```

#### Discussion

The default implementation of this method does nothing.

If the layout object supports custom layout attributes, you can use this method to apply those attributes to the view. In such a case, the `layoutAttributes` parameter should contain an instance of a subclass of [`UICollectionViewLayoutAttributes`](uicollectionviewlayoutattributes.md). You do not need to override this method to support the standard layout attributes of the [`UICollectionViewLayoutAttributes`](uicollectionviewlayoutattributes.md) class. The collection view applies those attributes automatically.

## Parameters

- `layoutAttributes`: The layout attributes to apply.

## See Also

- [func preferredLayoutAttributesFitting(UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes](uicollectionreusableview/preferredlayoutattributesfitting(_:).md)
  Gives the cell a chance to modify the attributes provided by the layout object.
- [func willTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](uicollectionreusableview/willtransition(from:to:).md)
  Tells your view that the layout object of the collection view is about to change.
- [func didTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](uicollectionreusableview/didtransition(from:to:).md)
  Tells your view that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview/apply(_:))*