# BNNSDestroyRandomGenerator(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Destroys a random number generator.

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
func BNNSDestroyRandomGenerator(_ generator: BNNSRandomGenerator?)
```

```c
void BNNSDestroyRandomGenerator(BNNSRandomGenerator generator);
```

## Parameters

- `generator`: The random number generator.

## See Also

### Random number generation
- [class RandomGenerator](./bnns/randomgenerator.md)
  A random number generator.
- [func BNNSCreateRandomGenerator(BNNSRandomGeneratorMethod, UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?](./bnnscreaterandomgenerator%28_,_%29.md)
  Returns a new random number generator using an internally generated random seed.
- [func BNNSCreateRandomGeneratorWithSeed(BNNSRandomGeneratorMethod, UInt64, UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?](./bnnscreaterandomgeneratorwithseed%28_,_,_%29.md)
  Returns a new random number generator using the specified seed.
- [struct BNNSRandomGeneratorMethod](./bnnsrandomgeneratormethod.md)
  Constants that describe random number generation methods.
- [typealias BNNSRandomGenerator](./bnnsrandomgenerator.md)
  A pointer to a random number generator object.
- [func BNNSRandomFillUniformInt(BNNSRandomGenerator?, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int64, Int64) -> Int32](./bnnsrandomfilluniformint%28_,_,_,_%29.md)
  Fills the specified tensor with random integer values from the continuous uniform distribution within a range.
- [func BNNSRandomFillUniformFloat(BNNSRandomGenerator?, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](./bnnsrandomfilluniformfloat%28_,_,_,_%29.md)
  Fills the specified tensor with random floating-point values from the continuous uniform distribution within a range.
- [func BNNSRandomFillNormalFloat(BNNSRandomGenerator?, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Float, Float) -> Int32](./bnnsrandomfillnormalfloat%28_,_,_,_%29.md)
  Fills the specified tensor with random floating-point values mapped to a normal distribution.
- [func BNNSRandomFillCategoricalFloat(BNNSRandomGenerator?, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, Bool) -> Int32](./bnnsrandomfillcategoricalfloat%28_,_,_,_%29.md)
  Fills the specified tensor with random values from the categorical distributions with the given event probabilities.
- [func BNNSRandomGeneratorStateSize(BNNSRandomGenerator?) -> Int](./bnnsrandomgeneratorstatesize%28_%29.md)
  Returns the state size, in bytes, of a random number generator.
- [func BNNSRandomGeneratorGetState(BNNSRandomGenerator?, Int, UnsafeMutableRawPointer) -> Int32](./bnnsrandomgeneratorgetstate%28_,_,_%29.md)
  Returns the state of a random number generator.
- [func BNNSRandomGeneratorSetState(BNNSRandomGenerator?, Int, UnsafeMutableRawPointer) -> Int32](./bnnsrandomgeneratorsetstate%28_,_,_%29.md)
  Sets the state of a random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdestroyrandomgenerator(_:))*