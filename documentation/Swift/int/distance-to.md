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
func distance(to other: Int) -> Int
```

#### Return Value

The distance from this value to `other`.

#### Discussion

For two values `x` and `y`, and a distance `n = x.distance(to: y)`, `x.advanced(by: n) == y`.

## Parameters

- `other`: The value to calculate the distance to.

## See Also

- [init()](int/init.md)
  Creates a new value equal to zero.
- [init(integerLiteral: Self)](int/init(integerliteral:).md)
- [typealias IntegerLiteralType](int/integerliteraltype.md)
  A type that represents an integer literal.
- [func advanced(by: Int) -> Int](int/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [typealias Stride](int/stride.md)
  A type that represents the distance between two values.
- [var hashValue: Int](int/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/distance(to:))*