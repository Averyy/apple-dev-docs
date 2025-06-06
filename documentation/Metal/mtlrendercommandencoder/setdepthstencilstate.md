# setDepthStencilState(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Configures the combined depth and stencil state.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setDepthStencilState(_ depthStencilState: (any MTLDepthStencilState)?)
```

#### Discussion

This method changes the combined depth and stencil state for the render command encoder that’s compatible with its depth and stencil attachment configuration. For example, if the new state enables depth testing or depth writing, the render pass needs to have a depth attachment. Similarly, if the new state enables stencil testing or stencil writing, the render pass’s stencil needs to have a stencil attachment. You create depth and stencil attachments for a render pass by assigning the [`depthAttachment`](mtlrenderpassdescriptor/depthattachment.md) and [`stencilAttachment`](mtlrenderpassdescriptor/stencilattachment.md) properties of the [`MTLRenderPassDescriptor`](mtlrenderpassdescriptor.md) instance that creates it.

Pass `nil` to clear the state from the previous call, which restores a state that’s equivalent to the default values of an [`MTLDepthStencilDescriptor`](mtldepthstencildescriptor.md) instance’s properties.

## Parameters

- `depthStencilState`: An instance that conforms to the   protocol.

## See Also

- [func setDepthBias(Float, slopeScale: Float, clamp: Float)](mtlrendercommandencoder/setdepthbias(_:slopescale:clamp:).md)
  Configures the adjustments a render pass applies to depth values from fragment functions by a scaling factor and bias.
- [func setDepthClipMode(MTLDepthClipMode)](mtlrendercommandencoder/setdepthclipmode(_:).md)
  Configures how the render pipeline handles fragments outside the near and far planes of the view frustum.
- [func setStencilReferenceValue(UInt32)](mtlrendercommandencoder/setstencilreferencevalue(_:).md)
  Configures the same comparison value for front- and back-facing primitives.
- [func setStencilReferenceValues(front: UInt32, back: UInt32)](mtlrendercommandencoder/setstencilreferencevalues(front:back:).md)
  Configures different comparison values for front- and back-facing primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setdepthstencilstate(_:))*