# nextBool()

**Framework**: GameplayKit  
**Kind**: method

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

#### Return Value

A random Boolean value.

#### Discussion

When using the [`GKRandomDistribution`](gkrandomdistribution.md) class directly, generated Boolean values are uniform—any call to this method has an equal chance of returning [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false). Subclasses of [`GKRandomDistribution`](gkrandomdistribution.md) can alter the relative probability of generating either value.

## See Also

- [func nextInt() -> Int](gkrandomdistribution/nextint.md)
  Generates and returns a new random integer within the bounds of the distribution.
- [func nextInt(upperBound: Int) -> Int](gkrandomdistribution/nextint(upperbound:).md)
  Generates and returns a new random integer within the bounds of the distribution and less than the specified limit.
- [func nextUniform() -> Float](gkrandomdistribution/nextuniform.md)
  Generates and returns a new random floating-point value within the characteristics of the distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution/nextbool())*