# orthogonalScrollingProperties

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The section’s orthogonal scrolling properties.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var orthogonalScrollingProperties: UICollectionLayoutSectionOrthogonalScrollingProperties { get }
```

```objc
@property (nonatomic, readonly) UICollectionLayoutSectionOrthogonalScrollingProperties * orthogonalScrollingProperties;
```

#### Discussion

Set this value to specify bouncing behavior and deceleration rate for an orthogonally scrolling section.

## See Also

### Specifying scrolling behavior
- [var orthogonalScrollingBehavior: UICollectionLayoutSectionOrthogonalScrollingBehavior](./orthogonalscrollingbehavior.md)
  The section’s scrolling behavior in relation to the main layout axis.
- [class UICollectionLayoutSectionOrthogonalScrollingProperties](../uicollectionlayoutsectionorthogonalscrollingproperties.md)
  An object that specifies properties for a layout section that scrolls orthogonally in relation to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/orthogonalscrollingproperties)*