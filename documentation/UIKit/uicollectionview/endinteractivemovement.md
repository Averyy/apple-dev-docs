# endInteractiveMovement()

**Framework**: UIKit  
**Kind**: method

Ends interactive movement tracking and moves the target item to its new location.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func endInteractiveMovement()
```

#### Discussion

Call this method upon the successful completion of movement tracking for a item. For example, when using a gesture recognizer to track user interactions, call this method upon the successful completion of the gesture. Calling this method lets the collection view know to end tracking and move the item to its new location permanently. The collection view responds by calling the [`collectionView(_:moveItemAt:to:)`](uicollectionviewdatasource/collectionview(_:moveitemat:to:).md) method of its data source to ensure that your data structures are updated.

## See Also

- [func beginInteractiveMovementForItem(at: IndexPath) -> Bool](uicollectionview/begininteractivemovementforitem(at:).md)
  Initiates the interactive movement of the item at the specified index path.
- [func updateInteractiveMovementTargetPosition(CGPoint)](uicollectionview/updateinteractivemovementtargetposition(_:).md)
  Updates the position of the item within the collection view’s bounds.
- [func cancelInteractiveMovement()](uicollectionview/cancelinteractivemovement.md)
  Ends interactive movement tracking and returns the target item to its original location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/endinteractivemovement())*