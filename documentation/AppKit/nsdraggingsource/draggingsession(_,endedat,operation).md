# draggingSession(_:endedAt:operation:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the dragging session has completed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func draggingSession(_ session: NSDraggingSession, endedAt screenPoint: NSPoint, operation: NSDragOperation)
```

```objc
- (void) draggingSession:(NSDraggingSession *) session endedAtPoint:(NSPoint) screenPoint operation:(NSDragOperation) operation;
```

## Parameters

- `session`: The dragging session.
- `screenPoint`: The point where the drag ended, in screen coordinates.
- `operation`: The drag operation. See [`NSDragOperation`](../nsdragoperation.md) for drag operation types.

## See Also

### Dragging Session Locations
- [func draggingSession(NSDraggingSession, willBeginAt: NSPoint)](./draggingsession%28_,willbeginat%29.md)
  Invoked when the drag will begin.
- [func draggingSession(NSDraggingSession, movedTo: NSPoint)](./draggingsession%28_,movedto%29.md)
  Invoked when the drag moves on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:endedat:operation:))*