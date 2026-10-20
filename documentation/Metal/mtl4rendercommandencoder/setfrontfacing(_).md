# setFrontFacing(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setFrontFacingWinding:(MTLWinding) frontFacingWinding;
```

## Parameters

- `frontFacingWinding`: A [`MTLWinding`](../mtlwinding.md) value that determines which side of a primitive the render pipeline interprets as front facing.

## See Also

### Configuring rendering behavior
- [func setTriangleFillMode(MTLTriangleFillMode)](./settrianglefillmode%28_%29.md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setCullMode(MTLCullMode)](./setcullmode%28_%29.md)
  Controls whether Metal culls front facing primitives, back facing primitives, or culls no primitives at all.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setfrontfacing(_:))*