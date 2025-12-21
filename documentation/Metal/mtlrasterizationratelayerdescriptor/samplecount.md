# sampleCount

**Framework**: Metal  
**Kind**: property

The number of rows and columns in the layer map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var sampleCount: MTLSize { get set }
```

#### Discussion

The [`sampleCount`](mtlrasterizationratelayerdescriptor/samplecount.md) property splits the logical viewport coordinate space into a 2D grid of equal-sized cells. Its [`depth`](mtlsize/depth.md) value is always `0`.

The default value is the same as [`maxSampleCount`](mtlrasterizationratelayerdescriptor/maxsamplecount.md).

## See Also

- [var maxSampleCount: MTLSize](mtlrasterizationratelayerdescriptor/maxsamplecount.md)
  The maximum number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](mtlrasterizationratelayerdescriptor/horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [var vertical: MTLRasterizationRateSampleArray](mtlrasterizationratelayerdescriptor/vertical.md)
  The vertical rasterization rates for the layer map’s rows.
- [class MTLRasterizationRateSampleArray](mtlrasterizationratesamplearray.md)
  An array instance that contains rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/samplecount)*