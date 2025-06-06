# nextBool()

**Framework**: GameplayKit  
**Kind**: method  
**Required**: Yes

Generates and returns a new random Boolean value.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
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

Typically, custom classes implementing this protocol should implement the [`nextBool()`](gkrandom/nextbool().md) method based on the value returned by the [`nextInt(upperBound:)`](gkrandom/nextint(upperbound:).md) method. Alternative implementations are possible, but may lead to less uniform results.

## See Also

- [func nextInt() -> Int](gkrandom/nextint.md)
  Generates and returns a new random integer.
- [func nextInt(upperBound: Int) -> Int](gkrandom/nextint(upperbound:).md)
  Generates and returns a new random integer less than the specified limit.
- [func nextUniform() -> Float](gkrandom/nextuniform.md)
  Generates and returns a new random floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandom/nextbool())*