# dragInteraction(_:sessionDidMove:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate the user moved the drag items to a new location on the screen.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionDidMove session: any UIDragSession)
```

```objc
- (void) dragInteraction:(UIDragInteraction *) interaction sessionDidMove:(id<UIDragSession>) session;
```

## Discussion

To get the new location, call the drag session’s [`location(in:)`](../uidragdropsession/location%28in%29.md) method.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The current drag session.

## See Also

### Monitoring drag progress
- [func dragInteraction(UIDragInteraction, sessionWillBegin: any UIDragSession)](./draginteraction%28_,sessionwillbegin%29.md)
  Tells the delegate the lift animation has finished and the user is starting to move the items across the screen.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, willAdd: [UIDragItem], for: UIDragInteraction)](./draginteraction%28_,session,willadd,for%29.md)
  Tells the delegate an interaction is about to add items to a drag session.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, willEndWith: UIDropOperation)](./draginteraction%28_,session,willendwith%29.md)
  Tells the delegate the drag activity will end with the specified operation.
- [func dragInteraction(UIDragInteraction, session: any UIDragSession, didEndWith: UIDropOperation)](./draginteraction%28_,session,didendwith%29.md)
  Tells the delegate the drag activity and its related animations have finished.
- [func dragInteraction(UIDragInteraction, sessionDidTransferItems: any UIDragSession)](./draginteraction%28_,sessiondidtransferitems%29.md)
  Tells the delegate the destination view has received the data for the drag items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessiondidmove:))*