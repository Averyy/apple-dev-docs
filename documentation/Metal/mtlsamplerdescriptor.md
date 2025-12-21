# MTLSamplerDescriptor

**Framework**: Metal  
**Kind**: class

An object that you use to configure a texture sampler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLSamplerDescriptor
```

## Mentions

- [Adding mipmap filtering to samplers](adding-mipmap-filtering-to-samplers.md)
- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Restricting access to specific mipmaps](restricting-access-to-specific-mipmaps.md)

#### Overview

To make a sampler, create and configure an [`MTLSamplerDescriptor`](mtlsamplerdescriptor.md) instance and then call an [`MTLDevice`](mtldevice.md) instance’s [`makeSamplerState(descriptor:)`](mtldevice/makesamplerstate(descriptor:).md) method. After you create the sampler, you can release the descriptor or reconfigure its properties to create other samplers.

## Topics

### Declaring the coordinate space
- [var normalizedCoordinates: Bool](mtlsamplerdescriptor/normalizedcoordinates.md)
  A Boolean value that indicates whether texture coordinates are normalized to the range `[0.0, 1.0]`.
### Declaring addressing modes
- [var rAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/raddressmode.md)
  The address mode for the texture depth (r) coordinate.
- [var sAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/saddressmode.md)
  The address mode for the texture width (s) coordinate.
- [var tAddressMode: MTLSamplerAddressMode](mtlsamplerdescriptor/taddressmode.md)
  The address mode for the texture height (t) coordinate.
- [var borderColor: MTLSamplerBorderColor](mtlsamplerdescriptor/bordercolor.md)
  The border color for clamped texture values.
- [enum MTLSamplerAddressMode](mtlsampleraddressmode.md)
  Modes that determine the texture coordinate at each pixel when a fetch falls outside the bounds of a texture.
- [enum MTLSamplerBorderColor](mtlsamplerbordercolor.md)
  Values that determine the border color for clamped texture values when the sampler address mode is [`MTLSamplerAddressMode.clampToBorderColor`](mtlsampleraddressmode/clamptobordercolor.md).
### Declaring filter modes
- [var minFilter: MTLSamplerMinMagFilter](mtlsamplerdescriptor/minfilter.md)
  The filtering option for combining pixels within one mipmap level when the sample footprint is larger than a pixel (minification).
- [var magFilter: MTLSamplerMinMagFilter](mtlsamplerdescriptor/magfilter.md)
  The filtering operation for combining pixels within one mipmap level when the sample footprint is smaller than a pixel (magnification).
- [var mipFilter: MTLSamplerMipFilter](mtlsamplerdescriptor/mipfilter.md)
  The filtering option for combining pixels between two mipmap levels.
- [var lodMinClamp: Float](mtlsamplerdescriptor/lodminclamp.md)
  The minimum level of detail (LOD) to use when sampling from a texture.
- [var lodMaxClamp: Float](mtlsamplerdescriptor/lodmaxclamp.md)
  The maximum level of detail (LOD) to use when sampling from a texture.
- [var lodAverage: Bool](mtlsamplerdescriptor/lodaverage.md)
  A Boolean value that specifies whether the GPU can use an average level of detail (LOD) when sampling from a texture.
- [var maxAnisotropy: Int](mtlsamplerdescriptor/maxanisotropy.md)
  The number of samples that can be taken to improve the quality of sample footprints that are anisotropic.
- [enum MTLSamplerMinMagFilter](mtlsamplerminmagfilter.md)
  Filtering options for determining which pixel value is returned within a mipmap level.
- [enum MTLSamplerMipFilter](mtlsamplermipfilter.md)
  Filtering options for determining what pixel value is returned with multiple mipmap levels.
### Declaring the depth comparison mode
- [var compareFunction: MTLCompareFunction](mtlsamplerdescriptor/comparefunction.md)
  The sampler comparison function used when performing a sample compare operation on a depth texture.
- [enum MTLCompareFunction](mtlcomparefunction.md)
  Options used to specify how a sample compare operation should be performed on a depth texture.
### Declaring whether the sampler can be used in argument buffers
- [var supportArgumentBuffers: Bool](mtlsamplerdescriptor/supportargumentbuffers.md)
  A Boolean value that indicates whether you can reference a sampler, that you make with this descriptor, by its resource ID from an argument buffer.
### Identifying the sampler
- [var label: String?](mtlsamplerdescriptor/label.md)
  A string that identifies the sampler.
### Instance Properties
- [var lodBias: Float](mtlsamplerdescriptor/lodbias.md)
  Sets the level-of-detail (lod) bias when sampling from a texture.
- [var reductionMode: MTLSamplerReductionMode](mtlsamplerdescriptor/reductionmode.md)
  Sets the reduction mode for filtering contributing samples.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Creating and sampling textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.
- [protocol MTLSamplerState](mtlsamplerstate.md)
  An instance that defines how a texture should be sampled.
- [struct MTLSamplePosition](mtlsampleposition.md)
  A subpixel sample position for use in multisample antialiasing (MSAA).
- [enum MTLSamplerReductionMode](mtlsamplerreductionmode.md)
  Configures how the sampler aggregates contributing samples to a final value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsamplerdescriptor)*