# setDepthTestBounds(_:)

**Framework**: Metal  
**Kind**: method

Configures the range for depth bounds testing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setDepthTestBounds(_ bounds: ClosedRange<Float>)
```

#### Discussion

The render command encoder disables depth bounds testing by default. The render command encoder also disables depth bounds testing when the `bounds` property equals `0.0...1.0`. `bounds.lowerBound` needs to be greater than or equal to `0.0`. `bounds.upperBound` needs to be less than or equal to `1.0`.

## Parameters

- `bounds`: A closed range the renderer applies to depth bounds testing.   The renderer discards fragments with a stored depth that is outside  .

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtl4rendercommandencoder/setdepthstencilstate(_:).md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtl4rendercommandencoder/setdepthclipmode(_:).md)
  Controls the behavior for fragments outside of the near or far planes.
- [func setStencilReferenceValue(UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(_:).md)
  Configures this encoder with a reference value for stencil testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(front:back:).md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthtestbounds(_:))*