# init(size:flipped:drawingHandler:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes a representation of an image of the specified size and flipped status, using a block to draw its content.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(size: NSSize, flipped drawingHandlerShouldBeCalledWithFlippedContext: Bool, drawingHandler: @escaping (NSRect) -> Bool)
```

```objc
- (instancetype) initWithSize:(NSSize) size flipped:(BOOL) drawingHandlerShouldBeCalledWithFlippedContext drawingHandler:(BOOL (^)(NSRect dstRect)) drawingHandler;
```

## Return Value

An initialized [`NSCustomImageRep`](../nscustomimagerep.md) object, or `nil` if the object could not be initialized.

## Discussion

Using the this method ensures you’ll get correct results under standard and high resolution.

Like other non-bitmap image rep types, drawing is cached as appropriate for the destination context. Practically speaking, the `drawingHandler` block will be invoked the first time the image is drawn to a particular type of destination (1x or 2x screen, for example). Subsequent drawing operations to the same type of destination will reuse the previously generated bitmap.

## Parameters

- `size`: The size of the image.
- `drawingHandlerShouldBeCalledWithFlippedContext`: [`true`](../../Swift/true.md) if the drawing handler should be called with a flipped graphics context; otherwise [`false`](../../Swift/false.md).
- `drawingHandler`: A block that draws the image representation content in the provided graphics context.

  The block may be invoked whenever and on whatever thread the image itself is drawn on. Care should be taken to ensure that all state accessed within the drawingHandler block is done so in a thread safe manner.

  This Block replaces the [`lockFocus()`](../nsimage/lockfocus%28%29.md) and [`unlockFocus()`](../nsimage/unlockfocus%28%29.md) technique of creating drawing content. The block is invoked at draw time, the drawing can be adjusted to suit the destination’s pixel density, color space, and other properties.

## See Also

### Related Documentation
- [var drawingHandler: ((NSRect) -> Bool)?](./drawinghandler.md)
  The destination rectangle of the drawing handler block.
### Creating Representations of Images in Custom Formats
- [init(draw: Selector, delegate: Any)](./init%28draw,delegate%29.md)
  Returns a representation of an image initialized with the specified delegate information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomimagerep/init(size:flipped:drawinghandler:))*