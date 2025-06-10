# scatter(input:indices:output:axis:reductionFunction:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Scatters the elements of a tensor along a single axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
static func scatter(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters? = nil) throws
```

## Parameters

- `input`: The input descriptor.
- `indices`: The indices descriptor.
- `output`: The output descriptor.
- `axis`: The axis along which the operation scatters elements.
- `reductionFunction`: The reduction operation that the function uses to reduce existing output value with scattered value.
- `filterParameters`: The runtime filter parameters.

## See Also

- [func BNNSScatter(Int, BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatter(_:_:_:_:_:_:).md)
  Scatters the elements of a tensor along a single axis.
- [Calculating the dominant colors in an image](calculating-the-dominant-colors-in-an-image.md)
  Find the main colors in an image by implementing k-means clustering using the Accelerate framework.
- [static func gather(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, filterParameters: BNNSFilterParameters?) throws](bnns/gather(input:indices:output:axis:filterparameters:).md)
  Gathers the elements of a tensor along a single axis.
- [static func gatherND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/gathernd(input:indices:output:filterparameters:).md)
  Gathers the slices of a tensor.
- [static func scatterND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters?) throws](bnns/scatternd(input:indices:output:reductionfunction:filterparameters:).md)
  Scatters the slices of a tensor.
- [func BNNSGather(Int, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsgather(_:_:_:_:_:).md)
  Gathers the elements of a tensor along a single axis.
- [func BNNSGatherND(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsgathernd(_:_:_:_:).md)
  Gathers the slices of a tensor.
- [func BNNSScatter(Int, BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatter(_:_:_:_:_:_:).md)
  Scatters the elements of a tensor along a single axis.
- [func BNNSScatterND(BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatternd(_:_:_:_:_:).md)
  Scatters the slices of a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/scatter(input:indices:output:axis:reductionfunction:filterparameters:))*