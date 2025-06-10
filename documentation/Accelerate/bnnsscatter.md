# BNNSScatter(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Scatters the elements of a tensor along a single axis.

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
func BNNSScatter(_ axis: Int, _ op: BNNSReduceFunction, _ input: UnsafePointer<BNNSNDArrayDescriptor>, _ indices: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use [`BNNSScatter(_:_:_:_:_:_:)`](bnnsscatter(_:_:_:_:_:_:).md) to scatter elements — that you specify by index — into an output tensor. The operation can set the scattered values or add them to the existing values in the output tensor.

In the simplest case, use [`BNNSScatter(_:_:_:_:_:_:)`](bnnsscatter(_:_:_:_:_:_:).md) to gather elements from a 1D vector with indices defined as a 1D vector. The following code scatters the values `[2, 4, 6, 8]` to the output elements at indices `[1, 3, 7, 5]`. The operation sums the scattered values with the existing values:

```swift
let values: [Float] = [2, 4, 6, 8]
var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .vector(values.count))

let indices: [Int32] = [1, 3, 7, 5]
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .vector(indices.count))

let outputValues: [Float] = [10, 20, 30, 40, 50, 60, 70, 80]
var outputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: outputValues,
    shape: .vector(outputValues.count))

let error = BNNSScatter(0,
                        BNNSReduceFunctionSum,
                        &inputDescriptor,
                        &indicesDescriptor,
                        &outputDescriptor,
                        nil)
```

On return, `outputDescriptor` contains the values `[10.0, 22.0, 30.0, 44.0, 50.0, 68.0, 70.0, 86.0]`. For example, `44.0` is the sum of the original value, `40`, and the scattered value, `4`.

[`BNNSScatter(_:_:_:_:_:_:)`](bnnsscatter(_:_:_:_:_:_:).md) supports scattering values from a tensor with two or more dimensions using indices defined as a 1D vector. In this case, the indices correspond to the values along an entire axis and the input and output shapes must match.

The following code scatters three rows from the input tensor to rows `[1, 3, 4]` in the output tensor. In this case, the operation sets the destination value.

```swift
let values: [Float] = [10, 11, 12,
                       30, 31, 32,
                       40, 41, 42]
var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .matrixRowMajor(3, 3))

let indices: [Int32] = [1, 3, 4]
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .vector(indices.count))

var outputDescriptor = BNNSNDArrayDescriptor.allocate(
    repeating: Float(0),
    shape: .matrixRowMajor(3, 5))

let error = BNNSScatter(0, // axis
                        BNNSReduceFunctionNone,
                        &inputDescriptor,
                        &indicesDescriptor,
                        &outputDescriptor,
                        nil)
```

On return, `outputDescriptor` contains the following values:

```swift
[  0.0,  0.0,  0.0,
  10.0, 11.0, 12.0,
   0.0,  0.0,  0.0,
  30.0, 31.0, 32.0,
  40.0, 41.0, 42.0 ]
```

[`BNNSScatter(_:_:_:_:_:_:)`](bnnsscatter(_:_:_:_:_:_:).md) supports scattering from a tensor with two or more dimensions using indices with the same shape.

In the following example, the index values specify the destination row and the operation derives the destination column from the input value’s column. For example, the input value `10`, in column `0` of the input tensor, has the corresponding index `4` in the indices tensor.

```swift
let values: [Float] = [10, 20, 30,
                       40, 50, 60,
                       70, 80, 90]
var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .matrixRowMajor(3, 3))

let indices: [Int32] = [4, 2, 3, // `10` -> (4,0), `20` -> (2,1), `30` -> (3,2)
                        0, 0, 0, // `40`, `50`, `60` -> row `0`
                        2, 4, 4] // `70` -> (2,0), `80` -> (4,1), `90` -> (4,2)
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: inputDescriptor.shape)

var outputDescriptor = BNNSNDArrayDescriptor.allocate(
    repeating: Float(0),
    shape: .matrixRowMajor(3, 5))

let error = BNNSScatter(0, // axis
                        BNNSReduceFunctionNone,
                        &inputDescriptor,
                        &indicesDescriptor,
                        &outputDescriptor,
                        nil)
```

On return, `outputDescriptor` contains the following values:

```swift
[ 40.0, 50.0, 60.0,
   0.0,  0.0,  0.0,
  70.0, 20.0,  0.0,
   0.0,  0.0, 30.0,
  10.0, 80.0, 90.0 ]
```

If multiple input values update the same output element, the function doesn’t define the order of update operations.

In particular, if you define the reduction as `BNNSReduceFunctionNone` the function doesn’t guarantee any particular value in the result.

## Parameters

- `axis`: The axis along which the operation scatters elements.
- `op`: The reduction operation that defines how the function combines scattered values with existing output values.
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
- [func BNNSGather(Int, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsgather(_:_:_:_:_:).md)
  Gathers the elements of a tensor along a single axis.
- [func BNNSGatherND(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsgathernd(_:_:_:_:).md)
  Gathers the slices of a tensor.
- [func BNNSScatterND(BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatternd(_:_:_:_:_:).md)
  Scatters the slices of a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsscatter(_:_:_:_:_:_:))*