# BNNS.SparseLayout

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that specify standardized sparse layouts that BNNS can convert to opaque.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
enum SparseLayout
```

## Topics

### Enumeration Cases
- [case coo(indices: BNNSNDArrayDescriptor)](./sparselayout/coo%28indices%29.md)
  The sparse coordinate list (COO) format.
- [case csr(columnIndices: BNNSNDArrayDescriptor, rowStarts: BNNSNDArrayDescriptor)](./sparselayout/csr%28columnindices,rowstarts%29.md)
  The compressed sparse row (CSR) format.

## See Also

### Sparse layers
- [func BNNSNDArrayGetDataSize(UnsafePointer<BNNSNDArrayDescriptor>) -> Int](../bnnsndarraygetdatasize%28_%29.md)
  Returns the size, in bytes, that an array descriptor requires.
- [func BNNSNDArrayFullyConnectedSparsifySparseCOO(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnsndarrayfullyconnectedsparsifysparsecoo%28_,_,_,_,_,_,_,_,_%29.md)
  Converts a sparse tensor from the standardized coordinate list (COO) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [func BNNSNDArrayFullyConnectedSparsifySparseCSR(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnsndarrayfullyconnectedsparsifysparsecsr%28_,_,_,_,_,_,_,_,_,_%29.md)
  Converts a sparse tensor from the standardized compressed sparse row (CSR) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [static func sparsify(batchSize: Int, inputLayout: BNNS.SparseLayout, inputDenseShape: BNNSNDArrayDescriptor, inputValues: BNNSNDArrayDescriptor, output: inout BNNSNDArrayDescriptor, sparseParameters: BNNS.SparseParameters?, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](./fullyconnectedlayer/sparsify%28batchsize,inputlayout,inputdenseshape,inputvalues,output,sparseparameters,workspace,filterparameters%29.md)
  Converts a sparse tensor from a standardized sparse layout to a device-specific sparse layout that Fully Connected uses.
- [struct SparseParameters](./sparseparameters.md)
  A data structure that provides a hint to the sparsity function.
- [BNNS.SparsityType](./sparsitytype.md)
  Constants that specify patterns in the sparsity.
- [var BNNSSparsityTypeUnstructured: BNNSSparsityType](../bnnssparsitytypeunstructured.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sparselayout)*