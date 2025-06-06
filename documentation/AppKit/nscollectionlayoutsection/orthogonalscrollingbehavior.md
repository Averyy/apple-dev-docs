# orthogonalScrollingBehavior

**Framework**: AppKit  
**Kind**: property

The section’s scrolling behavior in relation to the main layout axis.

**Availability**:
- macOS 10.15+

## Declaration

```swift
@MainActor
var orthogonalScrollingBehavior: NSCollectionLayoutSectionOrthogonalScrollingBehavior { get set }
```

#### Discussion

The default value of this property is [`UICollectionLayoutSectionOrthogonalScrollingBehavior.none`](https://developer.apple.com/documentation/UIKit/UICollectionLayoutSectionOrthogonalScrollingBehavior/none), which means the section lays out its content along the main axis of its layout, defined by the layout configuration’s [`scrollDirection`](https://developer.apple.com/documentation/UIKit/UICollectionViewCompositionalLayoutConfiguration/scrollDirection) property. Set a different value for this property to get the section to lay out its content orthogonally to the main layout axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionlayoutsection/orthogonalscrollingbehavior)*