# draw(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the image, scaling it (as needed) to fit the specified rectangle.

**Availability**:
- macOS

## Declaration

```swift
func draw(in rect: NSRect) -> Bool
```

```objc
- (BOOL) drawInRect:(NSRect) rect;
```

## Return Value

[`true`](../../Swift/true.md) if the image was successfully drawn; otherwise, [`false`](../../Swift/false.md). If the size of the image has not yet been set, this method returns [`false`](../../Swift/false.md) immediately.

## Discussion

This method sets the origin of the current coordinate system to the origin of the specified rectangle before invoking the receiver’s [`draw()`](./draw%28%29.md) method. If the rectangle size is different from the image’s native size, this method adjusts the coordinate transform, causing the image to be scaled appropriately.  After the `draw` method returns, the coordinate system changes are undone, restoring the original graphics state.

## Parameters

- `rect`: The rectangle in the current coordinate system in which to draw the image.

## See Also

### Drawing Images
- [func draw() -> Bool](./draw%28%29.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [func draw(at: NSPoint) -> Bool](./draw%28at%29.md)
  Draws the image representation’s image data at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool](./draw%28in,from,operation,fraction,respectflipped,hints%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [NSImageRep.HintKey](./hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/draw(in:))*