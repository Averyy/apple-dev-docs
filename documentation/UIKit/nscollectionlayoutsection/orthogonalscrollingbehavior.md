# orthogonalScrollingBehavior

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The section’s scrolling behavior in relation to the main layout axis.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var orthogonalScrollingBehavior: UICollectionLayoutSectionOrthogonalScrollingBehavior { get set }
```

```objc
@property (nonatomic) UICollectionLayoutSectionOrthogonalScrollingBehavior orthogonalScrollingBehavior;
```

## Discussion

The default value of this property is [`UICollectionLayoutSectionOrthogonalScrollingBehavior.none`](../uicollectionlayoutsectionorthogonalscrollingbehavior/none.md), which means the section lays out its content along the main axis of its layout, defined by the layout configuration’s [`scrollDirection`](../uicollectionviewcompositionallayoutconfiguration/scrolldirection.md) property. Set a different value for this property to get the section to lay out its content orthogonally to the main layout axis.

## See Also

### Specifying scrolling behavior
- [var orthogonalScrollingProperties: UICollectionLayoutSectionOrthogonalScrollingProperties](./orthogonalscrollingproperties.md)
  The section’s orthogonal scrolling properties.
- [class UICollectionLayoutSectionOrthogonalScrollingProperties](../uicollectionlayoutsectionorthogonalscrollingproperties.md)
  An object that specifies properties for a layout section that scrolls orthogonally in relation to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/orthogonalscrollingbehavior)*