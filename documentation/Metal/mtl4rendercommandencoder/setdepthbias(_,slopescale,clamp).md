# setDepthBias(_:slopeScale:clamp:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setDepthBias(_ depthBias: Float, slopeScale: Float, clamp: Float)
```

```objc
- (void) setDepthBias:(float) depthBias slopeScale:(float) slopeScale clamp:(float) clamp;
```

## Parameters

- `depthBias`: A constant bias the render pipeline applies to all fragments.
- `slopeScale`: A bias coefficient that scales with the depth of the primitive relative to the camera.
- `clamp`: A value that limits the bias value the render pipeline can apply to a fragment. Pass a positive or negative value to limit the largest magnitude of a positive or negative bias, respectively. Set this value to `0` to disable bias clamping.

## See Also

### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](./setdepthstencilstate%28_%29.md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthClipMode(MTLDepthClipMode)](./setdepthclipmode%28_%29.md)
  Controls the behavior for fragments outside of the near or far planes.
- [func setDepthTestBounds(ClosedRange<Float>)](./setdepthtestbounds%28_%29.md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](./setstencilreferencevalue%28_%29.md)
  Configures this encoder with a reference value for stencil testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](./setstencilreferencevalue%28front,back%29.md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:))*