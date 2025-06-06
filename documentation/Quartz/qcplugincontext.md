# QCPlugInContext

**Framework**: Quartz  
**Kind**: protocol

The `QCPlugInContext` protocol defines methods that you use only from within the execution method ([`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md)) of a `QCPlugIn` object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol QCPlugInContext
```

## Topics

### Getting the OpenGL Context
- [func cglContextObj() -> CGLContextObj!](qcplugincontext/cglcontextobj.md)
  Returns the destination CGL context to use for OpenGL rendering from within the execution method.
### Getting Execution Context Information
- [func userInfo() -> NSMutableDictionary!](qcplugincontext/userinfo.md)
  Returns a mutable dictionary that contains information that can be shared between all instances of the `QCPlugIn` subclass, running in the same Quartz Composer context.
- [func bounds() -> NSRect](qcplugincontext/bounds.md)
  Returns the bounds of the rendering context.
- [func colorSpace() -> Unmanaged<CGColorSpace>!](qcplugincontext/colorspace.md)
  Returns the color space used by the rendering context.
### Getting an Image Provider
- [func outputImageProviderFromBuffer(withPixelFormat: String!, pixelsWide: Int, pixelsHigh: Int, baseAddress: UnsafeRawPointer!, bytesPerRow: Int, releaseCallback: QCPlugInBufferReleaseCallback!, releaseContext: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> Any!](qcplugincontext/outputimageproviderfrombuffer(withpixelformat:pixelswide:pixelshigh:baseaddress:bytesperrow:releasecallback:releasecontext:colorspace:shouldcolormatch:).md)
  Returns an image provider from a single memory buffer.
- [func outputImageProviderFromTexture(withPixelFormat: String!, pixelsWide: Int, pixelsHigh: Int, name: GLuint, flipped: Bool, releaseCallback: QCPlugInTextureReleaseCallback!, releaseContext: UnsafeMutableRawPointer!, colorSpace: CGColorSpace!, shouldColorMatch: Bool) -> Any!](qcplugincontext/outputimageproviderfromtexture(withpixelformat:pixelswide:pixelshigh:name:flipped:releasecallback:releasecontext:colorspace:shouldcolormatch:).md)
  Returns an image provider from an OpenGL texture.
### Instance Methods
- [func compositionURL() -> URL!](qcplugincontext/compositionurl.md)

## See Also

- [QCCompositionParameterViewDelegate](qccompositionparameterviewdelegate.md)
  A protocol for composition parameter view’s delegate.
- [QCCompositionPickerViewDelegate](qccompositionpickerviewdelegate.md)
  The `QCCompositionPickerViewDelegate` informal protocol defines methods that allow  your application to respond to changes in a composition picker view (a [`QCCompositionPickerView`](qccompositionpickerview.md) object).
- [protocol QCCompositionRenderer](qccompositionrenderer.md)
  The `QCRenderer` protocol defines the methods used to pass data to the input ports or retrieve data from the output ports of the root patch of a Quartz Composer composition. This protocol is adopted by the [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), and [`QCCompositionLayer`](qccompositionlayer.md) classes.
- [protocol QCPlugInInputImageSource](qcplugininputimagesource.md)
  The `QCPlugInInputImageSource` protocol eliminates the need to use explicit image types for the image input ports on your custom patch. Not only does using the protocol avoid restrictions of a specific image type, but it avoids impedance mismatches, and provides better performance by deferring pixel computation until it is needed. When you need to access the pixels in an image, you simply convert the image to a representation (texture or buffer) using one of the methods defined by the `QCPlugInInputImageSource` protocol. Use a texture representation when you want to use input images on the GPU. Use a buffer representation when you want to use input images on the CPU.
- [protocol QCPlugInOutputImageProvider](qcpluginoutputimageprovider.md)
  The `QCPlugInOuputImageProvider` protocol eliminates the need to use explicit image types for the image output ports on a custom patch. The methods in this protocol are called by the Quartz Composer engine when the output image is needed. If your custom patch has an image output port, you need to implement the appropriate methods for rendering image data and to supply information about the rendering destination and the image bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugincontext)*