# setFrontFacing(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures which face of a primitive, such as a triangle, is the front.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setFrontFacing(_ frontFacingWinding: MTLWinding)
```

#### Discussion

The render pass’s default front-facing mode is [`MTLWinding.clockwise`](mtlwinding/clockwise.md).

The winding direction of a primitive determines whether the render pass culls it (see [`setCullMode(_:)`](mtlrendercommandencoder/setcullmode(_:).md)).

## Parameters

- `frontFacingWinding`: An   value that configures how the render pipeline defines which side of a primitive is its front.

## See Also

- [func setTriangleFillMode(MTLTriangleFillMode)](mtlrendercommandencoder/settrianglefillmode(_:).md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setCullMode(MTLCullMode)](mtlrendercommandencoder/setcullmode(_:).md)
  Configures how the render pipeline determines which primitives to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfrontfacing(_:))*