# BNNSRandomGeneratorMethod

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that describe random number generation methods.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSRandomGeneratorMethod
```

```c
typedef enum { ... } BNNSRandomGeneratorMethod;
```

## Topics

### Random Number Generation Methods
- [init(UInt32)](./bnnsrandomgeneratormethod/init%28_%29.md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](./bnnsrandomgeneratormethod/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](./bnnsrandomgeneratormethod/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSRandomGeneratorMethodAES_CTR: BNNSRandomGeneratorMethod](./bnnsrandomgeneratormethodaes_ctr.md)
  A constant that specifes an implementation that’s based on the Advanced Encryption Standard (AES) hash of a counter.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Random number generation
- [class RandomGenerator](./bnns/randomgenerator.md)
  A random number generator.
- [func BNNSCreateRandomGenerator(BNNSRandomGeneratorMethod, UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?](./bnnscreaterandomgenerator%28_,_%29.md)
  Returns a new random number generator using an internally generated random seed.
- [func BNNSCreateRandomGeneratorWithSeed(BNNSRandomGeneratorMethod, UInt64, UnsafePointer<BNNSFilterParameters>?) -> BNNSRandomGenerator?](./bnnscreaterandomgeneratorwithseed%28_,_,_%29.md)
  Returns a new random number generator using the specified seed.
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
- [func BNNSDestroyRandomGenerator(BNNSRandomGenerator?)](./bnnsdestroyrandomgenerator%28_%29.md)
  Destroys a random number generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsrandomgeneratormethod)*