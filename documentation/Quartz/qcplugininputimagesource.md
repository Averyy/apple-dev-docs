# QCPlugInInputImageSource

**Framework**: Quartz  
**Kind**: protocol  
**Role**: Protocol

The `QCPlugInInputImageSource` protocol eliminates the need to use explicit image types for the image input ports on your custom patch. Not only does using the protocol avoid restrictions of a specific image type, but it avoids impedance mismatches, and provides better performance by deferring pixel computation until it is needed. When you need to access the pixels in an image, you simply convert the image to a representation (texture or buffer) using one of the methods defined by the `QCPlugInInputImageSource` protocol. Use a texture representation when you want to use input images on the GPU. Use a buffer representation when you want to use input images on the CPU.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
protocol QCPlugInInputImageSource
```

```objc
@protocol QCPlugInInputImageSource
```

## Overview

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
- [func lockTextureRepresentation(with: CGColorSpace!, forBounds: NSRect) -> Bool](./qcplugininputimagesource/locktexturerepresentation%28with,forbounds%29.md)
  Creates an OpenGL texture representation from a subregion of the image source using the provided color space.
- [func unlockTextureRepresentation()](./qcplugininputimagesource/unlocktexturerepresentation%28%29.md)
  Releases the OpenGL texture representation of the image source.
- [func lockBufferRepresentation(withPixelFormat: String!, colorSpace: CGColorSpace!, forBounds: NSRect) -> Bool](./qcplugininputimagesource/lockbufferrepresentation%28withpixelformat,colorspace,forbounds%29.md)
  Creates a memory buffer representation from a subregion of the image source using the provided pixel format and color space.
- [func bindTextureRepresentation(toCGLContext: CGLContextObj!, textureUnit: GLenum, normalizeCoordinates: Bool)](./qcplugininputimagesource/bindtexturerepresentation%28tocglcontext,textureunit,normalizecoordinates%29.md)
  Binds the texture to a given texture unit and optionally scales or flips the texture.
- [func unbindTextureRepresentation(fromCGLContext: CGLContextObj!, textureUnit: GLenum)](./qcplugininputimagesource/unbindtexturerepresentation%28fromcglcontext,textureunit%29.md)
  Unbinds the texture from a texture unit.
- [func unlockBufferRepresentation()](./qcplugininputimagesource/unlockbufferrepresentation%28%29.md)
  Releases the memory buffer representation of the image source.
### Getting Color Space Information
- [func imageColorSpace() -> Unmanaged<CGColorSpace>!](./qcplugininputimagesource/imagecolorspace%28%29.md)
  Returns the color space of the image source.
- [func shouldColorMatch() -> Bool](./qcplugininputimagesource/shouldcolormatch%28%29.md)
  Returns whether or not the image source should be color matched.
### Getting Texture Information
- [func texturePixelsWide() -> Int](./qcplugininputimagesource/texturepixelswide%28%29.md)
  Returns the width of the texture representation.
- [func texturePixelsHigh() -> Int](./qcplugininputimagesource/texturepixelshigh%28%29.md)
  Returns the height of the texture representation.
- [func textureTarget() -> GLenum](./qcplugininputimagesource/texturetarget%28%29.md)
  Returns the texture target.
- [func textureName() -> GLuint](./qcplugininputimagesource/texturename%28%29.md)
  Returns the texture name.
- [func textureColorSpace() -> Unmanaged<CGColorSpace>!](./qcplugininputimagesource/texturecolorspace%28%29.md)
  Returns the color space of the texture representation.
- [func textureFlipped() -> Bool](./qcplugininputimagesource/textureflipped%28%29.md)
  Returns whether or not the contents of the texture are flipped vertically.
- [func textureMatrix() -> UnsafePointer<GLfloat>!](./qcplugininputimagesource/texturematrix%28%29.md)
  Returns a texture matrix.
### Getting Image Buffer Information
- [func imageBounds() -> NSRect](./qcplugininputimagesource/imagebounds%28%29.md)
  Returns the actual bounds of the image source expressed in pixels and aligned to integer boundaries.
- [func bufferPixelsWide() -> Int](./qcplugininputimagesource/bufferpixelswide%28%29.md)
  Returns the width of the image buffer representation.
- [func bufferPixelsHigh() -> Int](./qcplugininputimagesource/bufferpixelshigh%28%29.md)
  Returns the height of the image buffer representation.
- [func bufferPixelFormat() -> String!](./qcplugininputimagesource/bufferpixelformat%28%29.md)
  Returns the pixel format of the image buffer representation.
- [func bufferColorSpace() -> Unmanaged<CGColorSpace>!](./qcplugininputimagesource/buffercolorspace%28%29.md)
  Returns the color space of the image buffer representation.
- [func bufferBaseAddress() -> UnsafeRawPointer!](./qcplugininputimagesource/bufferbaseaddress%28%29.md)
  Returns the base address of the image buffer.
- [func bufferBytesPerRow() -> Int](./qcplugininputimagesource/bufferbytesperrow%28%29.md)
  Returns the  bytes per row of the buffer representation.

## See Also

### Protocols
- [QCCompositionParameterViewDelegate](./qccompositionparameterviewdelegate.md)
  A protocol for composition parameter view’s delegate.
- [QCCompositionPickerViewDelegate](./qccompositionpickerviewdelegate.md)
  The `QCCompositionPickerViewDelegate` informal protocol defines methods that allow  your application to respond to changes in a composition picker view (a [`QCCompositionPickerView`](./qccompositionpickerview.md) object).
- [protocol QCCompositionRenderer](./qccompositionrenderer.md)
  The `QCRenderer` protocol defines the methods used to pass data to the input ports or retrieve data from the output ports of the root patch of a Quartz Composer composition. This protocol is adopted by the [`QCRenderer`](./qcrenderer.md), [`QCView`](./qcview.md), and [`QCCompositionLayer`](./qccompositionlayer.md) classes.
- [protocol QCPlugInContext](./qcplugincontext.md)
  The `QCPlugInContext` protocol defines methods that you use only from within the execution method ([`execute(_:atTime:withArguments:)`](./qcplugin/execute%28_,attime,witharguments%29.md)) of a `QCPlugIn` object.
- [protocol QCPlugInOutputImageProvider](./qcpluginoutputimageprovider.md)
  The `QCPlugInOuputImageProvider` protocol eliminates the need to use explicit image types for the image output ports on a custom patch. The methods in this protocol are called by the Quartz Composer engine when the output image is needed. If your custom patch has an image output port, you need to implement the appropriate methods for rendering image data and to supply information about the rendering destination and the image bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugininputimagesource)*