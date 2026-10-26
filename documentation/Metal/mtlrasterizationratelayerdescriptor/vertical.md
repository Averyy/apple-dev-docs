# vertical

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The vertical rasterization rates for the layer map’s rows.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var vertical: MTLRasterizationRateSampleArray { get }
```

```objc
@property (nonatomic, readonly) MTLRasterizationRateSampleArray * vertical;
```

## See Also

### Inspecting the layer rate function parameters
- [var sampleCount: MTLSize](./samplecount.md)
  The number of rows and columns in the layer map.
- [var maxSampleCount: MTLSize](./maxsamplecount.md)
  The maximum number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](./horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [class MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md)
  An array instance that contains rasterization rates.
- [horizontalSampleStorage](./horizontalsamplestorage.md)
  A pointer to the storage for the layer map’s horizontal rasterization rates.
- [verticalSampleStorage](./verticalsamplestorage.md)
  A pointer to the storage for the layer map’s vertical rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/vertical)*