# createCGLayer(with:info:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Creates a CGLayer object from the provided parameters.

**Availability**:
- macOS 10.4+ - Deprecated in 10.11

## Declaration

```swift
func createCGLayer(with size: CGSize, info: CFDictionary?) -> CGLayer?
```

```objc
- (CGLayerRef) createCGLayerWithSize:(CGSize) size info:(CFDictionaryRef) info;
```

#### Return Value

A CGLayer object.

#### Discussion

After calling this method, Core Image draws content into the CGLayer object. Core Image creates a CGLayer object by calling the Quartz 2D function [`init(_:size:auxiliaryInfo:)`](../../CoreGraphics/cglayer/init%28_,size,auxiliaryinfo%29.md), whose prototype is:

```objc
CGLayerRef CGLayerCreateWithContext (
   CGContextRef context,
   CGSize size,
   CFDictionaryRef auxiliaryInfo
);
```

Core Image passes the [`CIContext`](../cicontext.md) object as the `context` parameter, the size as the `size` parameter, and the dictionary as the `auxiliaryInfo` parameter. For more information on CGLayer objects, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [`CGLayer`](../../CoreGraphics/cglayer.md).

## Parameters

- `size`: The size, in default user space units, of the layer relative to the graphics context.
- `info`: A dictionary, which is passed to `CGLayerCreateWithContext` as the `auxiliaryInfo` parameter. Pass `NULL` because this parameter is reserved for future use.

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
- [func draw(CIImage, at: CGPoint, from: CGRect)](./draw%28_,at,from%29.md)
  Renders a region of an image to a point in the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/createcglayer(with:info:))*