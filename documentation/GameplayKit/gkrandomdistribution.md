# GKRandomDistribution

**Framework**: GameplayKit  
**Kind**: class

A generator for random numbers that fall within a specific range and that exhibit a specific distribution over multiple samplings.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKRandomDistribution
```

#### Overview

> ❗ **Important**:  The randomization services provided in GameplayKit are suitable for reliably creating deterministic, pseudorandom gameplay mechanics, but are not cryptographically robust. For cryptography, obfuscation, or cipher uses, use the Security framework, described in [`Cryptographic Services Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172).

 The randomization services provided in GameplayKit are suitable for reliably creating deterministic, pseudorandom gameplay mechanics, but are not cryptographically robust. For cryptography, obfuscation, or cipher uses, use the Security framework, described in [`Cryptographic Services Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172).

You choose the algorithm that randomizes source values for a distribution by initializing it with an instance of any class that implements the [`GKRandom`](gkrandom.md) protocol, such as a basic random source (a subclass of [`GKRandomSource`](gkrandomsource.md)) or another random distribution. The [`GKRandomDistribution`](gkrandomdistribution.md) class itself implements a uniform distribution—for more specialized distributions use one of the subclasses [`GKGaussianDistribution`](gkgaussiandistribution.md) and [`GKShuffledDistribution`](gkshuffleddistribution.md).

In a  distribution, the probability of generating any number in a specified range (between the values of the distribution’s [`lowestValue`](gkrandomdistribution/lowestvalue.md) and [`highestValue`](gkrandomdistribution/highestvalue.md) properties) is approximately equal. In other words, there is no bias toward any possible outcome. To generate random numbers in this range, use the methods from the [`GKRandom`](gkrandom.md) protocol listed in Generating Random Numbers below.

For more information on choosing and using randomizers in GameplayKit, read [`Randomization`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/RandomSources.html#//apple_ref/doc/uid/TP40015172-CH9) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Creating a Random Distribution
- [init(randomSource: any GKRandom, lowestValue: Int, highestValue: Int)](gkrandomdistribution/init(randomsource:lowestvalue:highestvalue:).md)
  Initializes a uniform random distribution with the specified lower and upper bounds, using the specified source randomizer.
- [convenience init(lowestValue: Int, highestValue: Int)](gkrandomdistribution/init(lowestvalue:highestvalue:).md)
  Creates a random distribution with the specified lower and upper bounds, using the Arc4 randomizer.
### Creating Specific Random Distributions
- [class func d6() -> Self](gkrandomdistribution/d6.md)
  Creates a random distribution equivalent to a six-sided die.
- [class func d20() -> Self](gkrandomdistribution/d20.md)
  Creates a random distribution equivalent to a twenty-sided die.
- [convenience init(forDieWithSideCount: Int)](gkrandomdistribution/init(fordiewithsidecount:).md)
  Creates a random distribution equivalent to a die with the specified number of sides.
### Generating Random Numbers
- [func nextInt() -> Int](gkrandomdistribution/nextint.md)
  Generates and returns a new random integer within the bounds of the distribution.
- [func nextInt(upperBound: Int) -> Int](gkrandomdistribution/nextint(upperbound:).md)
  Generates and returns a new random integer within the bounds of the distribution and less than the specified limit.
- [func nextUniform() -> Float](gkrandomdistribution/nextuniform.md)
  Generates and returns a new random floating-point value within the characteristics of the distribution.
- [func nextBool() -> Bool](gkrandomdistribution/nextbool.md)
  Generates and returns a new random Boolean value within the characteristics of the distribution.
### Working with Characteristics of a Distribution
- [var lowestValue: Int](gkrandomdistribution/lowestvalue.md)
  The lowest value to be produced by the distribution.
- [var highestValue: Int](gkrandomdistribution/highestvalue.md)
  The highest value to be produced by the distribution.
- [var numberOfPossibleOutcomes: Int](gkrandomdistribution/numberofpossibleoutcomes.md)
  The number of unique values the distribution can generate.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [GKGaussianDistribution](gkgaussiandistribution.md)
- [GKShuffledDistribution](gkshuffleddistribution.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GKRandom](gkrandom.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol GKRandom](gkrandom.md)
  The common interface for all randomization classes in (or usable with) GameplayKit.
- [class GKRandomSource](gkrandomsource.md)
  The superclass for all basic randomization classes in GameplayKit.
- [class GKARC4RandomSource](gkarc4randomsource.md)
  A basic random number generator implementing the ARC4 algorithm, which is suitable for most gameplay mechanics.
- [class GKLinearCongruentialRandomSource](gklinearcongruentialrandomsource.md)
  A basic random number generator implementing the linear congruential generator algorithm, which is faster but less random than the default random source.
- [class GKMersenneTwisterRandomSource](gkmersennetwisterrandomsource.md)
  A basic random number generator implementing the Mersenne Twister algorithm, which is more random, but slower than the default random source.
- [class GKGaussianDistribution](gkgaussiandistribution.md)
  A generator for random numbers that follow a  (also known as a ) across multiple samplings.
- [class GKShuffledDistribution](gkshuffleddistribution.md)
  A generator for random numbers that are uniformly distributed across many samplings, but where short sequences of similar values are unlikely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution)*