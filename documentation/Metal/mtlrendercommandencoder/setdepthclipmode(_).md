# setDepthClipMode(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)
```

```objc
- (void) setDepthClipMode:(MTLDepthClipMode) depthClipMode;
```

#### Discussion

You can use depth clipping to ignore fragments outside the z-axis boundaries of a viewing volume.

The render pass’s default clip mode is [`MTLDepthClipMode.clip`](../mtldepthclipmode/clip.md).

## Parameters

- `depthClipMode`: The mode that determines how to handle fragments outside the near and far planes.

## See Also

### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](./setdepthstencilstate%28_%29.md)
  Configures the combined depth and stencil state.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](./setdepthbias%28_,slopescale,clamp%29.md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setDepthTestBounds(ClosedRange<Float>)](./setdepthtestbounds%28_%29.md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](./setstencilreferencevalue%28_%29.md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](./setstencilreferencevalues%28front,back%29.md)
  Configures different comparison values for front- and back-facing primitives.
- [- setDepthTestMinBound:maxBound:](./setdepthtestminbound_maxbound_.md)
  Configures the minimum and maximum bounds for depth bounds testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthclipmode(_:))*