# cursorGlyphHandler

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Required**: Yes

A handler that the framework calls to change the cursor’s appearance.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var cursorGlyphHandler: PGDisplayCursorGlyphHandler? { get }
```

## See Also

- [var queue: dispatch_queue_t?](pgdisplay/queue.md)
  The queue that the framework uses when dispatching messages to any of the display’s registered handlers.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](pgdisplay/cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [var modeChangeHandler: PGDisplayModeChangeHandler?](pgdisplay/modechangehandler.md)
  A handler that the framework calls to change the virtual display’s graphics mode.
- [var newFrameEventHandler: PGDisplayNewFrameEventHandler?](pgdisplay/newframeeventhandler.md)
  A handler that the framework calls when the guest environment has a new frame to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/cursorglyphhandler)*