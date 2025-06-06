# draw(_:)

**Framework**: Screen Saver  
**Kind**: method

Draws the screen saver view.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func draw(_ rect: NSRect)
```

#### Discussion

[`ScreenSaverView`](screensaverview.md) implements [`draw(_:)`](screensaverview/draw(_:).md) to draw a black background. Subclasses can do their drawing here or in [`animateOneFrame()`](screensaverview/animateoneframe().md).

## See Also

- [var isPreview: Bool](screensaverview/ispreview.md)
  A Boolean value that indicates whether the screen saver view is set to a size suitable for previewing its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screensaver/screensaverview/draw(_:))*