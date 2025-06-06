# allocate(randomIn:using:shape:batchSize:)

**Framework**: Accelerate  
**Kind**: method

Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
static func allocate<Scalar, Generator>(randomIn range: ClosedRange<Scalar>, using generator: inout Generator, shape: BNNS.Shape, batchSize: Int = 1) -> BNNSNDArrayDescriptor where Scalar : BNNSScalar, Scalar : FixedWidthInteger, Generator : RandomNumberGenerator
```

## Parameters

- `range`: The range in which to create random values.
- `generator`: The random number generator to use when creating the new random values.
- `shape`: The shape of n-dimensional array descriptor.
- `batchSize`: The number of batches of data.

## See Also

- [static func allocate<C>(initializingFrom: C, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(initializingfrom:shape:batchsize:).md)
  Returns a new n-dimensional array descriptor that’s initialized with a copy of the elements in the specified collection.
- [static func allocate<Scalar>(randomUniformUsing: BNNS.RandomGenerator, range: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor?](bnnsndarraydescriptor/allocate(randomuniformusing:range:shape:batchsize:)-2rorb.md)
  Returns a new array descriptor that’s initialized with random integer values from the continuous uniform distribution.
- [static func allocate<Scalar>(randomUniformUsing: BNNS.RandomGenerator, range: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor?](bnnsndarraydescriptor/allocate(randomuniformusing:range:shape:batchsize:)-761hg.md)
  Returns a new array descriptor that’s initialized with random floating-point values from the continuous uniform distribution.
- [static func allocate<Scalar>(randomIn: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:shape:batchsize:)-1697a.md)
  Returns a new n-dimensional array descriptor that’s initialized with random values within the specified range.
- [static func allocate<Scalar>(randomIn: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:shape:batchsize:)-5a2p2.md)
  Returns a new n-dimensional array descriptor that’s initialized with random values within the specified range.
- [static func allocate<Scalar, Generator>(randomIn: ClosedRange<Scalar>, using: inout Generator, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:using:shape:batchsize:)-5kbi8.md)
  Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.
- [static func allocate<T>(repeating: T, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(repeating:shape:batchsize:).md)
  Returns a new n-dimensional array descriptor that’s initialized with a single, repeated scalar value.
- [static func allocateUninitialized(scalarType: any BNNSScalar.Type, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocateuninitialized(scalartype:shape:batchsize:).md)
  Returns a new n-dimensional array descriptor that’s allocated with uninitialized memory.
- [func deallocate()](bnnsndarraydescriptor/deallocate.md)
  Deallocates the memory block previously allocated to this n-dimensional array descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/allocate(randomin:using:shape:batchsize:)-3w6ig)*