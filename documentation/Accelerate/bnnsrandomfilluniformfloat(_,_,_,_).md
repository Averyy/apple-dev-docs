# BNNSRandomFillUniformFloat(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Fills the specified tensor with random floating-point values from the continuous uniform distribution within a range.

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
func BNNSRandomFillUniformFloat(_ generator: BNNSRandomGenerator?, _ desc: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ a: Float, _ b: Float) -> Int32
```

```c
int BNNSRandomFillUniformFloat(BNNSRandomGenerator generator, BNNSNDArrayDescriptor *desc, float a, float b);
```

## Discussion

Use this function to fill an array descriptor with uniformly distributed random values.

If you use the same generator on multiple threads, note that this function serializes the generator through an internal lock. To eliminate this contention, use different generators for each thread.

If the descriptor’s [`data_type`](./bnnsndarraydescriptor/data_type.md) isn’t 32-bit floating point, the values that you specify for the bounds must be exactly representable in the descriptor’s data type.

The following code populates a descriptor with random floating-point values:

```swift
let data = UnsafeMutableBufferPointer<Float>.allocate(capacity: 8)
var descriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                       layout: BNNSDataLayoutVector,
                                       size: (10, 0, 0, 0, 0, 0, 0, 0),
                                       stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                       data: data.baseAddress!,
                                       data_type: BNNSDataType.float,
                                       table_data: nil,
                                       table_data_type: BNNSDataType.float,
                                       data_scale: 1, data_bias: 0)

guard let randomNumberGenerator = BNNSCreateRandomGenerator(BNNSRandomGeneratorMethodAES_CTR,
                                                            nil) else {
    return
}

BNNSRandomFillUniformFloat(randomNumberGenerator,
                           &descriptor,
                           -10,
                           10)

print(Array(data))

data.deallocate()
BNNSDestroyRandomGenerator(randomNumberGenerator)
```

## Parameters

- `generator`: The random number generator.
- `desc`: The descriptor of the destination.
- `a`: The lower bound of distribution.
- `b`: The upper bound of distribution.

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsrandomfilluniformfloat(_:_:_:_:))*