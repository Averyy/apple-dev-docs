# distance(to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the distance from this value to the given value, expressed as a stride.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func distance(to other: Self) -> Self.Stride
```

#### Return Value

The distance from this value to `other`.

#### Discussion

If this type’s `Stride` type conforms to `BinaryInteger`, then for two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`. Using this method with types that have a noninteger `Stride` may result in an approximation.

> **Complexity**: O(1)

## Parameters

- `other`: The value to calculate the distance to.

## Default Implementations

### Strideable Implementations
- [func distance(to: Self) -> Int](./distance%28to%29-1mibk.md)
  Returns the distance from this value to the given value, expressed as a stride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/strideable/distance(to:))*