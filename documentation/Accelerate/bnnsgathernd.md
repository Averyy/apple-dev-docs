# BNNSGatherND(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Gathers the slices of a tensor.

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
func BNNSGatherND(_ input: UnsafePointer<BNNSNDArrayDescriptor>, _ indices: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use [`BNNSGatherND(_:_:_:_:)`](bnnsgathernd(_:_:_:_:).md) to gather slices — that you specify by index — into an output tensor.

The function interprets the indices array as a `k - 1` dimensional set of lookup vectors, therefore, the indices tensor must have `(k - 1) + 1` or `k` dimensions.

If the lookup vectors don’t define a full set of indices, the function treats the undefined indices as a slice.

For example, given the following input values:

```swift
let values: [Float] = [10, 11,
                       12, 13,
                       
                       20, 21,
                       22, 23,
                       
                       30, 31,
                       32, 33]

var inputDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: values,
    shape: .tensor3DFirstMajor(3, 2, 2))
```

The following code shows that a scalar index gathers a 2D slice:

```swift
let indices: [Int32] = [1] // Elements `20, 21, 22, 23` from slice `1`
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .vector(1))

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .matrixFirstMajor(2, 2))

let error = BNNSGatherND(&inputDescriptor,
                         &indicesDescriptor,
                         &outputDescriptor,
                         nil)
                         
// `outputDescriptor` contains `[20.0, 21.0, 22.0, 23.0]`   
```

The following code shows that a 2D index gathers a 1D slice:

```swift
let indices: [Int32] = [1, 0] // Elements `20, 21` from row `0` of slice `1`
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .matrixFirstMajor(1, 2))

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .matrixFirstMajor(1, 2))

let error = BNNSGatherND(&inputDescriptor,
                         &indicesDescriptor,
                         &outputDescriptor,
                         nil)

// `outputDescriptor` contains `[20.0, 21.0]`
```

The following code shows that a 3D index gathers a single element:

```swift
let indices: [Int32] = [1, 1, 1] // Element `23` (index `1`) from row `1` of slice `1`
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .tensor3DFirstMajor(1, 1, 3))

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .matrixFirstMajor(1, 1))

let error = BNNSGatherND(&inputDescriptor,
                         &indicesDescriptor,
                         &outputDescriptor,
                         nil)
                         
// `outputDescriptor` contains `[23.0]`  
```

## Parameters

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
- [func BNNSScatter(Int, BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatter(_:_:_:_:_:_:).md)
  Scatters the elements of a tensor along a single axis.
- [func BNNSScatterND(BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatternd(_:_:_:_:_:).md)
  Scatters the slices of a tensor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgathernd(_:_:_:_:))*