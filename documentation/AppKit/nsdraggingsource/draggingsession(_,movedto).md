# draggingSession(_:movedTo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when the drag moves on the screen.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
optional func draggingSession(_ session: NSDraggingSession, movedTo screenPoint: NSPoint)
```

```objc
- (void) draggingSession:(NSDraggingSession *) session movedToPoint:(NSPoint) screenPoint;
```

## Parameters

- `session`: The dragging session.
- `screenPoint`: The point where the drag moved to, in screen coordinates.

## See Also

### Dragging Session Locations
- [func draggingSession(NSDraggingSession, willBeginAt: NSPoint)](./draggingsession%28_,willbeginat%29.md)
  Invoked when the drag will begin.
- [func draggingSession(NSDraggingSession, endedAt: NSPoint, operation: NSDragOperation)](./draggingsession%28_,endedat,operation%29.md)
  Invoked when the dragging session has completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingsource/draggingsession(_:movedto:))*