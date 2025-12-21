# draw(at:)

**Framework**: AppKit  
**Kind**: method

Draws the image representation’s image data at the specified point in the current coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
func draw(at point: NSPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the image was successfully drawn; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false). If the size of the image has not yet been set, this method returns [`false`](https://developer.apple.com/documentation/Swift/false) immediately

#### Discussion

This method sets the origin of the current coordinate system to the specified point and then invokes the receiver’s `draw` method to draw the image at that point. Upon completion, it restores the current coordinates to their original setting. If `aPoint` is (0.0, 0.0), this method simply invokes the [`draw()`](nsimagerep/draw().md) method.

## Parameters

- `point`: The point in the current coordinate system at which to draw the image.

## See Also

- [func draw() -> Bool](nsimagerep/draw.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [func draw(in: NSRect) -> Bool](nsimagerep/draw(in:).md)
  Draws the image, scaling it (as needed) to fit the specified rectangle.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool](nsimagerep/draw(in:from:operation:fraction:respectflipped:hints:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/draw(at:))*