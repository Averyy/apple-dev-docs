# MPSSize

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

A size of a region in an image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSSize
```

```c
typedef struct MPSSize { ... } MPSSize;
```

## Overview

The depth of a region is usually `1.0`.

The `double` data type is used because some kernel operations require fractional precision—for example, the [`MPSImageLanczosScale`](./mpsimagelanczosscale.md) filter.

## Topics

### Fields
- [var width: Double](./mpssize/width.md)
  The width of the region, in pixels.
- [var height: Double](./mpssize/height.md)
  The height of the region, in pixels.
- [var depth: Double](./mpssize/depth.md)
  The depth of the region, in pixels.
### Initializers
- [init()](./mpssize/init%28%29.md)
- [init(width: Double, height: Double, depth: Double)](./mpssize/init%28width,height,depth%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpssize)*