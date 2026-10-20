# nextBool()

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (BOOL) nextBool;
```

#### Return Value

A random Boolean value.

#### Discussion

Typically, custom classes implementing this protocol should implement the [`nextBool()`](./nextbool%28%29.md) method based on the value returned by the [`nextInt(upperBound:)`](./nextint%28upperbound%29.md) method. Alternative implementations are possible, but may lead to less uniform results.

## See Also

### Generating Random Numbers
- [func nextInt() -> Int](./nextint%28%29.md)
  Generates and returns a new random integer.
- [func nextInt(upperBound: Int) -> Int](./nextint%28upperbound%29.md)
  Generates and returns a new random integer less than the specified limit.
- [func nextUniform() -> Float](./nextuniform%28%29.md)
  Generates and returns a new random floating-point value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandom/nextbool())*