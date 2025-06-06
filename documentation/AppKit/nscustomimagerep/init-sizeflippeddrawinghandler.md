# init(size:flipped:drawingHandler:)

**Framework**: AppKit  
**Kind**: init

Initializes a representation of an image of the specified size and flipped status, using a block to draw its content.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(size: NSSize, flipped drawingHandlerShouldBeCalledWithFlippedContext: Bool, drawingHandler: @escaping (NSRect) -> Bool)
```

#### Return Value

An initialized [`NSCustomImageRep`](nscustomimagerep.md) object, or `nil` if the object could not be initialized.

#### Discussion

Using the this method ensures you’ll get correct results under standard and high resolution.

Like other non-bitmap image rep types, drawing is cached as appropriate for the destination context. Practically speaking, the `drawingHandler` block will be invoked the first time the image is drawn to a particular type of destination (1x or 2x screen, for example). Subsequent drawing operations to the same type of destination will reuse the previously generated bitmap.

## Parameters

- `size`: The size of the image.
- `drawingHandlerShouldBeCalledWithFlippedContext`:   if the drawing handler should be called with a flipped graphics context; otherwise  .
- `drawingHandler`: This Block replaces the   and   technique of creating drawing content. The block is invoked at draw time, the drawing can be adjusted to suit the destination’s pixel density, color space, and other properties.

## See Also

- [var drawingHandler: ((NSRect) -> Bool)?](nscustomimagerep/drawinghandler.md)
  The destination rectangle of the drawing handler block.
- [init(draw: Selector, delegate: Any)](nscustomimagerep/init(draw:delegate:).md)
  Returns a representation of an image initialized with the specified delegate information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomimagerep/init(size:flipped:drawinghandler:))*