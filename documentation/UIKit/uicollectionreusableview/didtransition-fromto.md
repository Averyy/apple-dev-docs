# didTransition(from:to:)

**Framework**: UIKit  
**Kind**: method

Tells your view that the layout object of the collection view changed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func didTransition(from oldLayout: UICollectionViewLayout, to newLayout: UICollectionViewLayout)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to finalize any behaviors associated with the change in layouts.

## Parameters

- `oldLayout`: The collection view’s previous layout object.
- `newLayout`: The current layout object associated with the collection view.

## See Also

- [func preferredLayoutAttributesFitting(UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes](uicollectionreusableview/preferredlayoutattributesfitting(_:).md)
  Gives the cell a chance to modify the attributes provided by the layout object.
- [func apply(UICollectionViewLayoutAttributes)](uicollectionreusableview/apply(_:).md)
  Applies the specified layout attributes to the view.
- [func willTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](uicollectionreusableview/willtransition(from:to:).md)
  Tells your view that the layout object of the collection view is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview/didtransition(from:to:))*