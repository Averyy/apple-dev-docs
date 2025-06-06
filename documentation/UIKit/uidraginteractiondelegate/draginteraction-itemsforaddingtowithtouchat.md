# dragInteraction(_:itemsForAddingTo:withTouchAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for the drag items to add to an in-progress drag session, in response to a user gesture to add the items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dragInteraction(_ interaction: UIDragInteraction, itemsForAddingTo session: any UIDragSession, withTouchAt point: CGPoint) -> [UIDragItem]
```

#### Return Value

An array of drag items to add to the drag session, or an empty array if there are no items to add to the session.

#### Discussion

Not implementing this method is the same as always returning an empty array.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The current drag session.
- `point`: The location of the user’s touch in the interaction’s view. The touch point is in the view’s coordinate system.

## See Also

- [func dragInteraction(UIDragInteraction, itemsForBeginning: any UIDragSession) -> [UIDragItem]](uidraginteractiondelegate/draginteraction(_:itemsforbeginning:).md)
  Asks the delegate for the array of drag items for an impending drag interaction.
- [func dragInteraction(UIDragInteraction, sessionForAddingItems: [any UIDragSession], withTouchAt: CGPoint) -> (any UIDragSession)?](uidraginteractiondelegate/draginteraction(_:sessionforaddingitems:withtouchat:).md)
  Asks the delegate which drag session to add drag items to when there is more than one in-progress session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:itemsforaddingto:withtouchat:))*