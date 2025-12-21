# setCullMode(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setCullMode(_ cullMode: MTLCullMode)
```

## Parameters

- `cullMode`:   to set.

## See Also

- [func setTriangleFillMode(MTLTriangleFillMode)](mtl4rendercommandencoder/settrianglefillmode(_:).md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setFrontFacing(MTLWinding)](mtl4rendercommandencoder/setfrontfacing(_:).md)
  Configures the vertex winding order that determines which face of a geometric primitive is the front one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcullmode(_:))*