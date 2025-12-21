# dragInteraction(_:sessionAllowsMoveOperation:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether the session allows the move operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dragInteraction(_ interaction: UIDragInteraction, sessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the session allows moving drag items to the destination view; otherwise [`false`](https://developer.apple.com/documentation/Swift/false). The default is [`true`](https://developer.apple.com/documentation/Swift/true) if you don’t provide this method.

#### Discussion

The [`UIDropOperation.move`](uidropoperation/move.md) operation only applies to drop activities within the same app. Drag items dropped onto another app are always copied.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drag session that should, or should not, allow the move operation.

## See Also

- [func dragInteraction(UIDragInteraction, sessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](uidraginteractiondelegate/draginteraction(_:sessionisrestrictedtodraggingapplication:).md)
  Asks the delegate whether the system should restrict the drag session to the app that started the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionallowsmoveoperation:))*