# draggingSession(_:movedTo:)

**Framework**: AppKit  
**Kind**: method

Invoked when the drag moves on the screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func draggingSession(_ session: NSDraggingSession, movedTo screenPoint: NSPoint)
```

## Parameters

- `session`: The dragging session.
- `screenPoint`: The point where the drag moved to, in screen coordinates.

## See Also

- [func draggingSession(NSDraggingSession, willBeginAt: NSPoint)](nsdraggingsource/draggingsession(_:willbeginat:).md)
  Invoked when the drag will begin.
- [func draggingSession(NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nsdraggingsource/draggingsession(_:endedat:operation:).md)
  Invoked when the dragging session has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:movedto:))*