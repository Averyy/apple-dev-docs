# GKShuffledDistribution

**Framework**: GameplayKit  
**Kind**: class

A generator for random numbers that are uniformly distributed across many samplings, but where short sequences of similar values are unlikely.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKShuffledDistribution
```

#### Overview

The behavior of a shuffled distribution is sometimes called “fair” randomization, because true randomness in games can result in extended “lucky streaks” or “unlucky streaks” for players. To create a shuffled distribution and use it to generate random numbers, use the methods defined by its superclass [`GKRandomDistribution`](gkrandomdistribution.md).

The [`GKShuffledDistribution`](gkshuffleddistribution.md) class inherits its entire interface from its superclass—to initialize and use a shuffled distribution, use the methods listed in [`GKRandomDistribution`](gkrandomdistribution.md). A shuffled distribution differs from its superclass in behavior only. Consider the code snippets below:

In this example, each distribution generates 100 random integers from a simulated six-sided die. In both cases, the distribution of results is roughly uniform—that is, the number of occurrences of any specific value is about the same as that of any other value. However, the shuffled distribution makes sure not to repeat any one value until it has used all of its possible values. In this example, if the die rolls a 1, the shuffled distribution will not generate another 1 for at least five more rolls.

> ❗ **Important**:  The randomization services provided in GameplayKit are suitable for reliably creating deterministic, pseudorandom gameplay mechanics, but are not cryptographically robust. For cryptography, obfuscation, or cipher uses, use the Security framework, described in [`Cryptographic Services Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172).

For more information on choosing and using randomizers in GameplayKit, read [`Randomization`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/RandomSources.html#//apple_ref/doc/uid/TP40015172-CH9) in [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Relationships

### Inherits From
- [GKRandomDistribution](gkrandomdistribution.md)
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
- [class GKRandomDistribution](gkrandomdistribution.md)
  A generator for random numbers that fall within a specific range and that exhibit a specific distribution over multiple samplings.
- [class GKGaussianDistribution](gkgaussiandistribution.md)
  A generator for random numbers that follow a  (also known as a ) across multiple samplings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkshuffleddistribution)*