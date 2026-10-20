# distance(to:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

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
func distance(to other: Double) -> Double
```

#### Return Value

The distance from this value to `other`.

#### Discussion

If this type’s `Stride` type conforms to `BinaryInteger`, then for two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`. Using this method with types that have a noninteger `Stride` may result in an approximation.

> **Complexity**: O(1)

## Parameters

- `other`: The value to calculate the distance to.

## See Also

### Infrequently Used Functionality
- [init()](./init%28%29.md)
- [init(floatLiteral: Double)](./init%28floatliteral%29.md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Int64)](./init%28integerliteral%29.md)
  Creates an instance initialized to the specified integer value.
- [init(integerLiteral: Self)](./init%28integerliteral%29-6hc7j.md)
- [typealias FloatLiteralType](./floatliteraltype.md)
  A type that represents a floating-point literal.
- [typealias IntegerLiteralType](./integerliteraltype.md)
  A type that represents an integer literal.
- [func advanced(by: Double) -> Double](./advanced%28by%29.md)
  Returns a value that is offset the specified distance from this value.
- [typealias Stride](./stride.md)
  A type that represents the distance between two values.
- [func write<Target>(to: inout Target)](./write%28to%29.md)
  Writes a textual representation of this instance into the given output stream.
- [var hashValue: Int](./hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/distance(to:))*