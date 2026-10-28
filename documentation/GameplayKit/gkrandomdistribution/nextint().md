# nextInt()

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSInteger) nextInt;
```

## Return Value

An integer in the range specified by the distribution’s [`lowestValue`](./lowestvalue.md) and [`highestValue`](./highestvalue.md) properties (inclusive).

## Discussion

When using the [`GKRandomDistribution`](../gkrandomdistribution.md) directly, generated numbers are uniform within this range. Subclasses of [`GKRandomDistribution`](../gkrandomdistribution.md) can alter the relative probability of generating any particular number within the distribution’s range.

## See Also

### Generating Random Numbers
- [func nextInt(upperBound: Int) -> Int](./nextint%28upperbound%29.md)
  Generates and returns a new random integer within the bounds of the distribution and less than the specified limit.
- [func nextUniform() -> Float](./nextuniform%28%29.md)
  Generates and returns a new random floating-point value within the characteristics of the distribution.
- [func nextBool() -> Bool](./nextbool%28%29.md)
  Generates and returns a new random Boolean value within the characteristics of the distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/nextint())*