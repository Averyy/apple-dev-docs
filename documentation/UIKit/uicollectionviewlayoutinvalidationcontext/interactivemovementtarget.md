# interactiveMovementTarget

**Framework**: UIKit  
**Kind**: property

The current point used to determine the placement of moving items.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var interactiveMovementTarget: CGPoint { get }
```

#### Discussion

This property is filled when an interactive move is in progress or has just ended. The value represents the point that was used to determine the new index paths in the [`targetIndexPathsForInteractivelyMovingItems`](uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems.md) property. You can use this point as needed to calculate the position of items in your layout.

## See Also

- [var previousIndexPathsForInteractivelyMovingItems: [IndexPath]?](uicollectionviewlayoutinvalidationcontext/previousindexpathsforinteractivelymovingitems.md)
  An array of index paths representing the previous location of moving items in the collection view.
- [var targetIndexPathsForInteractivelyMovingItems: [IndexPath]?](uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems.md)
  An array of index paths representing the new location of moving items in the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/interactivemovementtarget)*