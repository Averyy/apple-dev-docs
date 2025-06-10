# UIGraphicsPDFRenderer

**Framework**: UIKit  
**Kind**: class

A graphics renderer for creating PDFs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsPDFRenderer
```

#### Overview

You can use PDF renderers to create PDF files, without having to manage Core Graphics contexts.

To render a PDF:

1. Optionally create a [`UIGraphicsPDFRendererFormat`](uigraphicspdfrendererformat.md) object to specify nondefault parameters the renderer should use to create its context.
2. Instantiate a [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md) object, providing the dimensions of the output image and a format object. The renderer uses sensible defaults for the current device if you don’t provide format object, as demonstrated in [`Creating a graphics PDF renderer`](uigraphicspdfrenderer#Creating-a-graphics-PDF-renderer.md).
3. Choose one of the rendering methods depending on your desired output: [`pdfData(actions:)`](uigraphicspdfrenderer/pdfdata(actions:).md) outputs the PDF in the form of a [`Data`](https://developer.apple.com/documentation/Foundation/Data) object, and [`writePDF(to:withActions:)`](uigraphicspdfrenderer/writepdf(to:withactions:).md) saves the PDF as a file directly to disk.
4. Provide Core Graphics drawing instructions within the closure associated with your chosen method, as shown in [`Creating a PDF with a PDF renderer`](uigraphicspdfrenderer#Creating-a-PDF-with-a-PDF-renderer.md).
5. Optionally, you can create a multi-page PDF, using the approach shown in [`Adding pages`](uigraphicspdfrenderer#Adding-pages.md).
6. Optionally, add links to your PDF to make navigation easy, as shown in [`Creating internal links`](uigraphicspdfrenderer#Creating-internal-links.md).

After initializing a PDF renderer, you can use it to draw multiple PDFs with the same configuration.

##### Creating a Graphics Pdf Renderer

Create a PDF renderer, providing the bounds of the PDF page.

You can instead use one of the other [`UIGraphicsPDFRenderer`](uigraphicspdfrenderer.md) initializers to specify a renderer format ([`UIGraphicsPDFRendererFormat`](uigraphicspdfrendererformat.md)) in addition to the bounds. This allows you to configure the underlying Core Graphics context with custom PDF document info. If you don’t provide a format, the renderer uses the [`default()`](uigraphicsrendererformat/default().md) format, which creates a context best suited for the current device.

##### Creating a Pdf with a Pdf Renderer

Use the [`pdfData(actions:)`](uigraphicspdfrenderer/pdfdata(actions:).md) method to create a PDF with the PDF renderer you created above. This takes a block that represents the drawing actions. Within this block, the renderer creates a Core Graphics context using the parameters provided during renderer initialization, and sets this to be the current context.

Before issuing PDF drawing instructions, you must create a page with a call to either the [`beginPage()`](uigraphicspdfrenderercontext/beginpage().md) method or [`beginPage(withBounds:pageInfo:)`](uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:).md) method on the supplied [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md).

The drawing actions closure takes a single argument of type [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md). This provides access to some high-level drawing functions, such as [`fill(_:)`](uigraphicsrenderercontext/fill(_:).md) through the [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) superclass.

> **Note**:  This code uses a drawing method on [`NSString`](https://developer.apple.com/documentation/Foundation/NSString). If you want to create a PDF with more text, consider using [`TextKit`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/iPhoneOSTechOverview/iPhoneOSTechnologies/iPhoneOSTechnologies.html#//apple_ref/doc/uid/TP40007898-CH3-SW11) or [`Core Text`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/LowerLevelText-HandlingTechnologies/LowerLevelText-HandlingTechnologies.html#//apple_ref/doc/uid/TP40009542-CH15-SW3), both of which provide extensive text layout functionality.

The above code creates the following result:

![Image of a PDF open in Preview, with the word “Hello!” rendered in large, black lettering in the top-left.](https://docs-assets.developer.apple.com/published/a1502445dbaa2ddde3045eaa89064476/media-2864001%402x.png)

##### Adding Pages

Add multiple pages to your PDF through repeated calls to the [`beginPage()`](uigraphicspdfrenderercontext/beginpage().md) method on the [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md) provided to the drawing block.

Use the [`beginPage(withBounds:pageInfo:)`](uigraphicspdfrenderercontext/beginpage(withbounds:pageinfo:).md) method instead of the [`beginPage()`](uigraphicspdfrenderercontext/beginpage().md) method if you want to override the default properties for the new page.

This code creates a PDF with three pages, each of which contains the current page number as large text, as shown in the following image.

![Screenshot from Preview showing a 3-page PDF. Each page contains large black lettering which details the current page number.](https://docs-assets.developer.apple.com/published/69c0b1a8802e3a5f9e3d1cd2cfa64c77/media-2864003%402x.png)

##### Creating Internal Links

You can create internal links, known as destinations, in PDFs. A complete link has two components:

- A named destination. This is a point on a PDF page. You create these with the [`addDestination(withName:at:)`](uigraphicspdfrenderercontext/adddestination(withname:at:).md) method on [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md).
- A link region. This is a rectangle on a PDF page, which when tapped, instructs the PDF viewing app to jump to a specific named destination. You create these with the [`setDestinationWithName(_:for:)`](uigraphicspdfrenderercontext/setdestinationwithname(_:for:).md) method on [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md), providing the name of the destination to jump to, and the bounds of the active link region.

The following code demonstrates how to use destinations with a PDF renderer by showing how to create links that jump to the next page.

This code adds large red labels that jump from the current page to the next page when clicked. Each page has a destination with names of the form `page-1`, positioned at the origin. The bounding box for the next-page label is the link to the destination on the following page.

> **Note**:  The [`addDestination(withName:at:)`](uigraphicspdfrenderercontext/adddestination(withname:at:).md) and [`setDestinationWithName(_:for:)`](uigraphicspdfrenderercontext/setdestinationwithname(_:for:).md) methods on [`UIGraphicsPDFRendererContext`](uigraphicspdfrenderercontext.md) use the underlying PDF coordinate space, which has its y-axis flipped with respect to the coordinate system used by Core Graphics. You can translate between the two using the [`userSpaceToDeviceSpaceTransform`](https://developer.apple.com/documentation/CoreGraphics/CGContext/userSpaceToDeviceSpaceTransform) property on [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext), as shown in the code.

The above code results in the following PDF:

![Screenshot from Preview showing a 3-page PDFs with red links entitled “Next Page” at the bottom-right of each page.](https://docs-assets.developer.apple.com/published/9cae1cc7f0812418f8639b4d40da5e94/media-2864256%402x.png)

## Topics

### Creating a PDF renderer
- [init(bounds: CGRect, format: UIGraphicsPDFRendererFormat)](uigraphicspdfrenderer/init(bounds:format:).md)
  Creates a new graphics renderer with the specified bounds and format.
### Managing the PDF data
- [func pdfData(actions: (UIGraphicsPDFRendererContext) -> Void) -> Data](uigraphicspdfrenderer/pdfdata(actions:).md)
  Creates a PDF from a set of drawing instructions and returns it as a data object.
- [func writePDF(to: URL, withActions: (UIGraphicsPDFRendererContext) -> Void) throws](uigraphicspdfrenderer/writepdf(to:withactions:).md)
  Creates a PDF from a set of drawing instructions and saves it to a specified URL.
- [UIGraphicsPDFRenderer.DrawingActions](uigraphicspdfrenderer/drawingactions.md)
  A closure for drawing PDF content.

## Relationships

### Inherits From
- [UIGraphicsRenderer](uigraphicsrenderer.md)
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
- [class UIGraphicsPDFRendererContext](uigraphicspdfrenderercontext.md)
  The drawing environment for a PDF renderer.
- [class UIGraphicsPDFRendererFormat](uigraphicspdfrendererformat.md)
  A set of drawing attributes that represents the configuration of a PDF renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicspdfrenderer)*