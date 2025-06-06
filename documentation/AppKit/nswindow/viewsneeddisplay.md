# viewsNeedDisplay

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether any of the window’s views need to be displayed.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var viewsNeedDisplay: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when any of the window’s views need to be displayed; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). You should rarely need to set this property; the `NSView` method [`needsDisplay`](nsview/needsdisplay.md) and similar methods set it automatically.

## See Also

- [func display()](nswindow/display.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
- [func displayIfNeeded()](nswindow/displayifneeded.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var allowsConcurrentViewDrawing: Bool](nswindow/allowsconcurrentviewdrawing.md)
  A Boolean value that indicates whether the window allows multithreaded view drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/viewsneeddisplay)*