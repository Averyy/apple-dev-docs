# BNNSGather(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Gathers the elements of a tensor along a single axis.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func BNNSGather(_ axis: Int, _ input: UnsafePointer<BNNSNDArrayDescriptor>, _ indices: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use [`BNNSGather(_:_:_:_:_:)`](bnnsgather(_:_:_:_:_:).md) to gather elements — that you specify by index — into an output tensor.

In the simplest case, use [`BNNSGather(_:_:_:_:_:)`](bnnsgather(_:_:_:_:_:).md) to gather elements from a 1D vector with indices defined as a 1D vector. The following code gathers the four elements at indices `[1, 3, 7, 5]`:

```swift
let values: [Float] = [10, 20, 30, 40, 50, 60, 70, 80]
var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .vector(values.count))

let indices: [Int32] = [1, 3, 7, 5]
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .vector(indices.count))

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: indicesDescriptor.shape)

let error = BNNSGather(0,
                       &inputDescriptor,
                       &indicesDescriptor,
                       &outputDescriptor,
                       nil)

```

On return, `outputDescriptor` contains the values `[20.0, 40.0, 80.0, 60.0]`.

[`BNNSGather(_:_:_:_:_:)`](bnnsgather(_:_:_:_:_:).md) supports gathering from a tensor with two or more dimensions using indices defined as a 1D vector. In this case, the indices correspond to the values along an entire axis and the input and output shapes must match.

The following code generates a 3 x 4 matrix from the rows of a 3 x 3 matrix:

```swift
let values: [Float] = [10, 20, 30,
                       40, 50, 60,
                       70, 80, 90]
var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .matrixRowMajor(3, 3))

let indices: [Int32] = [0, 1, // Elements `0, 1` from row `0` = `10, 20`
                        2, 0, // Elements `2, 0` from row `1` = `60, 40`
                        1, 1] // Elements `1, 1` from row `2` = `80, 80`
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .matrixRowMajor(2, 3))

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: indicesDescriptor.shape)

let error = BNNSGather(1, // axis
                       &inputDescriptor,
                       &indicesDescriptor,
                       &outputDescriptor,
                       nil)
```

On return, `outputDescriptor` contains the following values:

```swift
 [ 10.0, 20.0,
   60.0, 40.0,
   80.0, 80.0 ]
```

The function returns an error if any of the indices are out of range.

## Parameters

- `axis`: The axis along which the operation gathers the indices.
- `input`: A pointer to the input descriptor.
- `indices`: A pointer to the indices descriptor.
- `output`: A pointer to the output descriptor.
- `filter_params`: The filter runtime parameters.

## See Also

- [Calculating the dominant colors in an image](calculating-the-dominant-colors-in-an-image.md)
  Find the main colors in an image by implementing k-means clustering using the Accelerate framework.
- [static func gather(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, filterParameters: BNNSFilterParameters?) throws](bnns/gather(input:indices:output:axis:filterparameters:).md)
  Gathers the elements of a tensor along a single axis.
- [static func gatherND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](bnns/gathernd(input:indices:output:filterparameters:).md)
  Gathers the slices of a tensor.
- [static func scatter(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters?) throws](bnns/scatter(input:indices:output:axis:reductionfunction:filterparameters:).md)
  Scatters the elements of a tensor along a single axis.
- [static func scatterND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters?) throws](bnns/scatternd(input:indices:output:reductionfunction:filterparameters:).md)
  Scatters the slices of a tensor.
- [func BNNSGatherND(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsgathernd(_:_:_:_:).md)
  Gathers the slices of a tensor.
- [func BNNSScatter(Int, BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatter(_:_:_:_:_:_:).md)
  Scatters the elements of a tensor along a single axis.
- [func BNNSScatterND(BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatternd(_:_:_:_:_:).md)
  Scatters the slices of a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgather(_:_:_:_:_:))*