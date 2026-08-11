# NDArray.InterleaveLayout

**Framework**: Core AI  
**Kind**: struct

Describes the interleaved memory layout of an ndArray dimension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct InterleaveLayout
```

#### Overview

An interleaved layout means that elements of the interleaved `dimension` are stored in physically contiguous blocks of `factor` elements (stride 1 between adjacent elements within a block). This differs from the standard layout where a dimension’s elements are separated by the strides of subsequent dimensions.

A common use case is representing an image with interleaved channels: a `[C, H, W]` tensor uses `InterleaveLayout(dimension: 0, factor: C)` to store all channels for each pixel contiguously — like `RGBRGB...` — rather than in separate planar slices — like `RRR...GGG...BBB...`. More generally, this can be useful for optimizing the layout of an ndArray based on how the later compute will access it.

#### Stride Semantics

The stride for the interleaved dimension (as reported by [`strides`](ndarray/strides.md)) is a *block stride* — the distance in memory between adjacent blocks of `factor` elements, not between individual elements. Within a block, adjacent elements have stride 1. The element offset formula is:

```swift
// Given strides and InterleaveLayout with dimension d and factor f:
// offset = (index[d] / f) * strides[d] + (index[d] % f)
//        + Σ index[i] * strides[i]  for all i ≠ d
```

#### Equivalence with Shapestride Transformations

When `factor` divides the size of the interleaved dimension evenly, the layout can equivalently be expressed as a shape/stride transformation without interleave metadata. For example, for `shape=[8, 256, 256]` with `InterleaveLayout(dimension: 0, factor: 4)`:

```swift
// Interleaved representation:
shape=[8, 256, 256], strides=[262144, 1024, 4]
interleaveLayout=InterleaveLayout(dimension: 0, factor: 4)

// Equivalent shape/stride form (no interleave needed):
shape=[2, 256, 256, 4], strides=[262144, 1024, 4, 1]
interleaveLayout=nil
```

The interleaved form preserves the original logical shape; the equivalent form makes the blocking explicit as an extra dimension.

When `factor` does not divide the dimension size evenly, the shape/stride equivalence is not possible. In such case the interleaved representation is the only way to express the layout.

## Topics

### Creating a layout
- [init(dimension: Int, factor: Int)](ndarray/interleavelayout-swift.struct/init(dimension:factor:).md)
### Inspecting the layout
- [var dimension: Int](ndarray/interleavelayout-swift.struct/dimension.md)
  The index of the interleaved dimension.
- [var factor: Int](ndarray/interleavelayout-swift.struct/factor.md)
  The number of elements from the interleaved dimension stored contiguously per block. Adjacent elements within a block have stride 1 in memory.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/interleavelayout-swift.struct)*