# verticalSampleStorage

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A pointer to the storage for the layer map’s vertical rasterization rates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) float * verticalSampleStorage;
```

#### Discussion

Points to the first element in the array of vertical rasterization rates. The number of elements is equal to the [`height`](../mtlsize/height.md) value of [`sampleCount`](./samplecount.md).

## See Also

### Inspecting the layer rate function parameters
- [var sampleCount: MTLSize](./samplecount.md)
  The number of rows and columns in the layer map.
- [var maxSampleCount: MTLSize](./maxsamplecount.md)
  The maximum number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](./horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [var vertical: MTLRasterizationRateSampleArray](./vertical.md)
  The vertical rasterization rates for the layer map’s rows.
- [horizontalSampleStorage](./horizontalsamplestorage.md)
  A pointer to the storage for the layer map’s horizontal rasterization rates.
- [class MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md)
  An array instance that contains rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/verticalsamplestorage)*