# dropInteraction(_:sessionDidUpdate:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate the drop session has changed.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dropInteraction(_ interaction: UIDropInteraction, sessionDidUpdate session: any UIDropSession) -> UIDropProposal
```

## Mentions

- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)

#### Return Value

A drop proposal that contains the operation the delegate intends to perform. You may return a proposal containing the [`UIDropOperation.move`](uidropoperation/move.md) operation only if the session’s [`allowsMoveOperation`](uidragdropsession/allowsmoveoperation.md) is [`true`](https://developer.apple.com/documentation/swift/true).

#### Discussion

You must implement this method if the drop interaction’s view can accept drop activities. If you don’t provide this method, the view cannot accept any drop activities.

The interaction calls this method when one of the following happens:

- The session enters the area of the drop interaction’s view.
- The session moves inside the area of the drop interaction’s view.
- The user adds a drag item to the session that within the area of the drop interaction’s view.

To get the location of the drop session after it has moved, call the session’s [`location(in:)`](uidragdropsession/location(in:).md) method.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drop session that has changed.

## See Also

- [func dropInteraction(UIDropInteraction, sessionDidEnter: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:sessiondidenter:).md)
  Tells the delegate the drop session has moved into the drop interaction’s view.
- [func dropInteraction(UIDropInteraction, sessionDidExit: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:sessiondidexit:).md)
  Tells the delegate the drop session has moved out of the drop interaction’s view.
- [func dropInteraction(UIDropInteraction, sessionDidEnd: any UIDropSession)](uidropinteractiondelegate/dropinteraction(_:sessiondidend:).md)
  Tells the delegate the drop session has ended.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:sessiondidupdate:))*