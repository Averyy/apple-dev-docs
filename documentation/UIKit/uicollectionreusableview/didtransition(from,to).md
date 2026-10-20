# didTransition(from:to:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells your view that the layout object of the collection view changed.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func didTransition(from oldLayout: UICollectionViewLayout, to newLayout: UICollectionViewLayout)
```

```objc
- (void) didTransitionFromLayout:(UICollectionViewLayout *) oldLayout toLayout:(UICollectionViewLayout *) newLayout;
```

#### Discussion

The default implementation of this method does nothing. Subclasses can override this method and use it to finalize any behaviors associated with the change in layouts.

## Parameters

- `oldLayout`: The collection view’s previous layout object.
- `newLayout`: The current layout object associated with the collection view.

## See Also

### Managing layout changes
- [func preferredLayoutAttributesFitting(UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes](./preferredlayoutattributesfitting%28_%29.md)
  Gives the cell a chance to modify the attributes provided by the layout object.
- [func apply(UICollectionViewLayoutAttributes)](./apply%28_%29.md)
  Applies the specified layout attributes to the view.
- [func willTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](./willtransition%28from,to%29.md)
  Tells your view that the layout object of the collection view is about to change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview/didtransition(from:to:))*