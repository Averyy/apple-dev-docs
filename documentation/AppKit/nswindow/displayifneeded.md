# displayIfNeeded()

**Framework**: AppKit  
**Kind**: method

Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func displayIfNeeded()
```

#### Discussion

This method includes the frame view that draws the border, title bar, and other peripheral elements. It’s useful when you want to modify some number of views and then display only the ones that you modified.

You rarely need to invoke this method. `NSWindow` objects normally record which of their views need displaying and display them automatically on each pass through the event loop.

## See Also

- [func display()](nswindow/display.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
- [var viewsNeedDisplay: Bool](nswindow/viewsneeddisplay.md)
  A Boolean value that indicates whether any of the window’s views need to be displayed.
- [var allowsConcurrentViewDrawing: Bool](nswindow/allowsconcurrentviewdrawing.md)
  A Boolean value that indicates whether the window allows multithreaded view drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/displayifneeded())*