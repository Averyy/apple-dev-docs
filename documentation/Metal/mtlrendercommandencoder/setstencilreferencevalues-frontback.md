# setStencilReferenceValues(front:back:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures different comparison values for front- and back-facing primitives.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setStencilReferenceValues(front frontReferenceValue: UInt32, back backReferenceValue: UInt32)
```

#### Discussion

The command sets separate reference values for front- and back-facing primitives (see [`stencilCompareFunction`](mtlstencildescriptor/stencilcomparefunction.md), [`frontFaceStencil`](mtldepthstencildescriptor/frontfacestencil.md), and [`backFaceStencil`](mtldepthstencildescriptor/backfacestencil.md)). These reference values apply to the stencil state you set with the [`setDepthStencilState(_:)`](mtlrendercommandencoder/setdepthstencilstate(_:).md) method.

The render pass’s default reference value for the front and back stencil compare function is `0`.

## Parameters

- `frontReferenceValue`: A stencil test comparison value the render pipeline applies to only front-facing primitives.
- `backReferenceValue`: A stencil test comparison value the render pipeline applies to only back-facing primitives.

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtlrendercommandencoder/setdepthstencilstate(_:).md)
  Configures the combined depth and stencil state.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtlrendercommandencoder/setdepthclipmode(_:).md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setstencilreferencevalues(front:back:))*