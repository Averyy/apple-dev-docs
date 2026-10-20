# beginInteractiveMovementForItem(at:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Initiates the interactive movement of the item at the specified index path.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func beginInteractiveMovementForItem(at indexPath: IndexPath) -> Bool
```

```objc
- (BOOL) beginInteractiveMovementForItemAtIndexPath:(NSIndexPath *) indexPath;
```

#### Return Value

[`true`](../../Swift/true.md) if it is possible to move the item or [`false`](../../Swift/false.md) if the item is not allowed to move.

#### Discussion

Call this method when you want to begin the interactive movement of an item from its current location to a new location within the same collection view. When using a gesture recognizer to track movements of the item, call this method from your handler method when the gesture recognition process begins. When interactions with the item end, you must call either the [`endInteractiveMovement()`](./endinteractivemovement%28%29.md) or [`cancelInteractiveMovement()`](./cancelinteractivemovement%28%29.md) method to inform the collection view of that fact.

When you call this method, the collection view consults its delegate to make sure the item can be moved. If the data source does not support the movement of the item, this method returns [`false`](../../Swift/false.md).

## Parameters

- `indexPath`: The index path of the item you want to move.

## See Also

### Reordering items interactively
- [func updateInteractiveMovementTargetPosition(CGPoint)](./updateinteractivemovementtargetposition%28_%29.md)
  Updates the position of the item within the collection view’s bounds.
- [func endInteractiveMovement()](./endinteractivemovement%28%29.md)
  Ends interactive movement tracking and moves the target item to its new location.
- [func cancelInteractiveMovement()](./cancelinteractivemovement%28%29.md)
  Ends interactive movement tracking and returns the target item to its original location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionview/begininteractivemovementforitem(at:))*