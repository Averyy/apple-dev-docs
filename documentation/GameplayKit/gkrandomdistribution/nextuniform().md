# nextUniform()

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Generates and returns a new random floating-point value within the characteristics of the distribution.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nextUniform() -> Float
```

```objc
- (float) nextUniform;
```

## Return Value

A random floating-point value within the range `[delta, 1.0]`, where `delta` is the ratio of the [`lowestValue`](./lowestvalue.md) and [`highestValue`](./highestvalue.md) properties.

## Discussion

When using the [`GKRandomDistribution`](../gkrandomdistribution.md) class directly, generated numbers are uniform within the range of the distribution. For example, in a distribution whose lowest value is `1` and highest is `20` (as produced by the [`d20()`](./d20%28%29.md) class method), `delta` is `1/20 = 0.05`; that is, the distribution returns numbers in 5% increments. Subclasses of [`GKRandomDistribution`](../gkrandomdistribution.md) can alter this quantization, as well as relative probability of generating any particular number within the distribution’s range.

## See Also

### Generating Random Numbers
- [func nextInt() -> Int](./nextint%28%29.md)
  Generates and returns a new random integer within the bounds of the distribution.
- [func nextInt(upperBound: Int) -> Int](./nextint%28upperbound%29.md)
  Generates and returns a new random integer within the bounds of the distribution and less than the specified limit.
- [func nextBool() -> Bool](./nextbool%28%29.md)
  Generates and returns a new random Boolean value within the characteristics of the distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/nextuniform())*