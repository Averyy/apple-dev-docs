# distance(to:)

**Framework**: Swift  
**Kind**: method

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
func distance(to other: Self) -> Int
```

#### Return Value

The distance from this value to `other`.

#### Discussion

For two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`.

## Parameters

- `other`: The value to calculate the distance to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/distance(to:))*