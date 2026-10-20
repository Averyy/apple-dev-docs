# targetIndexPathsForInteractivelyMovingItems

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of index paths representing the new location of moving items in the collection view.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var targetIndexPathsForInteractivelyMovingItems: [IndexPath]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSIndexPath *> * targetIndexPathsForInteractivelyMovingItems;
```

#### Discussion

This property is filled when an interactive move is in progress or has just ended. Use this property together with the [`previousIndexPathsForInteractivelyMovingItems`](./previousindexpathsforinteractivelymovingitems.md) property to determine what changes you need to make to the affected items. For most other updates, the value of this property is `nil`.

## See Also

### Invalidating the Order of Items
- [var previousIndexPathsForInteractivelyMovingItems: [IndexPath]?](./previousindexpathsforinteractivelymovingitems.md)
  An array of index paths representing the previous location of moving items in the collection view.
- [var interactiveMovementTarget: CGPoint](./interactivemovementtarget.md)
  The current point used to determine the placement of moving items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewlayoutinvalidationcontext/targetindexpathsforinteractivelymovingitems)*