# distance(to:)

**Framework**: Swift  
**Kind**: method

Returns the distance from this value to the given value, expressed as a stride.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func distance(to other: Float16) -> Float16
```

#### Return Value

The distance from this value to `other`.

#### Discussion

If this type’s `Stride` type conforms to `BinaryInteger`, then for two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`. Using this method with types that have a noninteger `Stride` may result in an approximation.

> **Note**: O(1)

## Parameters

- `other`: The value to calculate the distance to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/distance(to:))*