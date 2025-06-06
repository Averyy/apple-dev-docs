# BNNSCreateRandomGeneratorWithSeed(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new random number generator using the specified seed.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func BNNSCreateRandomGeneratorWithSeed(_ method: BNNSRandomGeneratorMethod, _ seed: UInt64, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?
```

#### Return Value

A pointer to the random generator.

## Parameters

- `method`: The method that the generator uses to generate random numbers.
- `seed`: The random seed that this function uses to initialize the generator.
- `filter_params`: The filter runtime parameters.

## See Also

- [class RandomGenerator](bnns/randomgenerator.md)
  A random number generator.
- [func BNNSCreateRandomGenerator(BNNSRandomGeneratorMethod, UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?](bnnscreaterandomgenerator(_:_:).md)
  Returns a new random number generator using an internally generated random seed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnscreaterandomgeneratorwithseed(_:_:_:))*