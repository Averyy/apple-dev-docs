# init(lowestValue:highestValue:)

**Framework**: GameplayKit  
**Kind**: init

Creates a random distribution with the specified lower and upper bounds, using the Arc4 randomizer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(lowestValue lowestInclusive: Int, highestValue highestInclusive: Int)
```

#### Return Value

A new random distribution.

#### Discussion

Creating a random source with this method is equivalent to calling the [`init(randomSource:lowestValue:highestValue:)`](gkrandomdistribution/init(randomsource:lowestvalue:highestvalue:).md) initializer and passing a new instance of the [`GKARC4RandomSource`](gkarc4randomsource.md) class for the `source` parameter. Because the newly created distribution uses its own [`GKRandomSource`](gkrandomsource.md) instance, the random behavior of the distribution is independent from that of other randomizers.

## Parameters

- `lowestInclusive`: The lowest value to be produced by the distribution.
- `highestInclusive`: The highest value to be produced by the distribution.

## See Also

- [init(randomSource: any GKRandom, lowestValue: Int, highestValue: Int)](gkrandomdistribution/init(randomsource:lowestvalue:highestvalue:).md)
  Initializes a uniform random distribution with the specified lower and upper bounds, using the specified source randomizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/init(lowestvalue:highestvalue:))*