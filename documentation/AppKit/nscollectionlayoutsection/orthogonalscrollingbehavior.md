# orthogonalScrollingBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The section’s scrolling behavior in relation to the main layout axis.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var orthogonalScrollingBehavior: NSCollectionLayoutSectionOrthogonalScrollingBehavior { get set }
```

```objc
@property NSCollectionLayoutSectionOrthogonalScrollingBehavior orthogonalScrollingBehavior;
```

#### Discussion

The default value of this property is [`UICollectionLayoutSectionOrthogonalScrollingBehavior.none`](../../UIKit/uicollectionlayoutsectionorthogonalscrollingbehavior/none.md), which means the section lays out its content along the main axis of its layout, defined by the layout configuration’s [`scrollDirection`](../../UIKit/uicollectionviewcompositionallayoutconfiguration/scrolldirection.md) property. Set a different value for this property to get the section to lay out its content orthogonally to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsection/orthogonalscrollingbehavior)*