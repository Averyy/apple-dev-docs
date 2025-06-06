# setDepthClipMode(_:)

**Framework**: Metal  
**Kind**: method  
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

#### Discussion

You can use depth clipping to ignore fragments outside the z-axis boundaries of a viewing volume.

The render pass’s default clip mode is [`MTLDepthClipMode.clip`](mtldepthclipmode/clip.md).

## Parameters

- `depthClipMode`: The mode that determines how to handle fragments outside the near and far planes.

## See Also

- [func setDepthStencilState((any MTLDepthStencilState)?)](mtlrendercommandencoder/setdepthstencilstate(_:).md)
  Configures the combined depth and stencil state.
- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](mtlrendercommandencoder/setstencilreferencevalues(front:back:).md)
  Configures different comparison values for front- and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthclipmode(_:))*