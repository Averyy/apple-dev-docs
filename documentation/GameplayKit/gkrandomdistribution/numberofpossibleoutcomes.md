# numberOfPossibleOutcomes

**Framework**: GameplayKit  
**Kind**: property

The number of unique values the distribution can generate.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var numberOfPossibleOutcomes: Int { get }
```

#### Discussion

When using the [`GKRandomDistribution`](gkrandomdistribution.md) directly, this property is determined by the [`lowestValue`](gkrandomdistribution/lowestvalue.md) and [`highestValue`](gkrandomdistribution/highestvalue.md) properties according to the formula `number = highest - lowest + 1`. For example, in a distribution whose lowest value is 1 and highest value is 4, the [`nextInt()`](gkrandomdistribution/nextint().md) method can return `1`, `2`, `3`, or `4`, and the [`nextUniform()`](gkrandomdistribution/nextuniform().md) method can return `0.25`, `0.5`, `0.75`, or `1.0`, so the number of possible outcomes is 4.

Subclasses of [`GKRandomDistribution`](gkrandomdistribution.md) can alter the number of unique possible outcomes.

## See Also

- [var lowestValue: Int](gkrandomdistribution/lowestvalue.md)
  The lowest value to be produced by the distribution.
- [var highestValue: Int](gkrandomdistribution/highestvalue.md)
  The highest value to be produced by the distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/numberofpossibleoutcomes)*