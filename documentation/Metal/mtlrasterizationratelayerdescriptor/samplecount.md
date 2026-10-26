# sampleCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) MTLSize sampleCount;
```

#### Discussion

The [`sampleCount`](./samplecount.md) property splits the logical viewport coordinate space into a 2D grid of equal-sized cells. Its [`depth`](../mtlsize/depth.md) value is always `0`.

The default value is the same as [`maxSampleCount`](./maxsamplecount.md).

## See Also

### Inspecting the layer rate function parameters
- [var maxSampleCount: MTLSize](./maxsamplecount.md)
  The maximum number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](./horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [var vertical: MTLRasterizationRateSampleArray](./vertical.md)
  The vertical rasterization rates for the layer map’s rows.
- [class MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md)
  An array instance that contains rasterization rates.
- [horizontalSampleStorage](./horizontalsamplestorage.md)
  A pointer to the storage for the layer map’s horizontal rasterization rates.
- [verticalSampleStorage](./verticalsamplestorage.md)
  A pointer to the storage for the layer map’s vertical rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/samplecount)*