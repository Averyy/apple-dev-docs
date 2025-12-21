# beginInteractiveMovementForItem(at:)

**Framework**: UIKit  
**Kind**: method

Initiates the interactive movement of the item at the specified index path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func beginInteractiveMovementForItem(at indexPath: IndexPath) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if it is possible to move the item or [`false`](https://developer.apple.com/documentation/Swift/false) if the item is not allowed to move.

#### Discussion

Call this method when you want to begin the interactive movement of an item from its current location to a new location within the same collection view. When using a gesture recognizer to track movements of the item, call this method from your handler method when the gesture recognition process begins. When interactions with the item end, you must call either the [`endInteractiveMovement()`](uicollectionview/endinteractivemovement().md) or [`cancelInteractiveMovement()`](uicollectionview/cancelinteractivemovement().md) method to inform the collection view of that fact.

When you call this method, the collection view consults its delegate to make sure the item can be moved. If the data source does not support the movement of the item, this method returns [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `indexPath`: The index path of the item you want to move.

## See Also

- [func updateInteractiveMovementTargetPosition(CGPoint)](uicollectionview/updateinteractivemovementtargetposition(_:).md)
  Updates the position of the item within the collection view’s bounds.
- [func endInteractiveMovement()](uicollectionview/endinteractivemovement.md)
  Ends interactive movement tracking and moves the target item to its new location.
- [func cancelInteractiveMovement()](uicollectionview/cancelinteractivemovement.md)
  Ends interactive movement tracking and returns the target item to its original location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/begininteractivemovementforitem(at:))*