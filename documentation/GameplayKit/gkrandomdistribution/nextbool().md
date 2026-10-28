# nextBool()

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method

Generates and returns a new random Boolean value within the characteristics of the distribution.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nextBool() -> Bool
```

```objc
- (BOOL) nextBool;
```

## Return Value

A random Boolean value.

## Discussion

When using the [`GKRandomDistribution`](../gkrandomdistribution.md) class directly, generated Boolean values are uniform—any call to this method has an equal chance of returning [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md). Subclasses of [`GKRandomDistribution`](../gkrandomdistribution.md) can alter the relative probability of generating either value.

## See Also

### Generating Random Numbers
- [func nextInt() -> Int](./nextint%28%29.md)
  Generates and returns a new random integer within the bounds of the distribution.
- [func nextInt(upperBound: Int) -> Int](./nextint%28upperbound%29.md)
  Generates and returns a new random integer within the bounds of the distribution and less than the specified limit.
- [func nextUniform() -> Float](./nextuniform%28%29.md)
  Generates and returns a new random floating-point value within the characteristics of the distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/nextbool())*