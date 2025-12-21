# setFrontFacing(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the vertex winding order that determines which face of a geometric primitive is the front one.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setFrontFacing(_ frontFacingWinding: MTLWinding)
```

## Parameters

- `frontFacingWinding`: A   value that determines which side of a primitive the render pipeline   interprets as front facing.

## See Also

- [func setTriangleFillMode(MTLTriangleFillMode)](mtl4rendercommandencoder/settrianglefillmode(_:).md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setCullMode(MTLCullMode)](mtl4rendercommandencoder/setcullmode(_:).md)
  Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setfrontfacing(_:))*