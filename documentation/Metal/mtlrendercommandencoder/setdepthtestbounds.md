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

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtlrendercommandencoder/setdepthstencilstate(_:).md)
  Configures the combined depth and stencil state.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtlrendercommandencoder/setdepthclipmode(_:).md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](mtlrendercommandencoder/setstencilreferencevalues(front:back:).md)
  Configures different comparison values for front- and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthtestbounds(_:))*