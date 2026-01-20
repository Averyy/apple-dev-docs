# init(cglContext:pixelFormat:colorSpace:options:)

**Framework**: Core Image  
**Kind**: init

Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.

**Availability**:
- macOS 10.6+

## Declaration

```swift
init(cglContext cglctx: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]? = nil)
```

#### Discussion

After calling this method, Core Image draws content into the surface (drawable object) attached to the CGL context. A CGL context is a macOS OpenGL context. For more information, see [`OpenGL Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/opengl_intro.html#//apple_ref/doc/uid/TP40001987).

When you create a [`CIContext`](cicontext.md) object using a CGL context, all OpenGL states set for the CGL context affect rendering to that context. That means that coordinate and viewport transformations set on the CGL context, as well as the vertex color, affect drawing to that context.

For best results, follow these guidelines when you use Core Image to render into an OpenGL context:

- Ensure that a single unit in the coordinate space of the OpenGL context represents a single pixel in the output device.
- The Core Image coordinate space has the origin in the bottom-left corner of the screen. You should configure the OpenGL context in the same way.
- The OpenGL context blending state is respected by Core Image. If the image you want to render contains translucent pixels, it’s best to enable blending using a blend function with the parameters `GL_ONE, GL_ONE_MINUS_SRC_ALPHA`, as shown in the following code example.

Core Image manages its own internal OpenGL context that shares resources with the OpenGL context you specify. To enable resource sharing, use the following code:

## Parameters

- `cglctx`: A CGL context obtained by calling the CGL function  .
- `pixelFormat`: A CGL pixel format object either obtained from the system or created by calling a CGL function such as  . This parameter must be the same pixel format object used to create the CGL context. The pixel format object must be valid for the lifetime of the Core Image context. Don’t release the pixel format object until after you release the Core Image context.
- `colorSpace`: A color space object encapsulating color space information that is used to specify how color values are interpreted.
- `options`: A dictionary that contains options for creating a   object. You can pass any of the keys defined in   along with the appropriate value.

## See Also

- [init(cgContext: CGContext, options: [CIContextOption : Any]?)](cicontext/init(cgcontext:options:).md)
  Creates a Core Image context from a Quartz context, using the specified options.
- [init(eaglContext: EAGLContext)](cicontext/init(eaglcontext:).md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](cicontext/init(eaglcontext:options:).md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAtIndex: UInt32)](cicontext/init(forofflinegpuatindex:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:).md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](cicontext/createcglayer(with:info:).md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](cicontext/draw(_:at:from:).md)
  Renders a region of an image to a point in the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(cglcontext:pixelformat:colorspace:options:))*