# MPSOrigin

**Framework**: Metal Performance Shaders  
**Kind**: struct

A position in an image used as the source origin.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSOrigin
```

#### Overview

The `double` data type is used because some kernel operations require fractional precision—for example, the [`MPSImageLanczosScale`](mpsimagelanczosscale.md) filter.

## Topics

### Fields
- [var x: Double](mpsorigin/x.md)
  The x coordinate of the position, in pixels.
- [var y: Double](mpsorigin/y.md)
  The y coordinate of the position, in pixels.
- [var z: Double](mpsorigin/z.md)
  The z coordinate of the position, in pixels.
### Initializers
- [init()](mpsorigin/init.md)
- [init(x: Double, y: Double, z: Double)](mpsorigin/init(x:y:z:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsorigin)*