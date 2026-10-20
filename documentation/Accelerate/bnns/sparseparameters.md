# BNNS.SparseParameters

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A data structure that provides a hint to the sparsity function.

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
struct SparseParameters
```

## Topics

### Creating a Sparse Parameters Structure
- [init(type: BNNS.SparsityType, ratio: (numerator: UInt32, denominator: UInt32), targetSystem: BNNSTargetSystem)](./sparseparameters/init%28type,ratio,targetsystem%29.md)
  Returns a new sparse parameters structure.
### Inspecting the Properties of a Sparse Parameters Structure
- [let ratio: (numerator: UInt32, denominator: UInt32)](./sparseparameters/ratio.md)
  The sparsity ratio expressed as the numerator and the denominator.
- [let targetSystem: BNNSTargetSystem](./sparseparameters/targetsystem.md)
  The target system.
- [let type: BNNS.SparsityType](./sparseparameters/type.md)
  An enumeration that specifies special patterns, if any, in the sparsity.

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
- [BNNS.SparseLayout](./sparselayout.md)
  Constants that specify standardized sparse layouts that BNNS can convert to opaque.
- [BNNS.SparsityType](./sparsitytype.md)
  Constants that specify patterns in the sparsity.
- [var BNNSSparsityTypeUnstructured: BNNSSparsityType](../bnnssparsitytypeunstructured.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sparseparameters)*