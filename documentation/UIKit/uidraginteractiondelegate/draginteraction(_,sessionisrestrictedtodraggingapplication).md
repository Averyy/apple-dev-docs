# dragInteraction(_:sessionIsRestrictedToDraggingApplication:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the system should restrict the drag session to the app that started the session.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionIsRestrictedToDraggingApplication session: any UIDragSession) -> Bool
```

```objc
- (BOOL) dragInteraction:(UIDragInteraction *) interaction sessionIsRestrictedToDraggingApplication:(id<UIDragSession>) session;
```

#### Return Value

[`true`](../../Swift/true.md) if you want to restrict the drag session to the app that started it; otherwise [`false`](../../Swift/false.md), which is the default if you don’t provide this method.

#### Discussion

If you return [`true`](../../Swift/true.md) and the user attempts to drop the drag items onto another app, the system cancels the session.

> **Note**:  The system calls this method only on devices that support dragging across apps.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drag session to restrict or not restrict.

## See Also

### Restricting the drag behavior
- [func dragInteraction(UIDragInteraction, sessionAllowsMoveOperation: any UIDragSession) -> Bool](./draginteraction%28_,sessionallowsmoveoperation%29.md)
  Asks the delegate whether the session allows the move operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionisrestrictedtodraggingapplication:))*