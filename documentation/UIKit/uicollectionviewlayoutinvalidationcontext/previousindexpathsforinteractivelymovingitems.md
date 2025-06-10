# previousIndexPathsForInteractivelyMovingItems

**Framework**: UIKit  
**Kind**: property

An array of index paths representing the previous location of moving items in the collection view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var previousIndexPathsForInteractivelyMovingItems: [IndexPath]? { get }
```

#### Discussion

This property is filled when an interactive move is in progress or has just ended. Use this property together with the [`targetIndexPathsForInteractivelyMovingItems`](uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems.md) property to determine what changes you need to make to the affected items. For most other updates, the value of this property is `nil`.

## See Also

- [var targetIndexPathsForInteractivelyMovingItems: [IndexPath]?](uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems.md)
  An array of index paths representing the new location of moving items in the collection view.
- [var interactiveMovementTarget: CGPoint](uicollectionviewlayoutinvalidationcontext/interactivemovementtarget.md)
  The current point used to determine the placement of moving items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/previousindexpathsforinteractivelymovingitems)*