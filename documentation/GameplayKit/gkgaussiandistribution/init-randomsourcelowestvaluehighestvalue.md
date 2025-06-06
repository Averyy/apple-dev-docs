# init(randomSource:lowestValue:highestValue:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a Gaussian random distribution with the specified lower and upper bounds, using the specified source randomizer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(randomSource source: any GKRandom, lowestValue lowestInclusive: Int, highestValue highestInclusive: Int)
```

#### Return Value

A new random distribution.

#### Discussion

Using this initializer creates a Gaussian distribution centered within the specified range. The [`mean`](gkgaussiandistribution/mean.md) property is set to the midpoint between the `lowestInclusive` and `highestInclusive` parameters (`mean = (highest + lowest) / 2`), and the [`deviation`](gkgaussiandistribution/deviation.md) property is set such that the highest and lowest values are each three deviations away from the mean (`deviation = (highest - lowest) / 6`). The [`mean`](gkgaussiandistribution/mean.md) and [`deviation`](gkgaussiandistribution/deviation.md) properties can thus be floating-point values even if you use the distribution only to produce integers.

A random distribution works by mapping the values produced by the `source` randomizer to the range and characteristics specified by the distribution. Multiple distributions can share the same source, with the side effect that retrieving a random value through one distribution affects the sequence of random numbers produced by the source.

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## Parameters

- `source`: A randomizer that produces raw random values for use by the distribution. A randomizer is any object implementing the   protocol, which can be a random source algorithm such as the   class or another random distribution.
- `lowestInclusive`: The lowest value to be produced by the distribution.
- `highestInclusive`: The highest value to be produced by the distribution.

## See Also

- [init(randomSource: any GKRandom, mean: Float, deviation: Float)](gkgaussiandistribution/init(randomsource:mean:deviation:).md)
  Initializes a Gaussian random distribution with the specified mean and deviation, using the specified source randomizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgaussiandistribution/init(randomsource:lowestvalue:highestvalue:))*