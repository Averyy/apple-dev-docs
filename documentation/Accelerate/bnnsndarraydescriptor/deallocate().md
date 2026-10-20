# deallocate()

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Deallocates the memory block previously allocated to this n-dimensional array descriptor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

## Declaration

```swift
func deallocate()
```

## See Also

### Allocating and Deallocating Memory
- [static func allocate<C>(initializingFrom: C, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](./allocate%28initializingfrom,shape,batchsize%29.md)
  Returns a new n-dimensional array descriptor that’s initialized with a copy of the elements in the specified collection.
- [static func allocate<Scalar>(randomUniformUsing: BNNS.RandomGenerator, range: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor?](./allocate%28randomuniformusing,range,shape,batchsize%29-2rorb.md)
  Returns a new array descriptor that’s initialized with random integer values from the continuous uniform distribution.
- [static func allocate<Scalar>(randomUniformUsing: BNNS.RandomGenerator, range: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor?](./allocate%28randomuniformusing,range,shape,batchsize%29-761hg.md)
  Returns a new array descriptor that’s initialized with random floating-point values from the continuous uniform distribution.
- [static func allocate<Scalar>(randomIn: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](./allocate%28randomin,shape,batchsize%29-1697a.md)
  Returns a new n-dimensional array descriptor that’s initialized with random values within the specified range.
- [static func allocate<Scalar>(randomIn: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](./allocate%28randomin,shape,batchsize%29-5a2p2.md)
  Returns a new n-dimensional array descriptor that’s initialized with random values within the specified range.
- [static func allocate<Scalar, Generator>(randomIn: ClosedRange<Scalar>, using: inout Generator, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](./allocate%28randomin,using,shape,batchsize%29-5kbi8.md)
  Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.
- [static func allocate<Scalar, Generator>(randomIn: ClosedRange<Scalar>, using: inout Generator, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](./allocate%28randomin,using,shape,batchsize%29-3w6ig.md)
  Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.
- [static func allocate<T>(repeating: T, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](./allocate%28repeating,shape,batchsize%29.md)
  Returns a new n-dimensional array descriptor that’s initialized with a single, repeated scalar value.
- [static func allocateUninitialized(scalarType: any BNNSScalar.Type, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](./allocateuninitialized%28scalartype,shape,batchsize%29.md)
  Returns a new n-dimensional array descriptor that’s allocated with uninitialized memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/deallocate())*