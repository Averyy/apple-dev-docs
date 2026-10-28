# draw(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Draws the image representation’s image data at the specified point in the current coordinate system.

**Availability**:
- macOS

## Declaration

```swift
func draw(at point: NSPoint) -> Bool
```

```objc
- (BOOL) drawAtPoint:(NSPoint) point;
```

## Return Value

[`true`](../../Swift/true.md) if the image was successfully drawn; otherwise, [`false`](../../Swift/false.md). If the size of the image has not yet been set, this method returns [`false`](../../Swift/false.md) immediately

## Discussion

This method sets the origin of the current coordinate system to the specified point and then invokes the receiver’s `draw` method to draw the image at that point. Upon completion, it restores the current coordinates to their original setting. If `aPoint` is (0.0, 0.0), this method simply invokes the [`draw()`](./draw%28%29.md) method.

## Parameters

- `point`: The point in the current coordinate system at which to draw the image.

## See Also

### Drawing Images
- [func draw() -> Bool](./draw%28%29.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [func draw(in: NSRect) -> Bool](./draw%28in%29.md)
  Draws the image, scaling it (as needed) to fit the specified rectangle.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool](./draw%28in,from,operation,fraction,respectflipped,hints%29.md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [NSImageRep.HintKey](./hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/draw(at:))*