# allowsConcurrentViewDrawing

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window allows multithreaded view drawing.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var allowsConcurrentViewDrawing: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the window allows multithreaded view drawing; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). The default value is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func display()](nswindow/display.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
- [func displayIfNeeded()](nswindow/displayifneeded.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var viewsNeedDisplay: Bool](nswindow/viewsneeddisplay.md)
  A Boolean value that indicates whether any of the window’s views need to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/allowsconcurrentviewdrawing)*