# setStencilReferenceValue(front:back:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the encoder with different stencil test reference values for front-facing and back-facing primitives.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func setStencilReferenceValue(front frontReferenceValue: UInt32, back backReferenceValue: UInt32)
```

#### Discussion

The render pipeline applies `frontReferenceValue` to front-facing primitives and `backReferenceValue` to back-facing primitives.

## Parameters

- `frontReferenceValue`: A stencil test comparison value the render pipeline applies   to front-facing primitives.
- `backReferenceValue`: A stencil test comparison value the render pipeline applies   to back-facing primitives.

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtl4rendercommandencoder/setdepthstencilstate(_:).md)
  Configures this encoder with a depth stencil state that applies to your subsequent draw commands.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtl4rendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment shader functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtl4rendercommandencoder/setdepthclipmode(_:).md)
  Controls the behavior for fragments outside of the near or far planes.
- [func setDepthTestBounds(ClosedRange<Float>)](mtl4rendercommandencoder/setdepthtestbounds(_:).md)
  Configures the range for depth bounds testing.
- [func setStencilReferenceValue(UInt32)](mtl4rendercommandencoder/setstencilreferencevalue(_:).md)
  Configures this encoder with a reference value for stencil testing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4rendercommandencoder/setstencilreferencevalue(front:back:))*