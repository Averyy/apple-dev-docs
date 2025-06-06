# BNNSMatMul(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a matrix multiplication operation directly to two input matrices.

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
func BNNSMatMul(_ transA: Bool, _ transB: Bool, _ alpha: Float, _ inputA: UnsafePointer<BNNSNDArrayDescriptor>, _ inputB: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafePointer<BNNSNDArrayDescriptor>, _ workspace: UnsafeMutableRawPointer?, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int32
```

#### Discussion

Use this function to perform the operation `C = alpha * op(A) * op(B)` where `op` transposes the corresponding matrix if the appropriate transpose parameter is `true`. The function broadcasts dimensions that are absent on either input matrix. The matrix multiplication is always on the final two indices of each operand.

For example, the following arrays of values and descriptors for the matrix multiply inputs and outputs define a matrix multiplication operation without broadcasting. Note that the operation repeats the values in `inputBValues` along the third dimension.

```swift
let inputAValues: [Float] = [
    [ 24 values ]
]

let inputBValues: [Float] = [
    1, 2,
    3, 4,
    
    1, 2,
    3, 4,
    
    1, 2,
    3, 4
]

var inputADescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: inputAValues,
    shape: .imageCHW(3, 4, 2))

var inputBDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: inputBValues,
    shape: .tensor3DFirstMajor(3, 2, 2))

var outputDescriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .imageCHW(inputADescriptor.shape.size.0,
                     inputADescriptor.shape.size.1,
                     inputBDescriptor.shape.size.1))
```

The [`BNNSMatMul(_:_:_:_:_:_:_:_:)`](bnnsmatmul(_:_:_:_:_:_:_:_:).md) function calculates the same result using a 2 x 2 matrix.

```swift
let inputBValues: [Float] = [
    1, 2,
    3, 4
]

var inputBDescriptor = BNNSNDArrayDescriptor.allocate(
    initializingFrom: inputBValues,
    shape: .matrixFirstMajor(2, 2))
```

In both cases, the call to the matrix multiply function is the same.

```swift
BNNSMatMul(false, false,
           1,
           &inputADescriptor, &inputBDescriptor,
           &outputDescriptor,
           nil, nil)
```

You may optionally pass a workspace to [`BNNSMatMul(_:_:_:_:_:_:_:_:)`](bnnsmatmul(_:_:_:_:_:_:_:_:).md). Call [`BNNSMatMulWorkspaceSize(_:_:_:_:_:_:_:)`](bnnsmatmulworkspacesize(_:_:_:_:_:_:_:).md) to calculate the required workspace size for a set of parameters. If you pass `nil` to the [`BNNSMatMul(_:_:_:_:_:_:_:_:)`](bnnsmatmul(_:_:_:_:_:_:_:_:).md) workspace parameter, BNNS allocates and dellocates the workspace.

## Parameters

- `transA`: A Boolean value that specifies whether the operation should treat   as transposed.
- `transB`: A Boolean value that specifies whether the operation should treat   as transposed.
- `alpha`: A value that the operation uses to scale the result.
- `inputA`: A pointer to the   matrix descriptor.
- `inputB`: A pointer to the   matrix descriptor.
- `output`: A pointer to the output matrix descriptor.
- `workspace`: An optional pointer to the workspace memory. Use   to calculate the workspace size that operation requires.   doesn’t require any particular alignment for the workspace memory.
- `filter_params`: The filter runtime parameters.

## See Also

- [func BNNSDirectApplyBroadcastMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?)](bnnsdirectapplybroadcastmatmul(_:_:_:_:_:_:_:).md)
  Applies a broadcast matrix multiplication operation directly to two input matrices.
- [class BroadcastMatrixMultiplyLayer](bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
- [struct BNNSLayerParametersBroadcastMatMul](bnnslayerparametersbroadcastmatmul.md)
  A set of parameters that define a broadcast matrix multiply layer.
- [func BNNSFilterCreateLayerBroadcastMatMul(UnsafePointer<BNNSLayerParametersBroadcastMatMul>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerbroadcastmatmul(_:_:).md)
  Returns a new broadcast matrix multiply layer.
- [func BNNSMatMulWorkspaceSize(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int](bnnsmatmulworkspacesize(_:_:_:_:_:_:_:).md)
  Returns the workspace size that a matrix multiply operation requires.
- [static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](bnns/applymatrixmultiplication(inputa:transposed:inputb:transposed:output:alpha:workspace:filterparameters:).md)
  Performs a matrix multiplication operation directly on two input matrices.
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](bnns/matrixmultiplicationworkspacesize(inputa:transposed:inputb:transposed:output:alpha:filterparameters:).md)
  Returns the workspace size that a matrix multiply operation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsmatmul(_:_:_:_:_:_:_:_:))*