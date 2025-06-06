# nextInt()

**Framework**: GameplayKit  
**Kind**: method

Generates and returns a new random integer within the bounds of the distribution.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nextInt() -> Int
```

#### Return Value

An integer in the range specified by the distribution’s [`lowestValue`](gkrandomdistribution/lowestvalue.md) and [`highestValue`](gkrandomdistribution/highestvalue.md) properties (inclusive).

#### Discussion

When using the [`GKRandomDistribution`](gkrandomdistribution.md) directly, generated numbers are uniform within this range. Subclasses of [`GKRandomDistribution`](gkrandomdistribution.md) can alter the relative probability of generating any particular number within the distribution’s range.

## See Also

- [func nextInt(upperBound: Int) -> Int](gkrandomdistribution/nextint(upperbound:).md)
  Generates and returns a new random integer within the bounds of the distribution and less than the specified limit.
- [func nextUniform() -> Float](gkrandomdistribution/nextuniform.md)
  Generates and returns a new random floating-point value within the characteristics of the distribution.
- [func nextBool() -> Bool](gkrandomdistribution/nextbool.md)
  Generates and returns a new random Boolean value within the characteristics of the distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/nextint())*