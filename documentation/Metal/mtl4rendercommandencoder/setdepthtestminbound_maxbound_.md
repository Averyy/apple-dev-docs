# setDepthTestMinBound:maxBound:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Configures the minimum and maximum bounds for depth bounds testing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) setDepthTestMinBound:(float) minBound maxBound:(float) maxBound;
```

#### Discussion

The render command encoder disables depth bounds testing by default. The render command encoder also disables depth bounds testing when all of the following properties equal a specific value:

- The `minBound` property is equal to `0.0f`.
- The `maxBound` property is equal to `1.0f`. Both `minBound` and `maxBound` need to be within `[0.0f, 1.0f]`, and `minBound` needs to be less than or equal to `maxBound`.

## Parameters

- `minBound`: A minimum bound for depth testing, which discards fragments with a stored depth that is less than `minBound`.
- `maxBound`: A maximum bound for depth testing, which discards fragments with a stored depth that is greater than `maxBound`.

## See Also

### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](./setdepthstencilstate%28_%29.md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](./setdepthbias%28_,slopescale,clamp%29.md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](./setdepthclipmode%28_%29.md)
  Controls the behavior for fragments outside of the near or far planes.
- [func setStencilReferenceValue(UInt32)](./setstencilreferencevalue%28_%29.md)
  Configures this encoder with a reference value for stencil testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](./setstencilreferencevalue%28front,back%29.md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthtestminbound:maxbound:)*