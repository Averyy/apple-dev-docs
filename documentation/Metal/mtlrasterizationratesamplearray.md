# MTLRasterizationRateSampleArray

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An array instance that contains rasterization rates.

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

```objc
@interface MTLRasterizationRateSampleArray : NSObject
```

#### Overview

The [`horizontal`](./mtlrasterizationratelayerdescriptor/horizontal.md) and [`vertical`](./mtlrasterizationratelayerdescriptor/vertical.md) properties of an [`MTLRasterizationRateLayerDescriptor`](./mtlrasterizationratelayerdescriptor.md) point to [`MTLRasterizationRateSampleArray`](./mtlrasterizationratesamplearray.md) instances that contains rasterization rates for the layer map. You can use array subscript syntax to access the samples. [`MTLRasterizationRateSampleArray`](./mtlrasterizationratesamplearray.md) instances perform bounds checking on any memory operations you make to their sample data.

## Topics

### Accessing the array
- [subscript(Int) -> Float](./mtlrasterizationratesamplearray/subscript%28_%29.md)
  Retrieves the sample value at the specified index.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Inspecting the layer rate function parameters
- [var sampleCount: MTLSize](./mtlrasterizationratelayerdescriptor/samplecount.md)
  The number of rows and columns in the layer map.
- [var maxSampleCount: MTLSize](./mtlrasterizationratelayerdescriptor/maxsamplecount.md)
  The maximum number of rows and columns in the layer map.
- [var horizontal: MTLRasterizationRateSampleArray](./mtlrasterizationratelayerdescriptor/horizontal.md)
  The horizontal rasterization rates for the layer map’s rows.
- [var vertical: MTLRasterizationRateSampleArray](./mtlrasterizationratelayerdescriptor/vertical.md)
  The vertical rasterization rates for the layer map’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrasterizationratesamplearray)*