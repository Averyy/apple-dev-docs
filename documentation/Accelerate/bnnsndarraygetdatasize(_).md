# BNNSNDArrayGetDataSize(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the size, in bytes, that an array descriptor requires.

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
func BNNSNDArrayGetDataSize(_ array: UnsafePointer<BNNSNDArrayDescriptor>) -> Int
```

```c
size_t BNNSNDArrayGetDataSize(const BNNSNDArrayDescriptor *array);
```

## Return Value

The size of the array descriptor.

## Discussion

Use this function to calcluate the size of the workspace that the [`BNNSNDArrayFullyConnectedSparsifySparseCOO(_:_:_:_:_:_:_:_:_:)`](./bnnsndarrayfullyconnectedsparsifysparsecoo%28_,_,_,_,_,_,_,_,_%29.md) and [`BNNSNDArrayFullyConnectedSparsifySparseCSR(_:_:_:_:_:_:_:_:_:_:)`](./bnnsndarrayfullyconnectedsparsifysparsecsr%28_,_,_,_,_,_,_,_,_,_%29.md) require.

## Parameters

- `array`: The array descriptor.

## See Also

### Sparse layers
- [func BNNSNDArrayFullyConnectedSparsifySparseCOO(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsndarrayfullyconnectedsparsifysparsecoo%28_,_,_,_,_,_,_,_,_%29.md)
  Converts a sparse tensor from the standardized coordinate list (COO) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [func BNNSNDArrayFullyConnectedSparsifySparseCSR(UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutablePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSSparsityParameters>?, Int, UnsafeMutableRawPointer?, Int, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsndarrayfullyconnectedsparsifysparsecsr%28_,_,_,_,_,_,_,_,_,_%29.md)
  Converts a sparse tensor from the standardized compressed sparse row (CSR) layout to a device-specific sparse layout that BNNS fully connected layers use.
- [static func sparsify(batchSize: Int, inputLayout: BNNS.SparseLayout, inputDenseShape: BNNSNDArrayDescriptor, inputValues: BNNSNDArrayDescriptor, output: inout BNNSNDArrayDescriptor, sparseParameters: BNNS.SparseParameters?, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](./bnns/fullyconnectedlayer/sparsify%28batchsize,inputlayout,inputdenseshape,inputvalues,output,sparseparameters,workspace,filterparameters%29.md)
  Converts a sparse tensor from a standardized sparse layout to a device-specific sparse layout that Fully Connected uses.
- [struct SparseParameters](./bnns/sparseparameters.md)
  A data structure that provides a hint to the sparsity function.
- [BNNS.SparseLayout](./bnns/sparselayout.md)
  Constants that specify standardized sparse layouts that BNNS can convert to opaque.
- [BNNS.SparsityType](./bnns/sparsitytype.md)
  Constants that specify patterns in the sparsity.
- [var BNNSSparsityTypeUnstructured: BNNSSparsityType](./bnnssparsitytypeunstructured.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraygetdatasize(_:))*