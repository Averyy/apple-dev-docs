# willTransition(from:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells your view that the layout object of the collection view is about to change.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func willTransition(from oldLayout: UICollectionViewLayout, to newLayout: UICollectionViewLayout)
```

```objc
- (void) willTransitionFromLayout:(UICollectionViewLayout *) oldLayout toLayout:(UICollectionViewLayout *) newLayout;
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to prepare for the change in layouts.

## Parameters

- `oldLayout`: The current layout object associated with the collection view.
- `newLayout`: The new layout object that is about to be applied to the collection view.

## See Also

### Managing layout changes
- [func preferredLayoutAttributesFitting(UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes](./preferredlayoutattributesfitting%28_%29.md)
  Gives the cell a chance to modify the attributes provided by the layout object.
- [func apply(UICollectionViewLayoutAttributes)](./apply%28_%29.md)
  Applies the specified layout attributes to the view.
- [func didTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](./didtransition%28from,to%29.md)
  Tells your view that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview/willtransition(from:to:))*