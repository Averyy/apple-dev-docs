# draw()

**Framework**: AppKit  
**Kind**: method

Implemented by subclasses to draw the image in the current coordinate system.

**Availability**:
- macOS ?+

## Declaration

```swift
func draw() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the image was successfully drawn; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false) if there was a problem. The default version of this method simply returns [`true`](https://developer.apple.com/documentation/Swift/true).

#### Discussion

Subclass override this method to draw the image using the image data. By the time this method is called, the graphics state is already configured for you to draw the image at location (0.0, 0.0) in the current coordinate system.

The standard Application Kit subclasses all draw the image using the `NSCompositeCopy` composite operation defined in the `Constants` section of `NSImage`. Using the copy operator, the image data overwrites the destination without any blending effects. Transparent (alpha) regions in the source image appear black. To use other composite operations, you must place the representation into an `NSImage` object and use its [`draw(at:from:operation:fraction:)`](nsimage/draw(at:from:operation:fraction:).md) or [`draw(in:from:operation:fraction:)`](nsimage/draw(in:from:operation:fraction:).md) methods.

## See Also

- [func draw(at: NSPoint) -> Bool](nsimagerep/draw(at:).md)
  Draws the image representation’s image data at the specified point in the current coordinate system.
- [func draw(in: NSRect) -> Bool](nsimagerep/draw(in:).md)
  Draws the image, scaling it (as needed) to fit the specified rectangle.
- [func draw(in: NSRect, from: NSRect, operation: NSCompositingOperation, fraction: CGFloat, respectFlipped: Bool, hints: [NSImageRep.HintKey : Any]?) -> Bool](nsimagerep/draw(in:from:operation:fraction:respectflipped:hints:).md)
  Draws all or part of the image in the specified rectangle in the current coordinate system.
- [NSImageRep.HintKey](nsimagerep/hintkey.md)
  Constants for the keys to include in a hints dictionary when drawing the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/draw())*