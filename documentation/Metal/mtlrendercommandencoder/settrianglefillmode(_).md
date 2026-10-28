# setTriangleFillMode(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Configures how subsequent draw commands rasterize triangle and triangle strip primitives.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTriangleFillMode(_ fillMode: MTLTriangleFillMode)
```

```objc
- (void) setTriangleFillMode:(MTLTriangleFillMode) fillMode;
```

## Discussion

The render pass’s default mode is [`MTLTriangleFillMode.fill`](../mtltrianglefillmode/fill.md).

## Parameters

- `fillMode`: A triangle filling mode the render pass applies to draw commands that rasterize triangles or triangle strips.

## See Also

### Configuring rendering behavior
- [func setFrontFacing(MTLWinding)](./setfrontfacing%28_%29.md)
  Configures which face of a primitive, such as a triangle, is the front.
- [func setCullMode(MTLCullMode)](./setcullmode%28_%29.md)
  Configures how the render pipeline determines which primitives to remove.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/settrianglefillmode(_:))*