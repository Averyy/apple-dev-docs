# draggingSession(_:willBeginAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the drag will begin.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func draggingSession(_ session: NSDraggingSession, willBeginAt screenPoint: NSPoint)
```

```objc
- (void) draggingSession:(NSDraggingSession *) session willBeginAtPoint:(NSPoint) screenPoint;
```

## Parameters

- `session`: The dragging session.
- `screenPoint`: The point where the drag will begin, in screen coordinates.

## See Also

### Dragging Session Locations
- [func draggingSession(NSDraggingSession, movedTo: NSPoint)](./draggingsession%28_,movedto%29.md)
  Invoked when the drag moves on the screen.
- [func draggingSession(NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./draggingsession%28_,endedat,operation%29.md)
  Invoked when the dragging session has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:willbeginat:))*