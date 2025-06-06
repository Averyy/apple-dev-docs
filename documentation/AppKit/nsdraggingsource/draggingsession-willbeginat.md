# draggingSession(_:willBeginAt:)

**Framework**: AppKit  
**Kind**: method

Invoked when the drag will begin.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func draggingSession(_ session: NSDraggingSession, willBeginAt screenPoint: NSPoint)
```

## Parameters

- `session`: The dragging session.
- `screenPoint`: The point where the drag will begin, in screen coordinates.

## See Also

- [func draggingSession(NSDraggingSession, movedTo: NSPoint)](nsdraggingsource/draggingsession(_:movedto:).md)
  Invoked when the drag moves on the screen.
- [func draggingSession(NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](nsdraggingsource/draggingsession(_:endedat:operation:).md)
  Invoked when the dragging session has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:willbeginat:))*