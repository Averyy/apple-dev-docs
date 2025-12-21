# Mixing Metal and OpenGL rendering in a view

**Framework**: Metal

Draw with Metal and OpenGL in the same view using an interoperable texture.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 10.13+
- Xcode 11.0+

#### Overview

If you’re developing a new app and migrating legacy OpenGL code to Metal, interoperable textures make it easy for you to see the results live as you go.

You can render Metal or OpenGL content into either view by initializing a [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) that operates as an interoperable texture. When you enable the pixel buffer’s Metal and OpenGL compatibility flags, the textures are capable of being drawn to—and presented by—either rendering technology.

If you’re working with an app you’ve already deployed, the interoperable textures give you the option of incrementally releasing updates throughout the porting process.

##### Getting Started

Interoperating with Metal and OpenGL requires macOS 10.13 or greater or iOS 11 or greater.

##### Select a Compatible Pixel Format

To create an interoperable texture, select a Core Video  pixel format, a Metal pixel format, and an OpenGL internal format that are compatible with each other. This sample provides you with a table preloaded with compatible options, and selects one based on the desired Metal pixel format:

```objective-c
for(int i = 0; i < AAPLNumInteropFormats; i++) {
    if(pixelFormat == AAPLInteropFormatTable[i].mtlFormat) {
        return &AAPLInteropFormatTable[i];
    }
}
```

##### Create an Interoperable Texture

Use a `CVPixelBuffer` as an interoperable texture to get a shared memory backing that’s synchronized across both renderers. To create the `CVPixelBuffer`, provide your Core Video  pixel format and enable OpenGL and Metal compatibility:

```objective-c
NSDictionary* cvBufferProperties = @{
    (__bridge NSString*)kCVPixelBufferOpenGLCompatibilityKey : @YES,
    (__bridge NSString*)kCVPixelBufferMetalCompatibilityKey : @YES,
};
CVReturn cvret = CVPixelBufferCreate(kCFAllocatorDefault,
                        size.width, size.height,
                        _formatInfo->cvPixelFormat,
                        (__bridge CFDictionaryRef)cvBufferProperties,
                        &_CVPixelBuffer);
```

##### Create an Opengl Texture From the Pixel Buffer in Macos

Start by creating an OpenGL Core Video texture cache from the pixel buffer:

```objective-c
cvret  = CVOpenGLTextureCacheCreate(
                kCFAllocatorDefault,
                nil,
                _openGLContext.CGLContextObj,
                _CGLPixelFormat,
                nil,
                &_CVGLTextureCache);
```

Then, create a `CVPixelBuffer`-backed OpenGL texture image from the texture cache:

```objective-c
cvret = CVOpenGLTextureCacheCreateTextureFromImage(
                kCFAllocatorDefault,
                _CVGLTextureCache,
                _CVPixelBuffer,
                nil,
                &_CVGLTexture);
```

Finally, get an OpenGL texture name from the `CVPixelBuffer`-backed OpenGL texture image:

```objective-c
_openGLTexture = CVOpenGLTextureGetName(_CVGLTexture);
```

##### Create an Opengl Es Texture From the Pixel Buffer in Ios

Start by creating an OpenGL `ES` Core Video  texture cache from the pixel buffer:

```objective-c
cvret = CVOpenGLESTextureCacheCreate(kCFAllocatorDefault,
                nil,
                _openGLContext,
                nil,
                &_CVGLTextureCache);
```

Then, create a `CVPixelBuffer`-backed OpenGL `ES` texture image from the texture cache:

```objective-c
cvret = CVOpenGLESTextureCacheCreateTextureFromImage(kCFAllocatorDefault,
                _CVGLTextureCache,
                _CVPixelBuffer,
                nil,
                GL_TEXTURE_2D,
                _formatInfo->glInternalFormat,
                _size.width, _size.height,
                _formatInfo->glFormat,
                _formatInfo->glType,
                0,
                &_CVGLTexture);
```

Finally, get an OpenGL `ES` texture name from the `CVPixelBuffer`-backed OpenGL `ES` texture image:

```objective-c
_openGLTexture = CVOpenGLESTextureGetName(_CVGLTexture);
```

##### Create a Metal Texture From the Pixel Buffer

Start by instantiating a Metal texture cache as follows:

```objective-c
cvret = CVMetalTextureCacheCreate(
                kCFAllocatorDefault,
                nil,
                _metalDevice,
                nil,
                &_CVMTLTextureCache);
```

Then, create a `CVPixelBuffer`-backed Metal texture image from the texture cache:

```objective-c
cvret = CVMetalTextureCacheCreateTextureFromImage(
                kCFAllocatorDefault,
                _CVMTLTextureCache,
                _CVPixelBuffer, nil,
                _formatInfo->mtlFormat,
                _size.width, _size.height,
                0,
                &_CVMTLTexture);
```

Finally, get a Metal texture using the Core Video  Metal texture reference:

```objective-c
_metalTexture = CVMetalTextureGetTexture(_CVMTLTexture);
```

##### Draw Metal Content in an Opengl View

When porting your app, statement by statement, begin by using Metal to render into an interoperable pixel buffer that OpenGL can draw. Each item in the following list describes the corresponding numbered area in the figure that follows:

1. Metal clears the interoperable texture by applying a green color.
2. Metal renders a quad with white text and color swatch onto the interoperable texture.
3. OpenGL clears the background by applying a red color.
4. OpenGL renders a quad with black text and the interoperable texture.

![Screenshot of the app showing, in the background, a red color cleared by OpenGL, a green quad cleared by Metal with a black text overlay rendered by OpenGL, and a color swatch with white text rendered by Metal.](https://docs-assets.developer.apple.com/published/f1dd9258fc759141f2f1ba10fa8de19b/opengl-interoperability-1-gl-view.png)

##### Draw Opengl Content in a Metal View

Draw OpenGL content into a Metal view when you’re ready to use Metal but have some legacy OpenGL code that you intend to port incrementally. Each item in the following list describes the corresponding numbered area in the figure that follows:

1. OpenGL clears the interoperable texture by applying a red color.
2. OpenGL renders a quad with white text and color swatch onto the interoperable texture.
3. Metal clears the background by applying a green color.
4. Metal renders a quad with black text and the interoperable texture.

![Screenshot of the app showing, in the background, a green color cleared by Metal, a red quad cleared by OpenGL with a black text overlay rendered by Metal, and a color swatch with white text rendered by OpenGL.](https://docs-assets.developer.apple.com/published/1f7d3a50ed7b0e2020ab046a4f8e3142/opengl-interoperability-2-metal-view.png)

## See Also

- [Migrating OpenGL code to Metal](migrating-opengl-code-to-metal.md)
  Replace your app’s deprecated OpenGL code with Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mixing-metal-and-opengl-rendering-in-a-view)*