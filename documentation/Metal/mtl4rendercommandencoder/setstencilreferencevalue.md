# setStencilReferenceValue(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures this encoder with a reference value for stencil testing.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setStencilReferenceValue(_ referenceValue: UInt32)
```

#### Discussion

The render pipeline applies this reference value to both front-facing and back-facing primitives.

## Parameters

- `referenceValue`: A stencil test comparison value.

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtl4rendercommandencoder/setdepthstencilstate(_:).md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtl4rendercommandencoder/setdepthclipmode(_:).md)
  Controls the behavior for fragments outside of the near or far planes.
- [func setDepthTestBounds(ClosedRange<Float>)](mtl4rendercommandencoder/setdepthtestbounds(_:).md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(front: UInt32, back: UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(front:back:).md)
  Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(_:))*