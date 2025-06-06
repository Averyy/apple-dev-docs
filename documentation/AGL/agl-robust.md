# AGL_ROBUST

**Framework**: AGL  
**Kind**: var

This constant is a Boolean attribute. If it is present in the attributes array,  specifies that AGL should consider only those renderers that do not have any failure modes associated with a lack of video card resources. You can pass this constant to the function [`AGL`](agl-collection.md).

**Availability**:
- macOS 10.0+

## Declaration

```swift
var AGL_ROBUST: Int32 { get }
```

## See Also

- [var AGL_RENDERER_ID: Int32](agl_renderer_id.md)
  The associated value is a nonnegative integer that specifies a renderer. If present, OpenGL renderers that match the specified ID are preferred. See [`Renderer IDs`](renderer-ids.md) for possible values. You can pass this constant to the function [`AGL`](agl-collection.md).
- [var AGL_SINGLE_RENDERER: Int32](agl_single_renderer.md)
- [var AGL_NO_RECOVERY: Int32](agl_no_recovery.md)
- [var AGL_ACCELERATED: Int32](agl_accelerated.md)
  This constant is a Boolean attribute. If it is present in the attributes array,  specifies renderers that are attached to a hardware accelerated graphics device. It is usually impossible to support more than one accelerated graphics device, because typically when a window spans more than one device, OpenGL uses the software renderer. You can pass this constant to the function [`AGL`](agl-collection.md) to find out whether a particular renderer is hardware accelerated.
- [var AGL_CLOSEST_POLICY: Int32](agl_closest_policy.md)
- [var AGL_BACKING_STORE: Int32](agl_backing_store.md)
- [var AGL_MP_SAFE: Int32](agl_mp_safe.md)
- [var AGL_WINDOW: Int32](agl_window.md)
  This constant is a Boolean attribute. If it is present in the attributes array, specifies that the pixel format can be used to render to an onscreen window. You can pass this constant to the function [`AGL`](agl-collection.md).
- [var AGL_MULTISCREEN: Int32](agl_multiscreen.md)
  This constant is a Boolean attribute. If it is present in the attributes array, specifies that the renderer is capable of driving multiple screens with the same rendering context. (A single window can span multiple screens.) You can pass this constant to the function [`AGL`](agl-collection.md).
- [var AGL_VIRTUAL_SCREEN: Int32](agl_virtual_screen.md)
  The associated value is an integer that specifies the virtual screen number of the pixel format.
- [var AGL_COMPLIANT: Int32](agl_compliant.md)
  This constant is a Boolean attribute. If it is present in the attributes array, specifies a pixel format that is fully compliant with OpenGL. All macOS renderers are OpenGL-compliant. You can pass this constant to the function [`AGL`](agl-collection.md).
- [var AGL_PBUFFER: Int32](agl_pbuffer.md)
  This constant is a Boolean attribute. If it is present in the attributes array, specifies that the renderer can render to a pixel buffer. You can pass this constant to the function [`AGL`](agl-collection.md).
- [var AGL_REMOTE_PBUFFER: Int32](agl_remote_pbuffer.md)
  This constant is a Boolean attribute. If it is present in the attributes array, specifies that the renderer can render offline to a pixel buffer.
- [var AGL_RENDERER_ID: Int32](agl_renderer_id.md)
  The associated value is a nonnegative integer that specifies a renderer. If present, OpenGL renderers that match the specified ID are preferred. See [`Renderer IDs`](renderer-ids.md) for possible values. You can pass this constant to the function [`AGL`](agl-collection.md).
- [var AGL_SINGLE_RENDERER: Int32](agl_single_renderer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/agl_robust)*