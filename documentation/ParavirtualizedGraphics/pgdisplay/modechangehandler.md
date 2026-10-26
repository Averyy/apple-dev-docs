# modeChangeHandler

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A handler that the framework calls to change the virtual display’s graphics mode.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var modeChangeHandler: PGDisplayModeChangeHandler? { get }
```

```objc
@property (nonatomic, readonly, nullable) PGDisplayModeChangeHandler modeChangeHandler;
```

## See Also

### Inspecting the Display Handlers
- [var queue: dispatch_queue_t?](./queue.md)
  The queue that the framework uses when dispatching messages to any of the display’s registered handlers.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](./cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [var newFrameEventHandler: PGDisplayNewFrameEventHandler?](./newframeeventhandler.md)
  A handler that the framework calls when the guest environment has a new frame to display.
- [cursorGlyphHandler](./cursorglyphhandler.md)
  A handler that the framework calls to change the cursor’s appearance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/modechangehandler)*