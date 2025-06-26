# BNNS.SparseParameters

**Framework**: Accelerate  
**Kind**: struct

A data structure that provides a hint to the sparsity function.

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
struct SparseParameters
```

## Topics

### Creating a Sparse Parameters Structure
- [init(type: BNNS.SparsityType, ratio: (numerator: UInt32, denominator: UInt32), targetSystem: BNNSTargetSystem)](bnns/sparseparameters/init(type:ratio:targetsystem:).md)
  Returns a new sparse parameters structure.
### Inspecting the Properties of a Sparse Parameters Structure
- [let ratio: (numerator: UInt32, denominator: UInt32)](bnns/sparseparameters/ratio.md)
  The sparsity ratio expressed as the numerator and the denominator.
- [let targetSystem: BNNSTargetSystem](bnns/sparseparameters/targetsystem.md)
  The target system.
- [let type: BNNS.SparsityType](bnns/sparseparameters/type.md)
  An enumeration that specifies special patterns, if any, in the sparsity.

## See Also

- [func BNNSNDArrayGetDataSize(UnsafePointer<BNNSNDArrayDescriptor>) -> Int](bnnsndarraygetdatasize(_:).md)
  Returns the size, in bytes, that an array descriptor requires.
- [func BNNSNDArrayFullyConnectedSparsifySparseCOO(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsndarrayfullyconnectedsparsifysparsecoo(_:_:_:_:_:_:_:_:_:).md)
  Converts a sparse tensor from the standardized coordinate list (COO) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [func BNNSNDArrayFullyConnectedSparsifySparseCSR(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsndarrayfullyconnectedsparsifysparsecsr(_:_:_:_:_:_:_:_:_:_:).md)
  Converts a sparse tensor from the standardized compressed sparse row (CSR) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [static func sparsify(batchSize: Int, inputLayout: BNNS.SparseLayout, inputDenseShape: BNNSNDArrayDescriptor, inputValues: BNNSNDArrayDescriptor, output: inout BNNSNDArrayDescriptor, sparseParameters: BNNS.SparseParameters?, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](bnns/fullyconnectedlayer/sparsify(batchsize:inputlayout:inputdenseshape:inputvalues:output:sparseparameters:workspace:filterparameters:).md)
  Converts a sparse tensor from a standardized sparse layout to a device-specific sparse layout that Fully Connected uses.
- [BNNS.SparseLayout](bnns/sparselayout.md)
  Constants that specify standardized sparse layouts that BNNS can convert to opaque.
- [BNNS.SparsityType](bnns/sparsitytype.md)
  Constants that specify patterns in the sparsity.
- [var BNNSSparsityTypeUnstructured: BNNSSparsityType](bnnssparsitytypeunstructured.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sparseparameters)*