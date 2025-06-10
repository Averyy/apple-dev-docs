# MTLSamplerState

**Framework**: Metal  
**Kind**: protocol

An object that defines how a texture should be sampled.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLSamplerState : NSObjectProtocol, Sendable
```

## Mentions

- [Improving CPU Performance by Using Argument Buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Adding Mipmap Filtering to Samplers](adding-mipmap-filtering-to-samplers.md)

#### Overview

The [`MTLSamplerState`](mtlsamplerstate.md) protocol defines the interface for a lightweight object used to encode how a shader or compute kernel should sample a texture. To create a sampler state object:

1. Create a [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) object.
2. Set the desired properties of the sampler descriptor, including filtering options, addressing modes, maximum anisotropy, and level-of-detail parameters.
3. Call the [`makeSamplerState(descriptor:)`](mtldevice/makesamplerstate(descriptor:).md) method of the [`MTLDevice`](mtldevice.md) object.

(Your app does not define a class that implements the [`MTLSamplerState`](mtlsamplerstate.md) protocol.)

You can either release the [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) object or modify its property values and reuse it to create more [`MTLSamplerState`](mtlsamplerstate.md) objects. The descriptor’s properties are only used during object creation; once created the behavior of a sampler state object is fixed and cannot be changed.

## Topics

### Identifying the Sampler
- [var device: any MTLDevice](mtlsamplerstate/device.md)
  The device object that created the sampler.
- [var label: String?](mtlsamplerstate/label.md)
  A string that identifies the sampler.
### Instance Properties
- [var gpuResourceID: MTLResourceID](mtlsamplerstate/gpuresourceid.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating and Sampling Textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.
- [class MTLSamplerDescriptor](mtlsamplerdescriptor.md)
  An object that you use to configure a texture sampler.
- [struct MTLSamplePosition](mtlsampleposition.md)
  A subpixel sample position for use in multisample antialiasing (MSAA).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerstate)*