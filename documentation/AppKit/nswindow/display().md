# display()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.

**Availability**:
- macOS

## Declaration

```swift
func display()
```

```objc
- (void) display;
```

#### Discussion

You rarely need to invoke this method. `NSWindow` objects normally record which of their views need displaying and display them automatically on each pass through the event loop.

This method includes the frame view that draws the border, title bar, and other peripheral elements.

## See Also

### Drawing Windows
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var viewsNeedDisplay: Bool](./viewsneeddisplay.md)
  A Boolean value that indicates whether any of the window’s views need to be displayed.
- [var allowsConcurrentViewDrawing: Bool](./allowsconcurrentviewdrawing.md)
  A Boolean value that indicates whether the window allows multithreaded view drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/display())*