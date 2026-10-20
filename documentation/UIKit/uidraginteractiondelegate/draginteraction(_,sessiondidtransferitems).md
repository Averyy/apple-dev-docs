# dragInteraction(_:sessionDidTransferItems:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the destination view has received the data for the drag items.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionDidTransferItems session: any UIDragSession)
```

```objc
- (void) dragInteraction:(UIDragInteraction *) interaction sessionDidTransferItems:(id<UIDragSession>) session;
```

#### Discussion

Implement this method if you need to clean up resources related to the drag items or their item provider objects.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drag session that has ended.

## See Also

### Monitoring drag progress
- [func dragInteraction(UIDragInteraction, sessionWillBegin: any UIDragSession)](./draginteraction%28_,sessionwillbegin%29.md)
  Tells the delegate the lift animation has finished and the user is starting to move the items across the screen.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, willAdd: [UIDragItem], for: UIDragInteraction)](./draginteraction%28_,session,willadd,for%29.md)
  Tells the delegate an interaction is about to add items to a drag session.
- [func dragInteraction(UIDragInteraction, sessionDidMove: any UIDragSession)](./draginteraction%28_,sessiondidmove%29.md)
  Tells the delegate the user moved the drag items to a new location on the screen.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, willEndWith: UIDropOperation)](./draginteraction%28_,session,willendwith%29.md)
  Tells the delegate the drag activity will end with the specified operation.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, didEndWith: UIDropOperation)](./draginteraction%28_,session,didendwith%29.md)
  Tells the delegate the drag activity and its related animations have finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessiondidtransferitems:))*