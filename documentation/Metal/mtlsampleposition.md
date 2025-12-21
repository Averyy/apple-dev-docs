# MTLSamplePosition

**Framework**: Metal  
**Kind**: struct

A subpixel sample position for use in multisample antialiasing (MSAA).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLSamplePosition
```

## Mentions

- [Positioning samples programmatically](positioning-samples-programmatically.md)

#### Overview

Subpixel sample positions are in a 16 x 16 grid across a pixel. Each subsample position’s [`x`](mtlsampleposition/x.md) and [`y`](mtlsampleposition/y.md) values are in 1/16 increments in the floating-point range `[0.0, 15.0/16.0)`. The pixel’s origin point `(0,0)` is at the top-left corner.

See [`Positioning samples programmatically`](positioning-samples-programmatically.md) for the details on working with subpixels.

## Topics

### Initializers
- [init()](mtlsampleposition/init.md)
  Returns a new sample position on a subpixel grid.
- [init(x: Float, y: Float)](mtlsampleposition/init(x:y:).md)
  Returns a new sample position on a subpixel grid at specified coordinates.
### Instance Properties
- [var x: Float](mtlsampleposition/x.md)
  The x position of the sample on the subpixel grid.
- [var y: Float](mtlsampleposition/y.md)
  The y position of the sample on the subpixel grid.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Creating and sampling textures](creating-and-sampling-textures.md)
  Load image data into a texture and apply it to a quadrangle.
- [protocol MTLSamplerState](mtlsamplerstate.md)
  An instance that defines how a texture should be sampled.
- [class MTLSamplerDescriptor](mtlsamplerdescriptor.md)
  An object that you use to configure a texture sampler.
- [enum MTLSamplerReductionMode](mtlsamplerreductionmode.md)
  Configures how the sampler aggregates contributing samples to a final value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlsampleposition)*