# BNNSScatterND(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Scatters the slices of a tensor.

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
func BNNSScatterND(_ op: BNNSReduceFunction, _ input: UnsafePointer<BNNSNDArrayDescriptor>, _ indices: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use [`BNNSScatterND(_:_:_:_:_:)`](bnnsscatternd(_:_:_:_:_:).md) to scatter slices — that you specify by index — into an output tensor.

The function interprets the indices array as a `k - 1` dimensional set of lookup vectors, therefore, the indices tensor must have `(k - 1) + 1` or `k` dimensions.

If the lookup vectors don’t define a full set of indices, the function treats the undefined indices as a slice.

[`BNNSScatterND(_:_:_:_:_:)`](bnnsscatternd(_:_:_:_:_:).md) is the inverse of [`BNNSGatherND(_:_:_:_:)`](bnnsgathernd(_:_:_:_:).md). The code samples below are based on the gathered values from the [`BNNSGatherND(_:_:_:_:)`](bnnsgathernd(_:_:_:_:).md) page.

The following code shows that a scalar index scatters a 2D slice:

```swift
let indices: [Int32] = [1] 
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .vector(1))
    
let gathereredValues: [Float] = [20.0, 21.0, 22.0, 23.0]
var gatheredDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: gathereredValues,
    shape: .matrixFirstMajor(2, 2))

var scatteredDescriptor = BNNSNDArrayDescriptor.allocate(
    repeating: Float(),
    shape: inputDescriptor.shape)

BNNSScatterND(BNNSReduceFunctionNone,
              &gatheredDescriptor,
              &indicesDescriptor,
              &scatteredDescriptor,
              nil)
```

On return, `scatteredDescriptor` contains the following values:

```swift
[ 0.0,  0.0,
  0.0,  0.0,

 20.0, 21.0,
 22.0, 23.0,

  0.0,  0.0,
  0.0,  0.0 ]
```

The following code shows that a 2D index scatters a 1D slice:

```swift
let indices: [Int32] = [1, 0] 
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .matrixFirstMajor(1, 2))
    
let gathereredValues: [Float] = [20.0, 21.0]
var gatheredDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: gathereredValues,
    shape: .matrixFirstMajor(1, 2))

var scatteredDescriptor = BNNSNDArrayDescriptor.allocate(
    repeating: Float(),
    shape: inputDescriptor.shape)

BNNSScatterND(BNNSReduceFunctionNone,
              &gatheredDescriptor,
              &indicesDescriptor,
              &scatteredDescriptor,
              nil)  
```

On return, `scatteredDescriptor` contains the following values:

```swift
[ 0.0,  0.0,
  0.0,  0.0,

 20.0, 21.0,
  0.0,  0.0,

  0.0,  0.0,
  0.0,  0.0 ]
```

The following code shows that a 3D index scatters a single element:

```swift
let indices: [Int32] = [
    1, 1, 1 
]
var indicesDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: indices,
    shape: .tensor3DFirstMajor(1, 1, 3))

let gathereredValues: [Float] = [23]
var gatheredDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: gathereredValues,
    shape: .matrixFirstMajor(1, 1))

var scatteredDescriptor = BNNSNDArrayDescriptor.allocate(
    repeating: Float(),
    shape: inputDescriptor.shape)

BNNSScatterND(BNNSReduceFunctionNone,
              &gatheredDescriptor,
              &indicesDescriptor,
              &scatteredDescriptor,
              nil)
```

On return, `scatteredDescriptor` contains the following values:

```swift
[ 0.0,  0.0,
  0.0,  0.0,

  0.0,  0.0,
  0.0, 23.0,

  0.0,  0.0,
  0.0,  0.0 ]
```

If multiple input values update the same output element, the function doesn’t define the order of update operations.

In particular, if you define the reduction as `BNNSReduceFunctionNone` the function doesn’t guarantee any particular value in the result.

## Parameters

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
- [func BNNSScatter(Int, BNNSReduceFunction, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsscatter(_:_:_:_:_:_:).md)
  Scatters the elements of a tensor along a single axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsscatternd(_:_:_:_:_:))*