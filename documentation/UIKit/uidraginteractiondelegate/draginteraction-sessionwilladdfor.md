# dragInteraction(_:session:willAdd:for:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate an interaction is about to add items to a drag session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dragInteraction(_ interaction: UIDragInteraction, session: any UIDragSession, willAdd items: [UIDragItem], for addingInteraction: UIDragInteraction)
```

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The current drag session.
- `items`: The drag items the interaction will add to the session.
- `addingInteraction`: The interaction adding the drag items.

## See Also

- [func dragInteraction(UIDragInteraction, sessionWillBegin: any UIDragSession)](uidraginteractiondelegate/draginteraction(_:sessionwillbegin:).md)
  Tells the delegate the lift animation has finished and the user is starting to move the items across the screen.
- [func dragInteraction(UIDragInteraction, sessionDidMove: any UIDragSession)](uidraginteractiondelegate/draginteraction(_:sessiondidmove:).md)
  Tells the delegate the user moved the drag items to a new location on the screen.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, willEndWith: UIDropOperation)](uidraginteractiondelegate/draginteraction(_:session:willendwith:).md)
  Tells the delegate the drag activity will end with the specified operation.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, didEndWith: UIDropOperation)](uidraginteractiondelegate/draginteraction(_:session:didendwith:).md)
  Tells the delegate the drag activity and its related animations have finished.
- [func dragInteraction(UIDragInteraction, sessionDidTransferItems: any UIDragSession)](uidraginteractiondelegate/draginteraction(_:sessiondidtransferitems:).md)
  Tells the delegate the destination view has received the data for the drag items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:session:willadd:for:))*