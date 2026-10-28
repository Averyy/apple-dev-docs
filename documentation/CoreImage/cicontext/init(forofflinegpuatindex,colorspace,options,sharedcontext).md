# init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)

**Framework**: Core Image  
**Kind**: init  
**Role**: Initializer

Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.

**Availability**:
- macOS 10.10+ - Deprecated in 10.14

> **Deprecated**: Core Image OpenGL API deprecated. (Define CI_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
init?(forOfflineGPUAtIndex index: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]? = nil, sharedContext: CGLContextObj?)
```

## Return Value

A Core Image context.

## Discussion

GPU devices that are not currently being used to drive a display can be used for Core Image rendering. Use the [`offlineGPUCount()`](./offlinegpucount%28%29.md) method to determine whether any such GPUs are available.

To create a Metal-based Core Image context using an offline GPU, use the [`MTLCopyAllDevices()`](../../Metal/mtlcopyalldevices%28%29.md) function to list Metal devices, then choose a device without a display to pass to the [`init(mtlDevice:)`](./init%28mtldevice%29-swey.md) method.

## Parameters

- `index`: The index of the offline GPU with which to create the context; a number between zero and the value returned by the [`offlineGPUCount()`](./offlinegpucount%28%29.md) method.
- `colorSpace`: A color space object encapsulating color space information that is used to specify how color values are interpreted.
- `options`: A dictionary that contains options for creating a [`CIContext`](../cicontext.md) object. You can pass any of the keys defined in [`CIContextOption`](../cicontextoption.md) along with the appropriate value.
- `sharedContext`: A CGL context with which to share OpenGL resources, obtained by calling the CGL function `CGLCreateContext(_:_:_:)`. Pass `NULL` to use a context that does not share OpenGL resources.

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
- [func createCGLayer(with: CGSize, info: CFDictionary?) -> CGLayer?](./createcglayer%28with,info%29.md)
  Creates a CGLayer object from the provided parameters.
- [func draw(CIImage, at: CGPoint, from: CGRect)](./draw%28_,at,from%29.md)
  Renders a region of an image to a point in the context destination.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:))*