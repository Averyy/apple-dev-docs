# QCPlugInInputImageSource

**Framework**: Quartz  
**Kind**: protocol

The `QCPlugInInputImageSource` protocol eliminates the need to use explicit image types for the image input ports on your custom patch. Not only does using the protocol avoid restrictions of a specific image type, but it avoids impedance mismatches, and provides better performance by deferring pixel computation until it is needed. When you need to access the pixels in an image, you simply convert the image to a representation (texture or buffer) using one of the methods defined by the `QCPlugInInputImageSource` protocol. Use a texture representation when you want to use input images on the GPU. Use a buffer representation when you want to use input images on the CPU.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol QCPlugInInputImageSource
```

#### Overview

Input images are opaque source objects that comply to this protocol. To create an image input port as an Objective-C 2.0 property, declare it as follows:

```objc
@property(dynamic) id<QCPlugInInputImageSource> inputImage;
```

To create an image input port dynamically. use the type `QCPortTypeImage`:

```objc
[self addInputPortWithType:QCPortTypeImage
                    forKey:@"inputImage"
            withAttributes:nil];
```

## Topics

### Converting an Image to a Representation
- [func lockTextureRepresentation(with: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/locktexturerepresentation(with:forbounds:).md)
  Creates an OpenGL texture representation from a subregion of the image source using the provided color space.
- [func unlockTextureRepresentation()](qcplugininputimagesource/unlocktexturerepresentation.md)
  Releases the OpenGL texture representation of the image source.
- [func lockBufferRepresentation(withPixelFormat: String!, colorSpace: CGColorSpace!, forBounds: NSRect) -> Bool](qcplugininputimagesource/lockbufferrepresentation(withpixelformat:colorspace:forbounds:).md)
  Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.
- [func bindTextureRepresentation(toCGLContext: CGLContextObj!, textureUnit: GLenum, normalizeCoordinates: Bool)](qcplugininputimagesource/bindtexturerepresentation(tocglcontext:textureunit:normalizecoordinates:).md)
  Binds the texture to a given texture unit and optionally scales or flips the texture.
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](qcplugininputimagesource/unbindtexturerepresentation(fromcglcontext:textureunit:).md)
  Unbinds the texture from a texture unit.
- [func unlockBufferRepresentation()](qcplugininputimagesource/unlockbufferrepresentation.md)
  Releases the memory buffer representation of the image source.
### Getting Color Space Information
- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/imagecolorspace.md)
  Returns the color space of the image source.
- [func shouldColorMatch() -> Bool](qcplugininputimagesource/shouldcolormatch.md)
  Returns whether or not the image source should be color matched.
### Getting Texture Information
- [func texturePixelsWide() -> Int](qcplugininputimagesource/texturepixelswide.md)
  Returns the width of the texture representation.
- [func texturePixelsHigh() -> Int](qcplugininputimagesource/texturepixelshigh.md)
  Returns the height of the texture representation.
- [func textureTarget() -> GLenum](qcplugininputimagesource/texturetarget.md)
  Returns the texture target.
- [func textureName() -> GLuint](qcplugininputimagesource/texturename.md)
  Returns the texture name.
- [func textureColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/texturecolorspace.md)
  Returns the color space of the texture representation.
- [func textureFlipped() -> Bool](qcplugininputimagesource/textureflipped.md)
  Returns whether or not the contents of the texture are flipped vertically.
- [func textureMatrix() -> UnsafePointer<GLfloat>!](qcplugininputimagesource/texturematrix.md)
  Returns a texture matrix.
### Getting Image Buffer Information
- [func imageBounds() -> NSRect](qcplugininputimagesource/imagebounds.md)
  Returns the actual bounds of the image source expressed in pixels and aligned to integer boundaries.
- [func bufferPixelsWide() -> Int](qcplugininputimagesource/bufferpixelswide.md)
  Returns the width of the image buffer representation.
- [func bufferPixelsHigh() -> Int](qcplugininputimagesource/bufferpixelshigh.md)
  Returns the height of the image buffer representation.
- [func bufferPixelFormat() -> String!](qcplugininputimagesource/bufferpixelformat.md)
  Returns the pixel format of the image buffer representation.
- [func bufferColorSpace() -> Unmanaged<CGColorSpace>!](qcplugininputimagesource/buffercolorspace.md)
  Returns the color space of the image buffer representation.
- [func bufferBaseAddress() -> UnsafeRawPointer!](qcplugininputimagesource/bufferbaseaddress.md)
  Returns the base address of the image buffer.
- [func bufferBytesPerRow() -> Int](qcplugininputimagesource/bufferbytesperrow.md)
  Returns the  bytes per row of the buffer representation.

## See Also

- [QCCompositionParameterViewDelegate](qccompositionparameterviewdelegate.md)
  A protocol for composition parameter view’s delegate.
- [QCCompositionPickerViewDelegate](qccompositionpickerviewdelegate.md)
  The `QCCompositionPickerViewDelegate` informal protocol defines methods that allow  your application to respond to changes in a composition picker view (a [`QCCompositionPickerView`](qccompositionpickerview.md) object).
- [protocol QCCompositionRenderer](qccompositionrenderer.md)
  The `QCRenderer` protocol defines the methods used to pass data to the input ports or retrieve data from the output ports of the root patch of a Quartz Composer composition. This protocol is adopted by the [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), and [`QCCompositionLayer`](qccompositionlayer.md) classes.
- [protocol QCPlugInContext](qcplugincontext.md)
  The `QCPlugInContext` protocol defines methods that you use only from within the execution method ([`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md)) of a `QCPlugIn` object.
- [protocol QCPlugInOutputImageProvider](qcpluginoutputimageprovider.md)
  The `QCPlugInOuputImageProvider` protocol eliminates the need to use explicit image types for the image output ports on a custom patch. The methods in this protocol are called by the Quartz Composer engine when the output image is needed. If your custom patch has an image output port, you need to implement the appropriate methods for rendering image data and to supply information about the rendering destination and the image bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource)*