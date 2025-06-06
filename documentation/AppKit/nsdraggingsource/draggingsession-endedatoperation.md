# draggingSession(_:endedAt:operation:)

**Framework**: AppKit  
**Kind**: method

Invoked when the dragging session has completed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func draggingSession(_ session: NSDraggingSession, endedAt screenPoint: NSPoint, operation: NSDragOperation)
```

## Parameters

- `session`: The dragging session.
- `screenPoint`: The point where the drag ended, in screen coordinates.
- `operation`: The drag operation. See   for drag operation types.

## See Also

- [func draggingSession(NSDraggingSession, willBeginAt: NSPoint)](nsdraggingsource/draggingsession(_:willbeginat:).md)
  Invoked when the drag will begin.
- [func draggingSession(NSDraggingSession, movedTo: NSPoint)](nsdraggingsource/draggingsession(_:movedto:).md)
  Invoked when the drag moves on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:endedat:operation:))*