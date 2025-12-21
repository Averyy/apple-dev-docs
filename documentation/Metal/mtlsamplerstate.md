# MTLSamplerState

**Framework**: Metal  
**Kind**: protocol

An instance that defines how a texture should be sampled.

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

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Adding mipmap filtering to samplers](adding-mipmap-filtering-to-samplers.md)

#### Overview

The [`MTLSamplerState`](mtlsamplerstate.md) protocol defines the interface for a lightweight instance used to encode how a shader or compute kernel should sample a texture. To create a sampler state instance:

1. Create an [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) instance.
2. Set the desired properties of the sampler descriptor, including filtering options, addressing modes, maximum anisotropy, and level-of-detail parameters.
3. Call the [`makeSamplerState(descriptor:)`](mtldevice/makesamplerstate(descriptor:).md) method of the [`MTLDevice`](mtldevice.md) instance.

(Your app does not define a class that implements the [`MTLSamplerState`](mtlsamplerstate.md) protocol.)

You can either release the [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) instance or modify its property values and reuse it to create more [`MTLSamplerState`](mtlsamplerstate.md) instances. The descriptor’s properties are only used during instance creation; once created the behavior of a sampler state instance is fixed and cannot be changed.

## Topics

### Identifying the sampler
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

- [Creating and sampling textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.
- [class MTLSamplerDescriptor](mtlsamplerdescriptor.md)
  An object that you use to configure a texture sampler.
- [struct MTLSamplePosition](mtlsampleposition.md)
  A subpixel sample position for use in multisample antialiasing (MSAA).
- [enum MTLSamplerReductionMode](mtlsamplerreductionmode.md)
  Configures how the sampler aggregates contributing samples to a final value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerstate)*