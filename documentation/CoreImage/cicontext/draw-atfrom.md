# draw(_:at:from:)

**Framework**: Core Image  
**Kind**: method

Renders a region of an image to a point in the context destination.

**Availability**:
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func draw(_ image: CIImage, at atPoint: CGPoint, from fromRect: CGRect)
```

#### Discussion

This method because it is ambiguous as to the units of the dimensions and won’t work as expected in a high-resolution environment which is why you should use `drawImage:inRect:fromRect:` instead.

On iOS platforms, this method draws the image onto a render buffer for the OpenGL ES context. Use this method only if the [`CIContext`](cicontext.md) object is created with `contextWithEAGLContext:`, and hence, you are rendering to a CAEAGLLayer.

## Parameters

- `image`: A Core Image image object.
- `atPoint`: The point in the context destination to draw to.
- `fromRect`: The region of the image to draw.

## See Also

- [init(cglContext: CGLContextObj, pixelFormat: CGLPixelFormatObj?, colorSpace: CGColorSpace?, options: [CIContextOption : Any]?)](cicontext/init(cglcontext:pixelformat:colorspace:options:).md)
  Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/draw(_:at:from:))*