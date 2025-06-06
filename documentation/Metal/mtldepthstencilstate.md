# MTLDepthStencilState

**Framework**: Metal  
**Kind**: protocol

A depth and stencil state object that specifies the depth and stencil configuration and operations used in a render pass.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLDepthStencilState : NSObjectProtocol
```

#### Overview

The [`MTLDepthStencilState`](mtldepthstencilstate.md) protocol defines the interface for a lightweight object used to encode how a graphics rendering pass should perform depth and stencil operations. The [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) uses a [`MTLDepthStencilState`](mtldepthstencilstate.md) object to set the depth and stencil state for a rendering pass.

Do not use standard allocation and initialization techniques to create a [`MTLDepthStencilState`](mtldepthstencilstate.md) object. To create a [`MTLDepthStencilState`](mtldepthstencilstate.md) object:

1. Create a [`MTLDepthStencilDescriptor`](mtldepthstencildescriptor.md) object that defines the operations you want the rendering pass to use.
2. Then call the [`makeDepthStencilState(descriptor:)`](mtldevice/makedepthstencilstate(descriptor:).md) method of [`MTLDevice`](mtldevice.md) to create a [`MTLDepthStencilState`](mtldepthstencilstate.md) object.

Typically, you create [`MTLDepthStencilState`](mtldepthstencilstate.md) objects when your app is first initialized and then reuse them throughout the lifetime of your app.

## Topics

### Identifying Properties
- [var device: any MTLDevice](mtldepthstencilstate/device.md)
  The device from which this state object was created.
- [var label: String?](mtldepthstencilstate/label.md)
  A string that identifies this object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Calculating Primitive Visibility Using Depth Testing](calculating-primitive-visibility-using-depth-testing.md)
  Determine which pixels are visible in a scene by using a depth texture.
- [class MTLDepthStencilDescriptor](mtldepthstencildescriptor.md)
  An object that configures new [`MTLDepthStencilState`](mtldepthstencilstate.md) objects.
- [class MTLStencilDescriptor](mtlstencildescriptor.md)
  An object that defines the front-facing or back-facing stencil operations of a depth and stencil state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencilstate)*