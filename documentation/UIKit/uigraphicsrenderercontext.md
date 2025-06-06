# UIGraphicsRendererContext

**Framework**: UIKit  
**Kind**: class

The base class for the drawing environments for graphics renderers.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsRendererContext
```

#### Overview

You don’t create instances of [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) yourself. Instead, when you use a concrete subclass of [`UIGraphicsRenderer`](uigraphicsrenderer.md), you are provided an instance of the appropriate [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) subclass—either [`UIGraphicsImageRendererContext`](uigraphicsimagerenderercontext.md) or [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md)—as an argument to a [`UIGraphicsDrawingActions`](uigraphicsdrawingactions.md) drawing actions block.

[`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) objects provide high-level drawing methods in addition to access to the underlying Core Graphics context.

## Topics

### Getting the drawing context
- [var cgContext: CGContext](uigraphicsrenderercontext/cgcontext.md)
  The underlying Core Graphics context.
- [var format: UIGraphicsRendererFormat](uigraphicsrenderercontext/format.md)
  The format used to create the associated graphics renderer.
### Drawing content
- [func stroke(CGRect)](uigraphicsrenderercontext/stroke(_:).md)
  Paints a rectangular path using the currently selected stroke color.
- [func stroke(CGRect, blendMode: CGBlendMode)](uigraphicsrenderercontext/stroke(_:blendmode:).md)
  Paints a rectangular path using the currently selected stroke color and specified blend mode.
- [func fill(CGRect, blendMode: CGBlendMode)](uigraphicsrenderercontext/fill(_:blendmode:).md)
  Paints a rectangular area with the currently selected fill color using the supplied blend mode.
- [func fill(CGRect)](uigraphicsrenderercontext/fill(_:).md)
  Paints a rectangular area with the currently selected fill color.
### Applying a clipping rectangle
- [func clip(to: CGRect)](uigraphicsrenderercontext/clip(to:).md)
  Sets the clipping mask for the drawing context to the specified rectangle.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md)
- [UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class UIGraphicsRenderer](uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
- [class UIGraphicsRendererFormat](uigraphicsrendererformat.md)
  A set of drawing attributes that represents the configuration of a graphics renderer context.
- [class UIGraphicsImageRenderer](uigraphicsimagerenderer.md)
  A graphics renderer for creating Core Graphics-backed images.
- [class UIGraphicsImageRendererContext](uigraphicsimagerenderercontext.md)
  The drawing environment for an image renderer.
- [class UIGraphicsImageRendererFormat](uigraphicsimagerendererformat.md)
  A set of drawing attributes that represents the configuration of an image renderer context.
- [class UIGraphicsPDFRenderer](uigraphicspdfrenderer.md)
  A graphics renderer for creating PDFs.
- [class UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.
- [class UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrenderercontext)*