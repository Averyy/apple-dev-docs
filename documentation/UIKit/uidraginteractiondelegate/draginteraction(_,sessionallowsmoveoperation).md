# dragInteraction(_:sessionAllowsMoveOperation:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate whether the session allows the move operation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func dragInteraction(_ interaction: UIDragInteraction, sessionAllowsMoveOperation session: any UIDragSession) -> Bool
```

```objc
- (BOOL) dragInteraction:(UIDragInteraction *) interaction sessionAllowsMoveOperation:(id<UIDragSession>) session;
```

#### Return Value

[`true`](../../Swift/true.md) if the session allows moving drag items to the destination view; otherwise [`false`](../../Swift/false.md). The default is [`true`](../../Swift/true.md) if you don’t provide this method.

#### Discussion

The [`UIDropOperation.move`](../uidropoperation/move.md) operation only applies to drop activities within the same app. Drag items dropped onto another app are always copied.

## Parameters

- `interaction`: The interaction that called this method.
- `session`: The drag session that should, or should not, allow the move operation.

## See Also

### Restricting the drag behavior
- [func dragInteraction(UIDragInteraction, sessionIsRestrictedToDraggingApplication: any UIDragSession) -> Bool](./draginteraction%28_,sessionisrestrictedtodraggingapplication%29.md)
  Asks the delegate whether the system should restrict the drag session to the app that started the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidraginteractiondelegate/draginteraction(_:sessionallowsmoveoperation:))*