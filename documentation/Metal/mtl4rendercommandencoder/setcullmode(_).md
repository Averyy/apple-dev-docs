# setCullMode(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) setCullMode:(MTLCullMode) cullMode;
```

## Parameters

- `cullMode`: [`MTLCullMode`](../mtlcullmode.md) to set.

## See Also

### Configuring rendering behavior
- [func setTriangleFillMode(MTLTriangleFillMode)](./settrianglefillmode%28_%29.md)
  Configures how subsequent draw commands rasterize triangle and triangle strip primitives.
- [func setFrontFacing(MTLWinding)](./setfrontfacing%28_%29.md)
  Configures the vertex winding order that determines which face of a geometric primitive is the front one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setcullmode(_:))*