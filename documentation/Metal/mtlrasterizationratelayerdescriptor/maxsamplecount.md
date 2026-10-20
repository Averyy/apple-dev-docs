# maxSampleCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The maximum number of rows and columns in the layer map.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxSampleCount: MTLSize { get }
```

```objc
@property (nonatomic, readonly) MTLSize maxSampleCount;
```

#### Discussion

Its [`depth`](../mtlsize/depth.md) value is always `0`.

## See Also

### Inspecting the layer rate function parameters
- [var sampleCount: MTLSize](./samplecount.md)
  The number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](./horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [var vertical: MTLRasterizationRateSampleArray](./vertical.md)
  The vertical rasterization rates for the layer map’s rows.
- [class MTLRasterizationRateSampleArray](../mtlrasterizationratesamplearray.md)
  An array instance that contains rasterization rates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratelayerdescriptor/maxsamplecount)*