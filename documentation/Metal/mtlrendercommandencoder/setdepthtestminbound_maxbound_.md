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

## Discussion

The render command encoder disables depth bounds testing by default. The render command encoder also disables depth bounds testing when all of the following properties equal a specific value:

- The `minBound` property is equal to `0.0f`.
- The `maxBound` property is equal to `1.0f`. Both `minBound` and `maxBound` need to be within `[0.0f, 1.0f]`, and `minBound` needs to be less than or equal to `maxBound`.

## Parameters

- `minBound`: A minimum bound for depth testing, which discards fragments with a stored depth that is less than `minBound`.
- `maxBound`: A maximum bound for depth testing, which discards fragments with a stored depth that is greater than `maxBound`.

## See Also

### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](./setdepthstencilstate%28_%29.md)
  Configures the combined depth and stencil state.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](./setdepthbias%28_,slopescale,clamp%29.md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](./setdepthclipmode%28_%29.md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setStencilReferenceValue(UInt32)](./setstencilreferencevalue%28_%29.md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](./setstencilreferencevalues%28front,back%29.md)
  Configures different comparison values for front- and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthtestminbound:maxbound:)*