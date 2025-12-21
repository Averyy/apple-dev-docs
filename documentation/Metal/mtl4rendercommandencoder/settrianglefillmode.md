# setTriangleFillMode(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures how subsequent draw commands rasterize triangle and triangle strip primitives.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)
```

## Parameters

- `fillMode`:   the render pass applies to draw commands that   rasterize triangles or triangle strips.

## See Also

- [func setFrontFacing(MTLWinding)](mtl4rendercommandencoder/setfrontfacing(_:).md)
  Configures the vertex winding order that determines which face of a geometric primitive is the front one.
- [func setCullMode(MTLCullMode)](mtl4rendercommandencoder/setcullmode(_:).md)
  Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/settrianglefillmode(_:))*