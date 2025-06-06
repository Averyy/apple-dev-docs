# cgImage(forProposedRect:context:hints:)

**Framework**: AppKit  
**Kind**: method

Returns a Core Graphics image object that captures the drawing of the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func cgImage(forProposedRect proposedDestRect: UnsafeMutablePointer<NSRect>?, context: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> CGImage?
```

#### Return Value

A [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage). This may be an existing [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) if one is available. If not, a new [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) is created.

#### Discussion

An [`NSImage`](nsimage.md) is potentially resolution independent, and may have representations that allow it to draw well in many contexts. A [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) is more like a single pixel-based representation. This method produces a snapshot of how the [`NSImage`](nsimage.md) would draw if it was asked to draw in the proposed rectangle in the graphics context.

All input parameters are optional. They provide hints for how to choose among existing [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) objects, or how to create one if there isn’t already a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) available. The parameters are only hints.

This method is intended as an override point for image representation subclasses that naturally have a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) available. For example, [`NSBitmapImageRep`](nsbitmapimagerep.md) overrides it to return the [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) that naturally backs the representation. You don’t need to override the method except possibly for performance, though. The [`NSImageRep`](nsimagerep.md)-level implementation will produce a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) by making a buffer and calling [`draw()`](nsimagerep/draw().md). That’s likely to be the best possible implementation for reps that aren’t naturally [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage)-backed. The [`draw()`](nsimagerep/draw().md) method remains the only method of [`NSImageRep`](nsimagerep.md) that a subclasser really needs to override.

## Parameters

- `proposedDestRect`: On output, the   may have been altered. This is because a   is necessarily pixel-integral, while an   is not. In order to produce a   for rect   without distortion or double-antialiasing, we may have to produce a 5x5  , and also inflate the  . Drawing the   in the out-value   is the same as drawing the   in the in-value of proposed rect.
- `context`: A graphics context. Can be  .
- `hints`: An optional dictionary of hints that provide more context for selecting or generating the image. See   for a summary of the possible key-value pairs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/cgimage(forproposedrect:context:hints:))*