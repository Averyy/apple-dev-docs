# MTLDepthStencilState

**Framework**: Metal  
**Kind**: protocol

A depth and stencil state instance that specifies the depth and stencil configuration and operations used in a render pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLDepthStencilState : NSObjectProtocol, Sendable
```

#### Overview

The [`MTLDepthStencilState`](mtldepthstencilstate.md) protocol defines the interface for a lightweight instance used to encode how a graphics rendering pass should perform depth and stencil operations. The [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) uses an [`MTLDepthStencilState`](mtldepthstencilstate.md) instance to set the depth and stencil state for a rendering pass.

The standard allocation and initialization techniques don’t apply when creating an [`MTLDepthStencilState`](mtldepthstencilstate.md) instance. Instead, you can apply the following steps:

1. Create an [`MTLDepthStencilDescriptor`](mtldepthstencildescriptor.md) instance that defines the operations you want the rendering pass to use.
2. Create an [`MTLDepthStencilState`](mtldepthstencilstate.md) instance by passing the descriptor to an [`MTLDevice`](mtldevice.md) instance’s [`makeDepthStencilState(descriptor:)`](mtldevice/makedepthstencilstate(descriptor:).md) method.

Typically, you create [`MTLDepthStencilState`](mtldepthstencilstate.md) instances when your app is first initialized and then reuse them throughout the lifetime of your app.

## Topics

### Identifying properties
- [var device: any MTLDevice](mtldepthstencilstate/device.md)
  The device from which this state object was created.
- [var label: String?](mtldepthstencilstate/label.md)
  A string that identifies this object.
### Instance Properties
- [var gpuResourceID: MTLResourceID](mtldepthstencilstate/gpuresourceid.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Calculating primitive visibility using depth testing](calculating-primitive-visibility-using-depth-testing.md)
  Determine which pixels are visible in a scene by using a depth texture.
- [class MTLDepthStencilDescriptor](mtldepthstencildescriptor.md)
  An instance that configures new [`MTLDepthStencilState`](mtldepthstencilstate.md) instances.
- [class MTLStencilDescriptor](mtlstencildescriptor.md)
  An object that defines the front-facing or back-facing stencil operations of a depth and stencil state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencilstate)*