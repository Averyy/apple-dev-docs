# draw(_:)

**Framework**: Screen Saver  
**Kind**: method  
**Role**: Instance Method

Draws the screen saver view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func draw(_ rect: NSRect)
```

```objc
- (void) drawRect:(NSRect) rect;
```

#### Discussion

[`ScreenSaverView`](../screensaverview.md) implements [`draw(_:)`](./draw%28_%29.md) to draw a black background. Subclasses can do their drawing here or in [`animateOneFrame()`](./animateoneframe%28%29.md).

## See Also

### Drawing the view
- [var isPreview: Bool](./ispreview.md)
  A Boolean value that indicates whether the screen saver view is set to a size suitable for previewing its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/draw(_:))*