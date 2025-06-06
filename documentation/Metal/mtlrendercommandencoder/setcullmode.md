# setCullMode(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures how the render pipeline determines which primitives to remove.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setCullMode(_ cullMode: MTLCullMode)
```

#### Discussion

This method configures which primitives the render pipeline removes, if any, based on the direction of each primitive’s face relative to the scene’s camera. For example, you can correctly cull hidden surfaces on some geometric models, such as a sphere made of filled triangles, if it uses orientable surfaces. A surface is  if its primitives consistently use the same ordering for its vertices. Metal defines vertex ordering with the [`MTLWinding`](mtlwinding.md) type, which includes [`MTLWinding.clockwise`](mtlwinding/clockwise.md) and [`MTLWinding.counterClockwise`](mtlwinding/counterclockwise.md). You can tell the render pipeline which direction your primitives face by calling the [`setFrontFacing(_:)`](mtlrendercommandencoder/setfrontfacing(_:).md) method, which affects the primitives the culling mode removes.

The render pass’s default culling mode is [`MTLCullMode.none`](mtlcullmode/none.md).

## Parameters

- `cullMode`: An   value that configures how the render pipeline determines which primitives to remove from the pipeline.

## See Also

- [func setTriangleFillMode(MTLTriangleFillMode)](mtlrendercommandencoder/settrianglefillmode(_:).md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setFrontFacing(MTLWinding)](mtlrendercommandencoder/setfrontfacing(_:).md)
  Configures which face of a primitive, such as a triangle, is the front.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setcullmode(_:))*