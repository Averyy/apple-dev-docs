# init(randomSource:mean:deviation:)

**Framework**: GameplayKit  
**Kind**: init

Initializes a Gaussian random distribution with the specified mean and deviation, using the specified source randomizer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(randomSource source: any GKRandom, mean: Float, deviation: Float)
```

#### Return Value

A new random distribution.

#### Discussion

Using this initializer creates a Gaussian distribution whose range is determined by the specified `mean` and `deviation` values. The [`lowestValue`](gkrandomdistribution/lowestvalue.md) property of the newly created distribution is set to three deviations below the mean (`lowest = mean - 3 * deviation`) and the [`highestValue`](gkrandomdistribution/highestvalue.md) property is set to three deviations above the mean (`highest = mean + 3 * deviation`).

A random distribution works by mapping the values produced by the `source` randomizer to the range and characteristics specified by the distribution. Multiple distributions can share the same source, with the side effect that retrieving a random value through one distribution affects the sequence of random numbers produced by the source.

## Parameters

- `source`: A randomizer that produces raw random values for use by the distribution. A randomizer is any object implementing the   protocol, which can be a random source algorithm such as the   class or another random distribution.
- `mean`: The mean value of the distribution (also called the   or  ).
- `deviation`: The standard deviation of the distribution (also called  ).

## See Also

- [init(randomSource: any GKRandom, lowestValue: Int, highestValue: Int)](gkgaussiandistribution/init(randomsource:lowestvalue:highestvalue:).md)
  Initializes a Gaussian random distribution with the specified lower and upper bounds, using the specified source randomizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkgaussiandistribution/init(randomsource:mean:deviation:))*