# dragInteraction(_:sessionIsRestrictedToDraggingApplication:)

**Framework**: Uikit  
**Kind**: method

Asks the delegate whether the system should restrict the drag session to the app that started the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dragInteraction(_ interaction: UIDragInteraction, sessionIsRestrictedToDraggingApplication session: any UIDragSession) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if you want to restrict the drag session to the app that started it; otherwise [`false`](https://developer.apple.com/documentation/swift/false), which is the default if you don’t provide this method.

#### Discussion

If you return [`true`](https://developer.apple.com/documentation/swift/true) and the user attempts to drop the drag items onto another app, the system cancels the session.

> **Note**:  The system calls this method only on devices that support dragging across apps.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drag session to restrict or not restrict.

## See Also

- [func dragInteraction(UIDragInteraction, sessionAllowsMoveOperation: any UIDragSession) -> Bool](uidraginteractiondelegate/draginteraction(_:sessionallowsmoveoperation:).md)
  Asks the delegate whether the session allows the move operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionisrestrictedtodraggingapplication:))*