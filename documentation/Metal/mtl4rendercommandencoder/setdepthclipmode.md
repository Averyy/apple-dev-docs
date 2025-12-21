# setDepthClipMode(_:)

**Framework**: Metal  
**Kind**: method  
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

## Parameters

- `depthClipMode`:   to set.

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtl4rendercommandencoder/setdepthstencilstate(_:).md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthTestBounds(ClosedRange<Float>)](mtl4rendercommandencoder/setdepthtestbounds(_:).md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(_:).md)
  Configures this encoder with a reference value for stencil testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(front:back:).md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setdepthclipmode(_:))*