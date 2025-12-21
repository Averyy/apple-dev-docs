# setDepthBias(_:slopeScale:clamp:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setDepthBias(_ depthBias: Float, slopeScale: Float, clamp: Float)
```

#### Discussion

Call this method to have the render pipeline apply a bias to the rasterized depth after the clipping stage. The bias affects both depth testing and the values the render pipeline writes to the depth render target. If you don’t explicitly call this method, the pipeline doesn’t apply a scale or a bias to a depth value.

Set a depth bias to improve the quality of techniques such as shadow mapping and avoid depth artifacts like shadow acne.

> **Note**: A depth bias only influences triangle primitives, but doesn’t apply to points or lines.

## Parameters

- `depthBias`: A constant bias the render pipeline applies to all fragments.
- `slopeScale`: A bias coefficient that scales with the depth of the primitive relative to the camera.
- `clamp`: You can disable the bias clamping functionality by passing  .

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtlrendercommandencoder/setdepthstencilstate(_:).md)
  Configures the combined depth and stencil state.
- [func setDepthClipMode(MTLDepthClipMode)](mtlrendercommandencoder/setdepthclipmode(_:).md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setDepthTestBounds(ClosedRange<Float>)](mtlrendercommandencoder/setdepthtestbounds(_:).md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](mtlrendercommandencoder/setstencilreferencevalues(front:back:).md)
  Configures different comparison values for front- and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:))*