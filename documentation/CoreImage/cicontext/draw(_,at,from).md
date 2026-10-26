# draw(_:at:from:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Renders a region of an image to a point in the context destination.

**Availability**:
- iOS 5.0+ - Deprecated in 6.0
- iPadOS 5.0+ - Deprecated in 6.0
- Mac Catalyst 5.0+ - Deprecated in 6.0
- tvOS
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Instead use [`draw(_:in:from:)`](./draw%28_,in,from%29.md).

## Declaration

```swift
func draw(_ image: CIImage, at atPoint: CGPoint, from fromRect: CGRect)
```

```objc
- (void) drawImage:(CIImage *) image atPoint:(CGPoint) atPoint fromRect:(CGRect) fromRect;
```

#### Discussion

This method because it is ambiguous as to the units of the dimensions and won’t work as expected in a high-resolution environment which is why you should use `drawImage:inRect:fromRect:` instead.

On iOS platforms, this method draws the image onto a render buffer for the OpenGL ES context. Use this method only if the [`CIContext`](../cicontext.md) object is created with `contextWithEAGLContext:`, and hence, you are rendering to a CAEAGLLayer.

## Parameters

- `image`: A Core Image image object.
- `atPoint`: The point in the context destination to draw to.
- `fromRect`: The region of the image to draw.

## See Also

### Deprecated
- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](./init%28cglcontext,pixelformat,colorspace,options%29-6rp6d.md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
- [init(eaglContext: EAGLContext)](./init%28eaglcontext%29-8ajef.md)
  Creates a Core Image context from an EAGL context.
- [init(eaglContext: EAGLContext, options: [CIContextOption : Any]?)](./init%28eaglcontext,options%29-6uyqj.md)
  Creates a Core Image context from an EAGL context using the specified options.
- [init?(forOfflineGPUAtIndex: UInt32)](./init%28forofflinegpuatindex%29.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.
- [init?(forOfflineGPUAtIndex: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?, sharedContext: CGLContextObj?)](./init%28forofflinegpuatindex,colorspace,options,sharedcontext%29.md)
  Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](./createcglayer%28with,info%29.md)
  Creates a CGLayer object from the provided parameters.
- [+ contextWithCGLContext:pixelFormat:options:](./contextwithcglcontext_pixelformat_options_.md)
  Creates a Core Image context from a CGL context, using the specified options and pixel format object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/draw(_:at:from:))*