# BNNSRandomFillNormalFloat(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Fills the specified tensor with random floating-point values mapped to a normal distribution.

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
func BNNSRandomFillNormalFloat(_ generator: BNNSRandomGenerator?, _ desc: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ mean: Float, _ stddev: Float) -> Int32
```

```c
int BNNSRandomFillNormalFloat(BNNSRandomGenerator generator, BNNSNDArrayDescriptor *desc, float mean, float stddev);
```

## Discussion

Use this function to fill an array descriptor with random values mapped to a normal distribution.

If you use the same generator on multiple threads, note that this function serializes the generator through an internal lock. To eliminate this contention, use different generators for each thread.

The following code populates a descriptor with random floating-point values:

```swift
let width = 1024
let height = 1024

var descriptor = BNNSNDArrayDescriptor.allocateUninitialized(
    scalarType: Float.self,
    shape: .matrixRowMajor(width,
                           height))

let randomNumberGenerator = BNNSCreateRandomGenerator(
    BNNSRandomGeneratorMethodAES_CTR,
    nil)

BNNSRandomFillNormalFloat(randomNumberGenerator,
                          &descriptor,
                          0,
                          2)
```

The graph below shows the distribution of values in `descriptor`.

![A graph that shows a single line that follows a bell curve shape.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3950634@2x.png)

## Parameters

- `generator`: The random number generator.
- `desc`: The descriptor of the destination.
- `mean`: The mean of the distribution.
- `stddev`: The standard deviation of the distribution.

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsrandomfillnormalfloat(_:_:_:_:))*