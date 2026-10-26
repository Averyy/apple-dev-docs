# contextWithCGLContext:pixelFormat:options:

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a Core Image context from a CGL context, using the specified options and pixel format object.

**Availability**:
- macOS 10.4+ - Deprecated in 10.6

> **Deprecated**: Instead use [`init(cglContext:pixelFormat:colorSpace:options:)`](./init%28cglcontext,pixelformat,colorspace,options%29-6rp6d.md).

## Declaration

```objc
+ (CIContext *) contextWithCGLContext:(CGLContextObj) cglctx pixelFormat:(CGLPixelFormatObj) pixelFormat options:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `cglctx`: A CGL context (`CGLContextObj` object) obtain by calling the CGL function `CGLCreateContext`.
- `pixelFormat`: A CGL pixel format object (`CGLPixelFormatObj` object) created by calling the CGL function `CGLChoosePixelFormat`. This argument must be the same pixel format object used to create the CGL context. The pixel format object must be valid for the lifetime of the Core Image context. Don’t release the pixel format object until after you release the Core Image context.
- `options`: A dictionary that contains color space information. You can provide the keys [`outputColorSpace`](../cicontextoption/outputcolorspace.md) or [`workingColorSpace`](../cicontextoption/workingcolorspace.md) along with a [`CGColorSpace`](../../CoreGraphics/cgcolorspace.md) object for each color space.

## See Also

### Related Documentation
- [init(cgContext: CGContext, options: [CIContextOption : Any]?)](./init%28cgcontext,options%29-6p78w.md)
  Creates a Core Image context from a Quartz context, using the specified options.
### Deprecated
- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](./init%28cglcontext,pixelformat,colorspace,options%29-6rp6d.md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](./init%28eaglcontext%29-8ajef.md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](./init%28eaglcontext,options%29-6uyqj.md)
  Creates a Core Image context from an EAGL context using the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](./createcglayer%28with,info%29.md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](./draw%28_,at,from%29.md)
  Renders a region of an image to a point in the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/contextwithcglcontext:pixelformat:options:)*