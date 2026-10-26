# setStencilReferenceValue(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Configures the same comparison value for front- and back-facing primitives.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setStencilReferenceValue(_ referenceValue: UInt32)
```

```objc
- (void) setStencilReferenceValue:(uint32_t) referenceValue;
```

#### Discussion

The command sets the same reference value for front- and back-facing primitives (see [`stencilCompareFunction`](../mtlstencildescriptor/stencilcomparefunction.md), [`frontFaceStencil`](../mtldepthstencildescriptor/frontfacestencil.md), and [`backFaceStencil`](../mtldepthstencildescriptor/backfacestencil.md)). This reference value applies to the stencil state you set with the [`setDepthStencilState(_:)`](./setdepthstencilstate%28_%29.md) method.

The render pass’s default reference value for the front and back stencil compare function is `0`.

## Parameters

- `referenceValue`: A stencil test comparison value the render pipeline applies to both front- and back-facing primitives.

## See Also

### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](./setdepthstencilstate%28_%29.md)
  Configures the combined depth and stencil state.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](./setdepthbias%28_,slopescale,clamp%29.md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](./setdepthclipmode%28_%29.md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setDepthTestBounds(ClosedRange<Float>)](./setdepthtestbounds%28_%29.md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](./setstencilreferencevalues%28front,back%29.md)
  Configures different comparison values for front- and back-facing primitives.
- [- setDepthTestMinBound:maxBound:](./setdepthtestminbound_maxbound_.md)
  Configures the minimum and maximum bounds for depth bounds testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setstencilreferencevalue(_:))*