# GKRandom

**Framework**: GameplayKit  
**Kind**: protocol

The common interface for all randomization classes in (or usable with) GameplayKit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKRandom
```

#### Overview

> ❗ **Important**:  The randomization services provided in GameplayKit are suitable for reliably creating deterministic, pseudorandom gameplay mechanics, but are not cryptographically robust. For cryptography, obfuscation, or cipher uses, use the Security framework, described in [`Cryptographic Services Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172).

GameplayKit randomization classes include the [`GKRandomSource`](gkrandomsource.md) and [`GKRandomDistribution`](gkrandomdistribution.md) classes and their subclasses. You use those classes to generate random behavior for gameplay mechanics, and use this protocol type directly when composing random sources to create more complex randomizers.

For more information on choosing and using randomizers in GameplayKit, read [`Randomization`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/RandomSources.html#//apple_ref/doc/uid/TP40015172-CH9) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Topics

### Generating Random Numbers
- [func nextInt() -> Int](gkrandom/nextint.md)
  Generates and returns a new random integer.
- [func nextInt(upperBound: Int) -> Int](gkrandom/nextint(upperbound:).md)
  Generates and returns a new random integer less than the specified limit.
- [func nextUniform() -> Float](gkrandom/nextuniform.md)
  Generates and returns a new random floating-point value.
- [func nextBool() -> Bool](gkrandom/nextbool.md)
  Generates and returns a new random Boolean value.

## Relationships

### Conforming Types
- [GKARC4RandomSource](gkarc4randomsource.md)
- [GKGaussianDistribution](gkgaussiandistribution.md)
- [GKLinearCongruentialRandomSource](gklinearcongruentialrandomsource.md)
- [GKMersenneTwisterRandomSource](gkmersennetwisterrandomsource.md)
- [GKRandomDistribution](gkrandomdistribution.md)
- [GKRandomSource](gkrandomsource.md)
- [GKShuffledDistribution](gkshuffleddistribution.md)

## See Also

- [class GKRandomSource](gkrandomsource.md)
  The superclass for all basic randomization classes in GameplayKit.
- [class GKARC4RandomSource](gkarc4randomsource.md)
  A basic random number generator implementing the ARC4 algorithm, which is suitable for most gameplay mechanics.
- [class GKLinearCongruentialRandomSource](gklinearcongruentialrandomsource.md)
  A basic random number generator implementing the linear congruential generator algorithm, which is faster but less random than the default random source.
- [class GKMersenneTwisterRandomSource](gkmersennetwisterrandomsource.md)
  A basic random number generator implementing the Mersenne Twister algorithm, which is more random, but slower than the default random source.
- [class GKRandomDistribution](gkrandomdistribution.md)
  A generator for random numbers that fall within a specific range and that exhibit a specific distribution over multiple samplings.
- [class GKGaussianDistribution](gkgaussiandistribution.md)
  A generator for random numbers that follow a  (also known as a ) across multiple samplings.
- [class GKShuffledDistribution](gkshuffleddistribution.md)
  A generator for random numbers that are uniformly distributed across many samplings, but where short sequences of similar values are unlikely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandom)*