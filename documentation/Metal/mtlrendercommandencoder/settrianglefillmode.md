# setTriangleFillMode(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures how subsequent draw commands rasterize triangle and triangle strip primitives.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)
```

#### Discussion

The render pass’s default mode is [`MTLTriangleFillMode.fill`](mtltrianglefillmode/fill.md).

## Parameters

- `fillMode`: A triangle filling mode the render pass applies to draw commands that rasterize triangles or triangle strips.

## See Also

- [func setFrontFacing(MTLWinding)](mtlrendercommandencoder/setfrontfacing(_:).md)
  Configures which face of a primitive, such as a triangle, is the front.
- [func setCullMode(MTLCullMode)](mtlrendercommandencoder/setcullmode(_:).md)
  Configures how the render pipeline determines which primitives to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settrianglefillmode(_:))*