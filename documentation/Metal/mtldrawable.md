# MTLDrawable

**Framework**: Metal  
**Kind**: protocol

A displayable resource that can be rendered or written to.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLDrawable : NSObjectProtocol
```

## Mentions

- [Managing your Metal app window in iPadOS](managing-your-metal-app-window-in-ipados.md)
- [Adjusting for GPU memory bandwidth tradeoffs](adjusting-for-gpu-memory-bandwidth-tradeoffs.md)

#### Overview

Objects that implement this protocol are connected both to the Metal framework and an underlying display system (such as Core Animation) that’s capable of showing content onscreen. You use drawable objects when you want to render images using Metal and present them onscreen.

Don’t implement this protocol yourself; instead, see [`CAMetalLayer`](https://developer.apple.com/documentation/QuartzCore/CAMetalLayer), for a class that can create and manage drawable objects for you.

## Topics

### Identifying the drawable
- [var drawableID: Int](mtldrawable/drawableid.md)
  A positive integer that identifies the drawable.
### Presenting the drawable
- [func present()](mtldrawable/present.md)
  Presents the drawable onscreen as soon as possible.
- [func present(afterMinimumDuration: CFTimeInterval)](mtldrawable/present(afterminimumduration:).md)
  Presents the drawable onscreen as soon as possible after a previous drawable is visible for the specified duration.
- [func present(at: CFTimeInterval)](mtldrawable/present(at:).md)
  Presents the drawable onscreen at a specific host time.
### Getting presentation information
- [func addPresentedHandler(MTLDrawablePresentedHandler)](mtldrawable/addpresentedhandler(_:).md)
  Registers a block of code to be called immediately after the drawable is presented.
- [var presentedTime: CFTimeInterval](mtldrawable/presentedtime.md)
  The host time, in seconds, when the drawable was displayed onscreen.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [typealias MTLDrawablePresentedHandler](mtldrawablepresentedhandler.md)
  A block of code invoked after a drawable is presented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldrawable)*