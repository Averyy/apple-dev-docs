# MPSOrigin

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

A position in an image used as the source origin.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSOrigin
```

```c
typedef struct MPSOrigin { ... } MPSOrigin;
```

## Overview

The `double` data type is used because some kernel operations require fractional precision—for example, the [`MPSImageLanczosScale`](./mpsimagelanczosscale.md) filter.

## Topics

### Fields
- [var x: Double](./mpsorigin/x.md)
  The x coordinate of the position, in pixels.
- [var y: Double](./mpsorigin/y.md)
  The y coordinate of the position, in pixels.
- [var z: Double](./mpsorigin/z.md)
  The z coordinate of the position, in pixels.
### Initializers
- [init()](./mpsorigin/init%28%29.md)
- [init(x: Double, y: Double, z: Double)](./mpsorigin/init%28x,y,z%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsorigin)*