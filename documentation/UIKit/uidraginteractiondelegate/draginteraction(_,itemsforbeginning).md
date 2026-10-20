# dragInteraction(_:itemsForBeginning:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asks the delegate for the array of drag items for an impending drag interaction.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func dragInteraction(_ interaction: UIDragInteraction, itemsForBeginning session: any UIDragSession) -> [UIDragItem]
```

```objc
- (NSArray<UIDragItem *> *) dragInteraction:(UIDragInteraction *) interaction itemsForBeginningSession:(id<UIDragSession>) session;
```

## Mentions

- [Making a view into a drag source](../making-a-view-into-a-drag-source.md)

#### Return Value

An array of drag items to include in the drag session, or an empty array if there are no drag items for the session.

#### Discussion

As part of enabling dragging from a view, implement this method to return an array of one or more drag items. The system calls this method and uses this array to populate the drag session’s `items` property.

If the drag items represent model objects in your app that are shown in a linear order, return them in the natural first-to-last order that users expect. The system handles any order-flipping required for right-to-left scripts.

Typically, the system shows multiple dragged items as a stack of images, with the array’s first element on top. If you return an empty array, the system does not start a drag interaction.

## Parameters

- `interaction`: The interaction asking for the drag items.
- `session`: The current drag session.

## See Also

### Performing the drag
- [func dragInteraction(UIDragInteraction, itemsForAddingTo: any UIDragSession, withTouchAt: CGPoint) -> [UIDragItem]](./draginteraction%28_,itemsforaddingto,withtouchat%29.md)
  Asks the delegate for the drag items to add to an in-progress drag session, in response to a user gesture to add the items.
- [func dragInteraction(UIDragInteraction, sessionForAddingItems: [any UIDragSession], withTouchAt: CGPoint) -> (any UIDragSession)?](./draginteraction%28_,sessionforaddingitems,withtouchat%29.md)
  Asks the delegate which drag session to add drag items to when there is more than one in-progress session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:itemsforbeginning:))*