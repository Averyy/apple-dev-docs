# newFrameEventHandler

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A handler that the framework calls when the guest environment has a new frame to display.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var newFrameEventHandler: PGDisplayNewFrameEventHandler? { get }
```

```objc
@property (nonatomic, readonly, nullable) PGDisplayNewFrameEventHandler newFrameEventHandler;
```

## See Also

### Inspecting the Display Handlers
- [var queue: dispatch_queue_t?](./queue.md)
  The queue that the framework uses when dispatching messages to any of the display’s registered handlers.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](./cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [var modeChangeHandler: PGDisplayModeChangeHandler?](./modechangehandler.md)
  A handler that the framework calls to change the virtual display’s graphics mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/newframeeventhandler)*