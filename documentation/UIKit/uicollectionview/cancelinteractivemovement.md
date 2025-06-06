# cancelInteractiveMovement()

**Framework**: UIKit  
**Kind**: method

Ends interactive movement tracking and returns the target item to its original location.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func cancelInteractiveMovement()
```

#### Discussion

Call this method to cancel movement tracking and return the item to its original location. For example, when using a gesture recognizer to track interactions, call this method when the gesture is cancelled. Calling this method lets the collection view know to end the tracking process and return the item to its original location.

## See Also

- [func beginInteractiveMovementForItem(at: IndexPath) -> Bool](uicollectionview/begininteractivemovementforitem(at:).md)
  Initiates the interactive movement of the item at the specified index path.
- [func updateInteractiveMovementTargetPosition(CGPoint)](uicollectionview/updateinteractivemovementtargetposition(_:).md)
  Updates the position of the item within the collection view’s bounds.
- [func endInteractiveMovement()](uicollectionview/endinteractivemovement.md)
  Ends interactive movement tracking and moves the target item to its new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/cancelinteractivemovement())*