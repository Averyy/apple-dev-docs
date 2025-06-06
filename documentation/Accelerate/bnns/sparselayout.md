# BNNS.SparseLayout

**Framework**: Accelerate  
**Kind**: enum

Constants that specify standardized sparse layouts that BNNS can convert to opaque.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
enum SparseLayout
```

## Topics

### Enumeration Cases
- [case coo(indices: BNNSNDArrayDescriptor)](bnns/sparselayout/coo(indices:).md)
  The sparse coordinate list (COO) format.
- [case csr(columnIndices: BNNSNDArrayDescriptor, rowStarts: BNNSNDArrayDescriptor)](bnns/sparselayout/csr(columnindices:rowstarts:).md)
  The compressed sparse row (CSR) format.

## See Also

- [func BNNSNDArrayGetDataSize(UnsafePointer<BNNSNDArrayDescriptor>) -> Int](bnnsndarraygetdatasize(_:).md)
  Returns the size, in bytes, that an array descriptor requires.
- [func BNNSNDArrayFullyConnectedSparsifySparseCOO(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsndarrayfullyconnectedsparsifysparsecoo(_:_:_:_:_:_:_:_:_:).md)
  Converts a sparse tensor from the standardized coordinate list (COO) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [func BNNSNDArrayFullyConnectedSparsifySparseCSR(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsndarrayfullyconnectedsparsifysparsecsr(_:_:_:_:_:_:_:_:_:_:).md)
  Converts a sparse tensor from the standardized compressed sparse row (CSR) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [static func sparsify(batchSize: Int, inputLayout: BNNS.SparseLayout, inputDenseShape: BNNSNDArrayDescriptor, inputValues: BNNSNDArrayDescriptor, output: inout BNNSNDArrayDescriptor, sparseParameters: BNNS.SparseParameters?, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](bnns/fullyconnectedlayer/sparsify(batchsize:inputlayout:inputdenseshape:inputvalues:output:sparseparameters:workspace:filterparameters:).md)
  Converts a sparse tensor from a standardized sparse layout to a device-specific sparse layout that Fully Connected uses.
- [struct SparseParameters](bnns/sparseparameters.md)
  A data structure that provides a hint to the sparsity function.
- [BNNS.SparsityType](bnns/sparsitytype.md)
  Constants that specify patterns in the sparsity.
- [var BNNSSparsityTypeUnstructured: BNNSSparsityType](bnnssparsitytypeunstructured.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sparselayout)*