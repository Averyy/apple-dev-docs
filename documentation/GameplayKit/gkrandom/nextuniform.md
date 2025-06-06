# nextUniform()

**Framework**: GameplayKit  
**Kind**: method  
**Required**: Yes

Generates and returns a new random floating-point value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nextUniform() -> Float
```

#### Return Value

A random floating-point value in the range `[0.0, 1.0]`.

#### Discussion

The distribution of multiple samplings is uniform within the range `[0.0, 1.0]`; that is, the probability of this method returning any one value is approximately equal to that of returning any other value.

Typically, custom classes implementing this protocol should implement the [`nextUniform()`](gkrandom/nextuniform().md) method based on the value returned by the [`nextInt(upperBound:)`](gkrandom/nextint(upperbound:).md) method. Alternative implementations are possible, but may lead to less uniform results.

## See Also

- [func nextInt() -> Int](gkrandom/nextint.md)
  Generates and returns a new random integer.
- [func nextInt(upperBound: Int) -> Int](gkrandom/nextint(upperbound:).md)
  Generates and returns a new random integer less than the specified limit.
- [func nextBool() -> Bool](gkrandom/nextbool.md)
  Generates and returns a new random Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandom/nextuniform())*