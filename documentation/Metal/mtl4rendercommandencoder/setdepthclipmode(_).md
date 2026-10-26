# setDepthClipMode(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Controls the behavior for fragments outside of the near or far planes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setDepthClipMode(_ depthClipMode: MTLDepthClipMode)
```

```objc
- (void) setDepthClipMode:(MTLDepthClipMode) depthClipMode;
```

## Parameters

- `depthClipMode`: [`MTLDepthClipMode`](../mtldepthclipmode.md) to set.

## See Also

### Configuring depth and stencil behavior
- [func setDepthStencilState((any MTLDepthStencilState)?)](./setdepthstencilstate%28_%29.md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](./setdepthbias%28_,slopescale,clamp%29.md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthTestBounds(ClosedRange<Float>)](./setdepthtestbounds%28_%29.md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](./setstencilreferencevalue%28_%29.md)
  Configures this encoder with a reference value for stencil testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](./setstencilreferencevalue%28front,back%29.md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.
- [- setDepthTestMinBound:maxBound:](./setdepthtestminbound_maxbound_.md)
  Configures the minimum and maximum bounds for depth bounds testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthclipmode(_:))*