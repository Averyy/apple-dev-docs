# allowsConcurrentViewDrawing

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window allows multithreaded view drawing.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var allowsConcurrentViewDrawing: Bool { get set }
```

```objc
@property BOOL allowsConcurrentViewDrawing;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the window allows multithreaded view drawing; otherwise, [`false`](../../Swift/false.md). The default value is [`true`](../../Swift/true.md).

## See Also

### Drawing Windows
- [func display()](./display%28%29.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views within the window.
- [func displayIfNeeded()](./displayifneeded%28%29.md)
  Passes a display message down the window’s view hierarchy, thus redrawing all views that need displaying.
- [var viewsNeedDisplay: Bool](./viewsneeddisplay.md)
  A Boolean value that indicates whether any of the window’s views need to be displayed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/allowsconcurrentviewdrawing)*