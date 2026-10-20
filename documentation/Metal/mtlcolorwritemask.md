# MTLColorWriteMask

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

Values used to specify a mask to permit or restrict writing to color channels of a color value.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
struct MTLColorWriteMask
```

```c
enum MTLColorWriteMask : NSUInteger;
```

#### Overview

The values [`red`](./mtlcolorwritemask/red.md), [`green`](./mtlcolorwritemask/green.md), [`blue`](./mtlcolorwritemask/blue.md), and [`alpha`](./mtlcolorwritemask/alpha.md) select one color channel each, and they can be bitwise combined.

## Topics

### Initializers
- [init(rawValue: UInt)](./mtlcolorwritemask/init%28rawvalue%29.md)
  Returns a new color write mask from a specified raw value.
### Type Properties
- [static var all: MTLColorWriteMask](./mtlcolorwritemask/all.md)
  All color channels are enabled.
- [static var alpha: MTLColorWriteMask](./mtlcolorwritemask/alpha.md)
  The alpha color channel is enabled.
- [static var blue: MTLColorWriteMask](./mtlcolorwritemask/blue.md)
  The blue color channel is enabled.
- [static var green: MTLColorWriteMask](./mtlcolorwritemask/green.md)
  The green color channel is enabled.
- [static var red: MTLColorWriteMask](./mtlcolorwritemask/red.md)
  The red color channel is enabled.
- [static var unspecialized: MTLColorWriteMask](./mtlcolorwritemask/unspecialized.md)
  Defers assigning the color write mask.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Configuring render pipeline states
- [var pixelFormat: MTLPixelFormat](./mtlrenderpipelinecolorattachmentdescriptor/pixelformat.md)
  The pixel format of the color attachment’s texture.
- [var writeMask: MTLColorWriteMask](./mtlrenderpipelinecolorattachmentdescriptor/writemask.md)
  A bitmask that restricts which color channels are written into the texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcolorwritemask)*