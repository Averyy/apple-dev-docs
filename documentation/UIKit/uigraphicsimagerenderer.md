# UIGraphicsImageRenderer

**Framework**: UIKit  
**Kind**: class

A graphics renderer for creating Core Graphics-backed images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class UIGraphicsImageRenderer
```

## Mentions

- [Adding Writing Tools support to a custom UIKit view](adding-writing-tools-support-to-a-custom-uiview.md)

#### Overview

You can use image renderers to accomplish drawing tasks, without having to handle configuration such as color depth and image scale, or manage Core Graphics contexts. You initialize an image renderer with parameters such as image output dimensions and format. You then use one or more of the drawing functions to render images that share these properties.

To render an image:

1. Optionally, create a [`UIGraphicsImageRendererFormat`](uigraphicsimagerendererformat.md) object to specify nondefault parameters the renderer should use to create its context.
2. Instantiate a [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) object, providing the dimensions of the output image and a format object. The renderer uses default values for the current device if you don’t provide format object, as demonstrated in [`Creating a graphics image renderer`](uigraphicsimagerenderer#Creating-a-graphics-image-renderer.md).
3. Choose one of the rendering methods depending on the output you desire: [`image(actions:)`](uigraphicsimagerenderer/image(actions:).md) returns a [`UIImage`](uiimage.md) object; [`jpegData(withCompressionQuality:actions:)`](uigraphicsimagerenderer/jpegdata(withcompressionquality:actions:).md) returns a JPEG-encoded [`Data`](https://developer.apple.com/documentation/Foundation/Data) object; and [`pngData(actions:)`](uigraphicsimagerenderer/pngdata(actions:).md) returns a PNG-encoded [`Data`](https://developer.apple.com/documentation/Foundation/Data) object.
4. Execute your chosen method, providing Core Graphics drawing instructions as the closure argument, as shown in [`Creating an image with an image renderer`](uigraphicsimagerenderer#Creating-an-image-with-an-image-renderer.md). [`Using blend mode`](uigraphicsimagerenderer#Using-blend-mode.md) demonstrates some of the more advanced rendering features you can use in your drawing instructions.
5. Optionally, you can use Core Graphics drawing code within the drawing instructions you provide to the rendering method, as shown in [`Using Core Graphics rendering functions`](uigraphicsimagerenderer#Using-Core-Graphics-rendering-functions.md).

After initializing an image renderer, you can use it to draw multiple images with the same configuration. An image renderer keeps a cache of Core Graphics contexts, so reusing the same renderer can be more efficient than creating new renderers.

##### Creating a Graphics Image Renderer

Create an image renderer, providing the size of the output image:

You can instead use one of the other [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) initializers to specify a renderer format ([`UIGraphicsImageRendererFormat`](uigraphicsimagerendererformat.md)) in addition to the size. This allows you to configure the underlying Core Graphics context for wide color and retina images.

If you don’t provide a format, the renderer uses the [`default()`](uigraphicsrendererformat/default().md) format, which creates a context best suited for the current device.

##### Creating an Image with an Image Renderer

Use the [`image(actions:)`](uigraphicsimagerenderer/image(actions:).md) method to create an image ([`UIImage`](uiimage.md) object) with an image renderer. This method takes a closure that represents the drawing actions. Within this closure, the renderer creates a Core Graphics context using the parameters provided during renderer initialization, and sets this Core Graphics context to be the current context.

The drawing actions closure takes a single argument of type [`UIGraphicsImageRendererContext`](uigraphicsimagerenderercontext.md). This provides access to some high-level drawing functions, such as [`fill(_:)`](uigraphicsrenderercontext/fill(_:).md), through the [`UIGraphicsRendererContext`](uigraphicsrenderercontext.md) superclass.

The above code creates the following image:

![Image showing a blue square in the top left of a larger white squares](https://docs-assets.developer.apple.com/published/120452bcd4ba5d1e1217df3088cb4c20/media-2874999%402x.png)

In addition to the [`image(actions:)`](uigraphicsimagerenderer/image(actions:).md) method that creates an [`UIImage`](uiimage.md) object, [`UIGraphicsImageRenderer`](uigraphicsimagerenderer.md) also has [`jpegData(withCompressionQuality:actions:)`](uigraphicsimagerenderer/jpegdata(withcompressionquality:actions:).md) and [`pngData(actions:)`](uigraphicsimagerenderer/pngdata(actions:).md) methods that create [`Data`](https://developer.apple.com/documentation/Foundation/Data) objects containing the image encoded as a JPEG or a PNG respectively. All three methods take the same approach as detailed here, accepting a block that represents the drawing actions.

##### Using Blend Mode

The utility methods on [`UIGraphicsImageRendererContext`](uigraphicsimagerenderercontext.md) also offer a variant that accepts a [`CGBlendMode`](https://developer.apple.com/documentation/CoreGraphics/CGBlendMode) value. This value determines how to combine the pixel values when painting.

This code draws a second square, using a blend mode of multiply. The following image shows the result.

![Image showing two overlapping squares, one blue, the other turquoise, in the top-left and bottom-right of a white background square respectively.](https://docs-assets.developer.apple.com/published/80b9801ced2dfb67ba11c15a666db490/media-2875000%402x.png)

##### Using Core Graphics Rendering Functions

The [`UIGraphicsImageRendererContext`](uigraphicsimagerenderercontext.md) available in the image closure has a [`cgContext`](uigraphicsrenderercontext/cgcontext.md) property, which allows you to use Core Graphics rendering functions directly. For example, the following code demonstrates how to add a circle to the image:

This code uses the [`fillEllipse(in:)`](https://developer.apple.com/documentation/CoreGraphics/CGContext/fillEllipse(in:)) method on [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext) to draw a green circle on the blue and turquoise squares image; the following image shows the result.

![An image showing two overlapping squares and an overlaid green circle.](https://docs-assets.developer.apple.com/published/4493395a1867556cb03a84fee2c59ed7/media-2875001%402x.png)

## Topics

### Initializing an image renderer
- [init(bounds: CGRect, format: UIGraphicsImageRendererFormat)](uigraphicsimagerenderer/init(bounds:format:).md)
  Creates an image renderer with the specified bounds and format.
- [convenience init(size: CGSize)](uigraphicsimagerenderer/init(size:).md)
  Creates an image renderer for drawing images of the specified size.
- [init(size: CGSize, format: UIGraphicsImageRendererFormat)](uigraphicsimagerenderer/init(size:format:).md)
  Creates an image renderer with the specified size and format.
### Creating images
- [func image(actions: (UIGraphicsImageRendererContext) -> Void) -> UIImage](uigraphicsimagerenderer/image(actions:).md)
  Creates an image from a set of drawing instructions.
- [func jpegData(withCompressionQuality: CGFloat, actions: (UIGraphicsImageRendererContext) -> Void) -> Data](uigraphicsimagerenderer/jpegdata(withcompressionquality:actions:).md)
  Creates a JPEG-encoded image from a set of drawing instructions.
- [func pngData(actions: (UIGraphicsImageRendererContext) -> Void) -> Data](uigraphicsimagerenderer/pngdata(actions:).md)
  Creates a PNG-encoded image from a set of drawing instructions.
- [UIGraphicsImageRenderer.DrawingActions](uigraphicsimagerenderer/drawingactions.md)
  A closure for drawing an image.

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

## See Also

- [class UIGraphicsRenderer](uigraphicsrenderer.md)
  An abstract base class for creating graphics renderers.
- [class UIGraphicsRendererContext](uigraphicsrenderercontext.md)
  The base class for the drawing environments for graphics renderers.
- [class UIGraphicsRendererFormat](uigraphicsrendererformat.md)
  A set of drawing attributes that represents the configuration of a graphics renderer context.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer)*