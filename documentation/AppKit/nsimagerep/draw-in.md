# draw(in:)

**Framework**: AppKit  
**Kind**: method

Draws the image, scaling it (as needed) to fit the specified rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func draw(in rect: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the image was successfully drawn; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). If the size of the image has not yet been set, this method returns [`false`](https://developer.apple.com/documentation/swift/false) immediately.

#### Discussion

This method sets the origin of the current coordinate system to the origin of the specified rectangle before invoking the receiver’s [`draw()`](nsimagerep/draw().md) method. If the rectangle size is different from the image’s native size, this method adjusts the coordinate transform, causing the image to be scaled appropriately.  After the `draw` method returns, the coordinate system changes are undone, restoring the original graphics state.

## Parameters

- `rect`: The rectangle in the current coordinate system in which to draw the image.

## See Also

- [func draw() -> Bool](nsimagerep/draw.md)
  Implemented by subclasses to draw the image in the current coordinate system.
- [func draw(at: NSPoint) -> Bool](nsimagerep/draw(at:).md)
  Draws the image representation’s image data at the specified point in the current coordinate system.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool](nsimagerep/draw(in:from:operation:fraction:respectflipped:hints:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/draw(in:))*