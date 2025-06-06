# QCPlugInOutputImageProvider

**Framework**: Quartz  
**Kind**: protocol

The `QCPlugInOuputImageProvider` protocol eliminates the need to use explicit image types for the image output ports on a custom patch. The methods in this protocol are called by the Quartz Composer engine when the output image is needed. If your custom patch has an image output port, you need to implement the appropriate methods for rendering image data and to supply information about the rendering destination and the image bounds.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol QCPlugInOutputImageProvider
```

#### Overview

Output images are opaque provider objects that comply to this protocol. To create an image output port as an Objective-C 2.0 property, declare it as follows:

```objc
@property(dynamic) id<QCPlugInOutputImageProvider> outputImage;
```

To create an image input port dynamically use the type `QCPortTypeImage`:

```objc
[self addOutputPortWithType:QCPortTypeImage
                    forKey:@"outputImage"
            withAttributes:nil];
```

To write images to that port, you need to implement the methods in this protocol and create an internal class that represents the images produced by the custom patch. For example, a simple interface for an image provider is:

```objc
@interface MyOutputImage : NSObject <QCPlugInOutputImageProvider>
{
    NSUInteger _width;
    NSUInteger _height;
}
```

## Topics

### Rendering an Image to a Destination
- [func render(toBuffer: UnsafeMutableRawPointer!, withBytesPerRow: Int, pixelFormat: String!, forBounds: NSRect) -> Bool](qcpluginoutputimageprovider/render(tobuffer:withbytesperrow:pixelformat:forbounds:).md)
  Renders a subregion of the image into  the supplied memory buffer using the specified pixel format.
- [func copyRenderedTexture(forCGLContext: CGLContextObj!, pixelFormat: String!, bounds: NSRect, isFlipped: UnsafeMutablePointer<ObjCBool>!) -> GLuint](qcpluginoutputimageprovider/copyrenderedtexture(forcglcontext:pixelformat:bounds:isflipped:).md)
  Returns the name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format.
- [func render(withCGLContext: CGLContextObj!, forBounds: NSRect) -> Bool](qcpluginoutputimageprovider/render(withcglcontext:forbounds:).md)
  Renders a subregion of the image to the provided CGL context.
- [func releaseRenderedTexture(GLuint, forCGLContext: CGLContextObj!)](qcpluginoutputimageprovider/releaserenderedtexture(_:forcglcontext:).md)
  Releases the previously copied texture.
### Providing Information About the Image
- [func imageBounds() -> NSRect](qcpluginoutputimageprovider/imagebounds.md)
  Returns the bounds of the image expressed in pixels and aligned to integer boundaries.
- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](qcpluginoutputimageprovider/imagecolorspace.md)
  Returns the color space of the image or `NULL` if the image should not be color matched.
- [func shouldColorMatch() -> Bool](qcpluginoutputimageprovider/shouldcolormatch.md)
  Returns whether the image should be color matched.
### Providing Information About the Rendering Destination
- [func supportedBufferPixelFormats() -> [Any]!](qcpluginoutputimageprovider/supportedbufferpixelformats.md)
  Returns a list of pixel formats that are supported for rendering to a memory buffer.
- [func supportedRenderedTexturePixelFormats() -> [Any]!](qcpluginoutputimageprovider/supportedrenderedtexturepixelformats.md)
  Returns a list of pixel formats that are supported for rendering to an onscreen OpenGL context.
- [func canRender(withCGLContext: CGLContextObj!) -> Bool](qcpluginoutputimageprovider/canrender(withcglcontext:).md)
  Returns whether the image data can be rendered into the provided CGL context.

## See Also

- [QCCompositionParameterViewDelegate](qccompositionparameterviewdelegate.md)
  A protocol for composition parameter view’s delegate.
- [QCCompositionPickerViewDelegate](qccompositionpickerviewdelegate.md)
  The `QCCompositionPickerViewDelegate` informal protocol defines methods that allow  your application to respond to changes in a composition picker view (a [`QCCompositionPickerView`](qccompositionpickerview.md) object).
- [protocol QCCompositionRenderer](qccompositionrenderer.md)
  The `QCRenderer` protocol defines the methods used to pass data to the input ports or retrieve data from the output ports of the root patch of a Quartz Composer composition. This protocol is adopted by the [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), and [`QCCompositionLayer`](qccompositionlayer.md) classes.
- [protocol QCPlugInContext](qcplugincontext.md)
  The `QCPlugInContext` protocol defines methods that you use only from within the execution method ([`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md)) of a `QCPlugIn` object.
- [protocol QCPlugInInputImageSource](qcplugininputimagesource.md)
  The `QCPlugInInputImageSource` protocol eliminates the need to use explicit image types for the image input ports on your custom patch. Not only does using the protocol avoid restrictions of a specific image type, but it avoids impedance mismatches, and provides better performance by deferring pixel computation until it is needed. When you need to access the pixels in an image, you simply convert the image to a representation (texture or buffer) using one of the methods defined by the `QCPlugInInputImageSource` protocol. Use a texture representation when you want to use input images on the GPU. Use a buffer representation when you want to use input images on the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider)*