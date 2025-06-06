# allocate(randomUniformUsing:range:shape:batchSize:)

**Framework**: Accelerate  
**Kind**: method

Returns a new array descriptor that’s initialized with random integer values from the continuous uniform distribution.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
static func allocate<Scalar>(randomUniformUsing: BNNS.RandomGenerator, range: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int = 1) -> BNNSNDArrayDescriptor? where Scalar : BNNSScalar, Scalar : BinaryFloatingPoint
```

#### Discussion

Use this function to create a new array descriptor that’s initialized with random values [`BNNS.RandomGenerator`](bnns/randomgenerator.md) generates.

If you use the same generator on multiple threads, note that this function serializes the generator through an internal lock. To eliminate this contention, use different generators for each thread.

The following code creates a 16-element 1D tensor that contains random 16-bit integer values between `-10` and `10`:

```swift
guard
    let randomGenerator = BNNS.RandomGenerator(
        method: .aesCtr,
        seed: 1234),
    let descriptor = BNNSNDArrayDescriptor.allocate(
        randomUniformUsing: randomGenerator,
        range: Int16(-10)...Int16(10),
        shape: [16]) else {
        return
    }

// Prints 16 random values.
print(descriptor.makeArray(of: Int16.self)!)

descriptor.deallocate()
```

## Parameters

- `randomUniformUsing`: The random number generator that provides random values.
- `range`: The range of random values.
- `shape`: The shape of the n-dimensional array descriptor.
- `batchSize`: The number of batches of data.

## See Also

- [static func allocate<C>(initializingFrom: C, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(initializingfrom:shape:batchsize:).md)
  Returns a new n-dimensional array descriptor that’s initialized with a copy of the elements in the specified collection.
- [static func allocate<Scalar>(randomUniformUsing: BNNS.RandomGenerator, range: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor?](bnnsndarraydescriptor/allocate(randomuniformusing:range:shape:batchsize:)-761hg.md)
  Returns a new array descriptor that’s initialized with random floating-point values from the continuous uniform distribution.
- [static func allocate<Scalar>(randomIn: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:shape:batchsize:)-1697a.md)
  Returns a new n-dimensional array descriptor that’s initialized with random values within the specified range.
- [static func allocate<Scalar>(randomIn: ClosedRange<Scalar>, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:shape:batchsize:)-5a2p2.md)
  Returns a new n-dimensional array descriptor that’s initialized with random values within the specified range.
- [static func allocate<Scalar, Generator>(randomIn: ClosedRange<Scalar>, using: inout Generator, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:using:shape:batchsize:)-5kbi8.md)
  Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.
- [static func allocate<Scalar, Generator>(randomIn: ClosedRange<Scalar>, using: inout Generator, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:using:shape:batchsize:)-3w6ig.md)
  Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.
- [static func allocate<T>(repeating: T, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(repeating:shape:batchsize:).md)
  Returns a new n-dimensional array descriptor that’s initialized with a single, repeated scalar value.
- [static func allocateUninitialized(scalarType: any BNNSScalar.Type, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocateuninitialized(scalartype:shape:batchsize:).md)
  Returns a new n-dimensional array descriptor that’s allocated with uninitialized memory.
- [func deallocate()](bnnsndarraydescriptor/deallocate.md)
  Deallocates the memory block previously allocated to this n-dimensional array descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsndarraydescriptor/allocate(randomuniformusing:range:shape:batchsize:)-2rorb)*