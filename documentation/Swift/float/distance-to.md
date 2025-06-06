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
func distance(to other: Float) -> Float
```

#### Return Value

The distance from this value to `other`.

#### Discussion

If this type’s `Stride` type conforms to `BinaryInteger`, then for two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`. Using this method with types that have a noninteger `Stride` may result in an approximation.

> **Note**: O(1)

O(1)

## Parameters

- `other`: The value to calculate the distance to.

## See Also

- [init()](float/init.md)
- [init(integerLiteral: Int64)](float/init(integerliteral:).md)
  Creates an instance initialized to the specified integer value.
- [init(floatLiteral: Float)](float/init(floatliteral:).md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Self)](float/init(integerliteral:)-6hc7h.md)
- [func advanced(by: Float) -> Float](float/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func write<Target>(to: inout Target)](float/write(to:).md)
  Writes a textual representation of this instance into the given output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/distance(to:))*