# nextInt(upperBound:)

**Framework**: GameplayKit  
**Kind**: method  
**Required**: Yes

Generates and returns a new random integer less than the specified limit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nextInt(upperBound: Int) -> Int
```

#### Return Value

A new random integer greater than or equal to zero and less than the value of the `upperBound` parameter.

## Parameters

- `upperBound`: A limit on the values of random numbers to generate.

## See Also

- [func nextInt() -> Int](gkrandom/nextint.md)
  Generates and returns a new random integer.
- [func nextUniform() -> Float](gkrandom/nextuniform.md)
  Generates and returns a new random floating-point value.
- [func nextBool() -> Bool](gkrandom/nextbool.md)
  Generates and returns a new random Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandom/nextint(upperbound:))*