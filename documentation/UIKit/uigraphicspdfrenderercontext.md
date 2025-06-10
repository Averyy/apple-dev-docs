# UIGraphicsPDFRendererContext

**Framework**: UIKit  
**Kind**: class

The drawing environment for a PDF renderer.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsPDFRendererContext
```

#### Overview

When using the [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md) drawing methods, you must pass a block of type [`UIGraphicsPDFRenderer.DrawingActions`](uigraphicspdfrenderer/drawingactions.md) as an argument, which provides a [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md) instance as an argument. Use the context object to access high-level drawing functions and the underlying Core Graphics context.

> **Note**:  [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md) inherits much of its functionality from its abstract superclass [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md).

To learn how to use a [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md) object in combination with a PDF renderer, see [`Creating a graphics PDF renderer`](uigraphicspdfrenderer#Creating-a-graphics-PDF-renderer.md).

## Topics

### Marking new pages
- [func beginPage()](uigraphicspdfrenderercontext/beginpage.md)
  Marks the beginning of a new page in the PDF context and configures it using default values.
- [func beginPage(withBounds: CGRect, pageInfo: [String : Any])](uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:).md)
  Marks the beginning of a new page in the PDF context and configures it using the specified values.
### Getting the PDF bounds
- [var pdfContextBounds: CGRect](uigraphicspdfrenderercontext/pdfcontextbounds.md)
  The bounds of the PDF context for the current page.
### Managing destinations
- [func addDestination(withName: String, at: CGPoint)](uigraphicspdfrenderercontext/adddestination(withname:at:).md)
  Creates a named destination point in the current PDF page.
- [func setDestinationWithName(String, for: CGRect)](uigraphicspdfrenderercontext/setdestinationwithname(_:for:).md)
  Creates a link rectangle in the current page that jumps the PDF viewer to the named destination when clicked.
- [func setURL(URL, for: CGRect)](uigraphicspdfrenderercontext/seturl(_:for:).md)
  Creates a link to an external resource defined by a URL

## Relationships

### Inherits From
- [UIGraphicsRendererContext](uigraphicsrenderercontext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIGraphicsRenderer](uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
- [class UIGraphicsRendererContext](uigraphicsrenderercontext.md)
  The base class for the drawing environments for graphics renderers.
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
- [class UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderercontext)*