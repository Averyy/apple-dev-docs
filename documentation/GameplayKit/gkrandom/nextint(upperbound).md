# nextInt(upperBound:)

**Framework**: GameplayKit  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (NSUInteger) nextIntWithUpperBound:(NSUInteger) upperBound;
```

## Return Value

A new random integer greater than or equal to zero and less than the value of the `upperBound` parameter.

## Parameters

- `upperBound`: A limit on the values of random numbers to generate.

## See Also

### Generating Random Numbers
- [func nextInt() -> Int](./nextint%28%29.md)
  Generates and returns a new random integer.
- [func nextUniform() -> Float](./nextuniform%28%29.md)
  Generates and returns a new random floating-point value.
- [func nextBool() -> Bool](./nextbool%28%29.md)
  Generates and returns a new random Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gameplaykit/gkrandom/nextint(upperbound:))*