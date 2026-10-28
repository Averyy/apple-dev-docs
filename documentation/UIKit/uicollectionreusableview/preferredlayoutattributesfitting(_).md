# preferredLayoutAttributesFitting(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Gives the cell a chance to modify the attributes provided by the layout object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func preferredLayoutAttributesFitting(_ layoutAttributes: UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes
```

```objc
- (UICollectionViewLayoutAttributes *) preferredLayoutAttributesFittingAttributes:(UICollectionViewLayoutAttributes *) layoutAttributes;
```

## Return Value

The final attributes to apply to the cell.

## Discussion

The default implementation of this method adjusts the size values to accommodate changes made by a self-sizing cell. Subclasses can override this method and use it to adjust other layout attributes too. If you override this method and want the cell size adjustments, call `super` first and make your own modifications to the returned attributes.

## Parameters

- `layoutAttributes`: The attributes provided by the layout object. These attributes represent the values that the layout intends to apply to the cell.

## See Also

### Managing layout changes
- [func apply(UICollectionViewLayoutAttributes)](./apply%28_%29.md)
  Applies the specified layout attributes to the view.
- [func willTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](./willtransition%28from,to%29.md)
  Tells your view that the layout object of the collection view is about to change.
- [func didTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](./didtransition%28from,to%29.md)
  Tells your view that the layout object of the collection view changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview/preferredlayoutattributesfitting(_:))*