# dropInteraction(_:sessionDidEnter:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate the drop session has moved into the drop interaction’s view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dropInteraction(_ interaction: UIDropInteraction, sessionDidEnter session: any UIDropSession)
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drop session that has moved into the interaction’s view.

## See Also

- [func dropInteraction(UIDropInteraction, sessionDidUpdate: any UIDropSession) -> UIDropProposal](uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:).md)
  Tells the delegate the drop session has changed.
- [func dropInteraction(UIDropInteraction, sessionDidExit: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:sessiondidexit:).md)
  Tells the delegate the drop session has moved out of the drop interaction’s view.
- [func dropInteraction(UIDropInteraction, sessionDidEnd: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:sessiondidend:).md)
  Tells the delegate the drop session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidenter:))*