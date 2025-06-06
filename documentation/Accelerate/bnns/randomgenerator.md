# BNNS.RandomGenerator

**Framework**: Accelerate  
**Kind**: class

A random number generator.

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
class RandomGenerator
```

## Topics

### Creating a Random Number Generator
- [init?(method: BNNS.RandomGeneratorMethod, seed: UInt64?, filterParameters: BNNSFilterParameters?)](bnns/randomgenerator/init(method:seed:filterparameters:).md)
  Returns a new random number generator.
- [BNNS.RandomGeneratorMethod](bnns/randomgeneratormethod.md)
  Constants that describe random number generation methods.
### Saving and Restoring a Randon Generator’s State
- [var state: BNNS.RandomGeneratorState](bnns/randomgenerator/state.md)
  The state of the random number generator.
- [class RandomGeneratorState](bnns/randomgeneratorstate.md)
  An opaque object that contains the state of a random number generator.

## See Also

- [static func allocate<Scalar, Generator>(randomIn: ClosedRange<Scalar>, using: inout Generator, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:using:shape:batchsize:)-3w6ig.md)
  Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.
- [static func allocate<Scalar, Generator>(randomIn: ClosedRange<Scalar>, using: inout Generator, shape: BNNS.Shape, batchSize: Int) -> BNNSNDArrayDescriptor](bnnsndarraydescriptor/allocate(randomin:using:shape:batchsize:)-5kbi8.md)
  Returns a new array descriptor that’s initialized with random values within the specified range, using the given generator as a source for randomness.
- [func BNNSCreateRandomGenerator(BNNSRandomGeneratorMethod, UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?](bnnscreaterandomgenerator(_:_:).md)
  Returns a new random number generator using an internally generated random seed.
- [func BNNSCreateRandomGeneratorWithSeed(BNNSRandomGeneratorMethod, UInt64, UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?](bnnscreaterandomgeneratorwithseed(_:_:_:).md)
  Returns a new random number generator using the specified seed.
- [struct BNNSRandomGeneratorMethod](bnnsrandomgeneratormethod.md)
  Constants that describe random number generation methods.
- [typealias BNNSRandomGenerator](bnnsrandomgenerator.md)
  A pointer to a random number generator object.
- [func BNNSRandomFillUniformInt(BNNSRandomGenerator?, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int64, Int64) -> Int32](bnnsrandomfilluniformint(_:_:_:_:).md)
  Fills the specified tensor with random integer values from the continuous uniform distribution within a range.
- [func BNNSRandomFillUniformFloat(BNNSRandomGenerator?, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](bnnsrandomfilluniformfloat(_:_:_:_:).md)
  Fills the specified tensor with random floating-point values from the continuous uniform distribution within a range.
- [func BNNSRandomFillNormalFloat(BNNSRandomGenerator?, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](bnnsrandomfillnormalfloat(_:_:_:_:).md)
  Fills the specified tensor with random floating-point values mapped to a normal distribution.
- [func BNNSRandomFillCategoricalFloat(BNNSRandomGenerator?, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Bool) -> Int32](bnnsrandomfillcategoricalfloat(_:_:_:_:).md)
  Fills the specified tensor with random values from the categorical distributions with the given event probabilities.
- [func BNNSRandomGeneratorStateSize(BNNSRandomGenerator?) -> Int](bnnsrandomgeneratorstatesize(_:).md)
  Returns the state size, in bytes, of a random number generator.
- [func BNNSRandomGeneratorGetState(BNNSRandomGenerator?, Int, UnsafeMutableRawPointer) -> Int32](bnnsrandomgeneratorgetstate(_:_:_:).md)
  Returns the state of a random number generator.
- [func BNNSRandomGeneratorSetState(BNNSRandomGenerator?, Int, UnsafeMutableRawPointer) -> Int32](bnnsrandomgeneratorsetstate(_:_:_:).md)
  Sets the state of a random number generator.
- [func BNNSDestroyRandomGenerator(BNNSRandomGenerator?)](bnnsdestroyrandomgenerator(_:).md)
  Destroys a random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/randomgenerator)*