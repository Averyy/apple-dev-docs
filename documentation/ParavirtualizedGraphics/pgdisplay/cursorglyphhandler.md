# cursorGlyphHandler

**Framework**: Paravirtualized Graphics  
**Kind**: property  
**Role**: Instance Property

A handler that the framework calls to change the cursor’s appearance.

**Availability**:
- Mac Catalyst 14.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) PGDisplayCursorGlyphHandler cursorGlyphHandler;
```

## See Also

### Inspecting the Display Handlers
- [var queue: dispatch_queue_t?](./queue.md)
  The queue that the framework uses when dispatching messages to any of the display’s registered handlers.
- [var cursorShowHandler: PGDisplayCursorShowHandler?](./cursorshowhandler.md)
  A handler that the framework calls to change the cursor’s visibility.
- [var modeChangeHandler: PGDisplayModeChangeHandler?](./modechangehandler.md)
  A handler that the framework calls to change the virtual display’s graphics mode.
- [var newFrameEventHandler: PGDisplayNewFrameEventHandler?](./newframeeventhandler.md)
  A handler that the framework calls when the guest environment has a new frame to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdisplay/cursorglyphhandler)*