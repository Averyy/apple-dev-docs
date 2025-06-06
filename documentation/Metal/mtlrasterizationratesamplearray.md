# MTLRasterizationRateSampleArray

**Framework**: Metal  
**Kind**: class

An array object that contains rasterization rates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.4+
- macOS 10.15.4+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLRasterizationRateSampleArray
```

#### Overview

The [`horizontal`](mtlrasterizationratelayerdescriptor/horizontal.md) and [`vertical`](mtlrasterizationratelayerdescriptor/vertical.md) properties of a [`MTLRasterizationRateLayerDescriptor`](mtlrasterizationratelayerdescriptor.md) point to [`MTLRasterizationRateSampleArray`](mtlrasterizationratesamplearray.md) objects that contains rasterization rates for the layer map. You can use array subscript syntax to access the samples. [`MTLRasterizationRateSampleArray`](mtlrasterizationratesamplearray.md) objects perform bounds checking on any accesses you make to their sample data.

## Topics

### Accessing the Array
- [subscript(Int) -> Float](mtlrasterizationratesamplearray/subscript(_:).md)
  Retrieves the sample value at the specified index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var sampleCount: MTLSize](mtlrasterizationratelayerdescriptor/samplecount.md)
  The number of rows and columns in the layer map.
- [var maxSampleCount: MTLSize](mtlrasterizationratelayerdescriptor/maxsamplecount.md)
  The maximum number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](mtlrasterizationratelayerdescriptor/horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [var vertical: MTLRasterizationRateSampleArray](mtlrasterizationratelayerdescriptor/vertical.md)
  The vertical rasterization rates for the layer map’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratesamplearray)*