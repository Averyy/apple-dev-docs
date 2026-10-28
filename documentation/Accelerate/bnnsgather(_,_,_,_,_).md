# BNNSGather(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Gathers the elements of a tensor along a single axis.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
func BNNSGather(_ axis: Int, _ input: UnsafePointer<BNNSNDArrayDescriptor>, _ indices: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

```c
int BNNSGather(size_t axis, const BNNSNDArrayDescriptor *input, const BNNSNDArrayDescriptor *indices, BNNSNDArrayDescriptor *output, const BNNSFilterParameters *filter_params);
```

## Discussion

Use [`BNNSGather(_:_:_:_:_:)`](./bnnsgather%28_,_,_,_,_%29.md) to gather elements — that you specify by index — into an output tensor.

In the simplest case, use [`BNNSGather(_:_:_:_:_:)`](./bnnsgather%28_,_,_,_,_%29.md) to gather elements from a 1D vector with indices defined as a 1D vector. The following code gathers the four elements at indices `[1, 3, 7, 5]`:

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

[`BNNSGather(_:_:_:_:_:)`](./bnnsgather%28_,_,_,_,_%29.md) supports gathering from a tensor with two or more dimensions using indices defined as a 1D vector. In this case, the indices correspond to the values along an entire axis and the input and output shapes must match.

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

### Gather and scatter operations
- [Calculating the dominant colors in an image](./calculating-the-dominant-colors-in-an-image.md)
  Find the main colors in an image by implementing k-means clustering using the Accelerate framework.
- [static func gather(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, filterParameters: BNNSFilterParameters?) throws](./bnns/gather%28input,indices,output,axis,filterparameters%29.md)
  Gathers the elements of a tensor along a single axis.
- [static func gatherND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, filterParameters: BNNSFilterParameters?) throws](./bnns/gathernd%28input,indices,output,filterparameters%29.md)
  Gathers the slices of a tensor.
- [static func scatter(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, axis: Int, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters?) throws](./bnns/scatter%28input,indices,output,axis,reductionfunction,filterparameters%29.md)
  Scatters the elements of a tensor along a single axis.
- [static func scatterND(input: BNNSNDArrayDescriptor, indices: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, reductionFunction: BNNS.ReductionFunction, filterParameters: BNNSFilterParameters?) throws](./bnns/scatternd%28input,indices,output,reductionfunction,filterparameters%29.md)
  Scatters the slices of a tensor.
- [func BNNSGatherND(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsgathernd%28_,_,_,_%29.md)
  Gathers the slices of a tensor.
- [func BNNSScatter(Int, BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsscatter%28_,_,_,_,_,_%29.md)
  Scatters the elements of a tensor along a single axis.
- [func BNNSScatterND(BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsscatternd%28_,_,_,_,_%29.md)
  Scatters the slices of a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgather(_:_:_:_:_:))*