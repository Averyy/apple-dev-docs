# willTransition(from:to:)

**Framework**: UIKit  
**Kind**: method

Tells your view that the layout object of the collection view is about to change.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func willTransition(from oldLayout: UICollectionViewLayout, to newLayout: UICollectionViewLayout)
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to prepare for the change in layouts.

## Parameters

- `oldLayout`: The current layout object associated with the collection view.
- `newLayout`: The new layout object that is about to be applied to the collection view.

## See Also

- [func preferredLayoutAttributesFitting(UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes](uicollectionreusableview/preferredlayoutattributesfitting(_:).md)
  Gives the cell a chance to modify the attributes provided by the layout object.
- [func apply(UICollectionViewLayoutAttributes)](uicollectionreusableview/apply(_:).md)
  Applies the specified layout attributes to the view.
- [func didTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](uicollectionreusableview/didtransition(from:to:).md)
  Tells your view that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview/willtransition(from:to:))*