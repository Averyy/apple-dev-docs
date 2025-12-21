# sparsify(batchSize:inputLayout:inputDenseShape:inputValues:output:sparseParameters:workspace:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Converts a sparse tensor from a standardized sparse layout to a device-specific sparse layout that Fully Connected uses.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static func sparsify(batchSize: Int = 1, inputLayout layout: BNNS.SparseLayout, inputDenseShape: BNNSNDArrayDescriptor, inputValues: BNNSNDArrayDescriptor, output: inout BNNSNDArrayDescriptor, sparseParameters: BNNS.SparseParameters? = nil, workspace: UnsafeMutableRawBufferPointer? = nil, filterParameters: BNNSFilterParameters? = nil) throws
```

## Parameters

- `batchSize`: The number of input-output pairs to process.
- `layout`: The layout and nonzero indices of the sparse input.
- `inputDenseShape`: The dense shape of the sparse 2D input.
- `inputValues`: A 1D array descriptor that contains the nonzero input values.
- `output`: The destination array descriptor that contains the output-device-optimized BNNS Sparse Fully Connected weights.
- `sparseParameters`: An optional data structure that provides a hint to the sparsity function.
- `workspace`: An optional pointer to a memory region that the function uses as scratch space.
- `filterParameters`: The runtime filter parameters.

## See Also

- [func BNNSNDArrayGetDataSize(UnsafePointer<BNNSNDArrayDescriptor>) -> Int](bnnsndarraygetdatasize(_:).md)
  Returns the size, in bytes, that an array descriptor requires.
- [func BNNSNDArrayFullyConnectedSparsifySparseCOO(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsndarrayfullyconnectedsparsifysparsecoo(_:_:_:_:_:_:_:_:_:).md)
  Converts a sparse tensor from the standardized coordinate list (COO) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [func BNNSNDArrayFullyConnectedSparsifySparseCSR(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsndarrayfullyconnectedsparsifysparsecsr(_:_:_:_:_:_:_:_:_:_:).md)
  Converts a sparse tensor from the standardized compressed sparse row (CSR) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [struct SparseParameters](bnns/sparseparameters.md)
  A data structure that provides a hint to the sparsity function.
- [BNNS.SparseLayout](bnns/sparselayout.md)
  Constants that specify standardized sparse layouts that BNNS can convert to opaque.
- [BNNS.SparsityType](bnns/sparsitytype.md)
  Constants that specify patterns in the sparsity.
- [var BNNSSparsityTypeUnstructured: BNNSSparsityType](bnnssparsitytypeunstructured.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fullyconnectedlayer/sparsify(batchsize:inputlayout:inputdenseshape:inputvalues:output:sparseparameters:workspace:filterparameters:))*