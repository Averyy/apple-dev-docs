# display()

**Framework**: AppKit  
**Kind**: method

Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func display()
```

#### Discussion

You rarely need to invoke this method. `NSWindow` objects normally record which of their views need displaying and display them automatically on each pass through the event loop.

This method includes the frame view that draws the border, title bar, and other peripheral elements.

## See Also

- [func displayIfNeeded()](nswindow/displayifneeded.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var viewsNeedDisplay: Bool](nswindow/viewsneeddisplay.md)
  A Boolean value that indicates whether any of the window’s views need to be displayed.
- [var allowsConcurrentViewDrawing: Bool](nswindow/allowsconcurrentviewdrawing.md)
  A Boolean value that indicates whether the window allows multithreaded view drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/display())*