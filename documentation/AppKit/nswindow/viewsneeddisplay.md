# viewsNeedDisplay

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether any of the window’s views need to be displayed.

**Availability**:
- macOS

## Declaration

```swift
var viewsNeedDisplay: Bool { get set }
```

```objc
@property BOOL viewsNeedDisplay;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when any of the window’s views need to be displayed; otherwise, [`false`](../../Swift/false.md). You should rarely need to set this property; the `NSView` method [`needsDisplay`](../nsview/needsdisplay.md) and similar methods set it automatically.

## See Also

### Drawing Windows
- [func display()](./display%28%29.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var allowsConcurrentViewDrawing: Bool](./allowsconcurrentviewdrawing.md)
  A Boolean value that indicates whether the window allows multithreaded view drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/viewsneeddisplay)*