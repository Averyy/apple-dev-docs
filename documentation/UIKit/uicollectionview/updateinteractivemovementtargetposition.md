# updateInteractiveMovementTargetPosition(_:)

**Framework**: UIKit  
**Kind**: method

Updates the position of the item within the collection view’s bounds.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateInteractiveMovementTargetPosition(_ targetPosition: CGPoint)
```

#### Discussion

When moving an item interactively, use this method to provide the collection view with the item’s new position. When using a gesture recognizer to track user interactions with the item, call this method each time the gesture recognizer reports a location change. The collection view uses the new point to determine if the item needs to be repositioned and if the current layout needs to be updated.

For each position change, the collection view reports the change to the [`collectionView(_:targetIndexPathForMoveFromItemAt:toProposedIndexPath:)`](uicollectionviewdelegate/collectionview(_:targetindexpathformovefromitemat:toproposedindexpath:).md) method of its delegate

## Parameters

- `targetPosition`: The position of the item in the collection view’s coordinate system.

## See Also

- [func beginInteractiveMovementForItem(at: IndexPath) -> Bool](uicollectionview/begininteractivemovementforitem(at:).md)
  Initiates the interactive movement of the item at the specified index path.
- [func endInteractiveMovement()](uicollectionview/endinteractivemovement.md)
  Ends interactive movement tracking and moves the target item to its new location.
- [func cancelInteractiveMovement()](uicollectionview/cancelinteractivemovement.md)
  Ends interactive movement tracking and returns the target item to its original location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/updateinteractivemovementtargetposition(_:))*