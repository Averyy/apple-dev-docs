# setDepthBias(_:slopeScale:clamp:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setDepthBias(_ depthBias: Float, slopeScale: Float, clamp: Float)
```

```objc
- (void) setDepthBias:(float) depthBias slopeScale:(float) slopeScale clamp:(float) clamp;
```

## Discussion

Call this method to have the render pipeline apply a bias to the rasterized depth after the clipping stage. The bias affects both depth testing and the values the render pipeline writes to the depth render target. If you don’t explicitly call this method, the pipeline doesn’t apply a scale or a bias to a depth value.

Set a depth bias to improve the quality of techniques such as shadow mapping and avoid depth artifacts like shadow acne.

> **Note**: A depth bias only influences triangle primitives, but doesn’t apply to points or lines.

## Parameters

- `depthBias`: A constant bias the render pipeline applies to all fragments.
- `slopeScale`: A bias coefficient that scales with the depth of the primitive relative to the camera.
- `clamp`: A value that limits the bias value the render pipeline can apply to a fragment. Pass a positive or negative value to limit the largest magnitude of a positive or negative bias, respectively.

  You can disable the bias clamping functionality by passing `0.0`.

## See Also

### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](./setdepthstencilstate%28_%29.md)
  Configures the combined depth and stencil state.
- [func setDepthClipMode(MTLDepthClipMode)](./setdepthclipmode%28_%29.md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setDepthTestBounds(ClosedRange<Float>)](./setdepthtestbounds%28_%29.md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](./setstencilreferencevalue%28_%29.md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](./setstencilreferencevalues%28front,back%29.md)
  Configures different comparison values for front- and back-facing primitives.
- [- setDepthTestMinBound:maxBound:](./setdepthtestminbound_maxbound_.md)
  Configures the minimum and maximum bounds for depth bounds testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:))*