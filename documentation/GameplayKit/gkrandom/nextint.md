# nextInt()

**Framework**: GameplayKit  
**Kind**: method  
**Required**: Yes

Generates and returns a new random integer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func nextInt() -> Int
```

#### Return Value

A random integer value in the range `[INT32_MIN, INT32_MAX]`.

#### Discussion

For more information, see [`GameplayKit Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/GameplayKit_Guide/index.html#//apple_ref/doc/uid/TP40015172).

## See Also

- [func nextInt(upperBound: Int) -> Int](gkrandom/nextint(upperbound:).md)
  Generates and returns a new random integer less than the specified limit.
- [func nextUniform() -> Float](gkrandom/nextuniform.md)
  Generates and returns a new random floating-point value.
- [func nextBool() -> Bool](gkrandom/nextbool.md)
  Generates and returns a new random Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandom/nextint())*