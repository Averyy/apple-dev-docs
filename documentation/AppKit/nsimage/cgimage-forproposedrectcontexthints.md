# cgImage(forProposedRect:context:hints:)

**Framework**: AppKit  
**Kind**: method

Returns a Core Graphics image based on the contents of the current image object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func cgImage(forProposedRect proposedDestRect: UnsafeMutablePointer<NSRect>?, context referenceContext: NSGraphicsContext?, hints: [NSImageRep.HintKey : Any]?) -> CGImage?
```

#### Return Value

A `CGImageRef`. This may be an existing `CGImage` if one is available. If not, a new `CGImage` is created.

#### Discussion

An `NSImage` is potentially resolution independent, and may have representations that allow it to draw well in many contexts.  A `CGImage` is more like a single pixel-based representation.   This method produces a snapshot of how the `NSImage` would draw if it was asked to draw in the proposed rectangle in the graphics context.

All input parameters are optional.  They provide hints for how to choose among existing [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) objects, or how to create one if there isn’t already a [`CGImage`](https://developer.apple.com/documentation/CoreGraphics/CGImage) available.  The parameters are only hints.

This method is typically called, not overridden.

## Parameters

- `proposedDestRect`: On input, the proposed destination rectangle for drawing the image. If  , it defaults to the smallest pixel-integral rectangle containing {{0,0}, [self size]}.  The   is in user space in the reference context.
- `referenceContext`: A graphics context.
- `hints`: A dictionary of hints that provide more context for selecting or generating a  , and may override properties of the  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/cgimage(forproposedrect:context:hints:))*