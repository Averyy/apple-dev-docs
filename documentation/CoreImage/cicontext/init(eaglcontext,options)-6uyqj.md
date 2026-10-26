# init(eaglContext:options:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates a Core Image context from an EAGL context using the specified options.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- tvOS - Deprecated in 12.0

> **Deprecated**: Core Image OpenGLES API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
init(eaglContext: EAGLContext, options: [CIContextOption : Any]? = nil)
```

```objc
+ (CIContext *) contextWithEAGLContext:(EAGLContext *) eaglContext options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

A Core Image context that targets OpenGL ES.

#### Discussion

The OpenGL ES context must support OpenGL ES 2.0. All drawing performed using the methods listed in Drawing Images is rendered directly into the context.

## Parameters

- `eaglContext`: The EAGL context to render to.
- `options`: A dictionary that contains options for creating a [`CIContext`](../cicontext.md) object. You can pass any of the keys defined in [`CIContextOption`](../cicontextoption.md) along with the appropriate value.

## See Also

### Deprecated
- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](./init%28cglcontext,pixelformat,colorspace,options%29-6rp6d.md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](./init%28eaglcontext%29-8ajef.md)
  Creates a Core Image context from an EAGL context.
- [init?(forOfflineGPUAtIndex: UInt32)](./init%28forofflinegpuatindex%29.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](./init%28forofflinegpuatindex,colorspace,options,sharedcontext%29.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](./createcglayer%28with,info%29.md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](./draw%28_,at,from%29.md)
  Renders a region of an image to a point in the context destination.
- [+ contextWithCGLContext:pixelFormat:options:](./contextwithcglcontext_pixelformat_options_.md)
  Creates a Core Image context from a CGL context, using the specified options and pixel format object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(eaglcontext:options:)-6uyqj)*