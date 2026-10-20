# advanced(by:)

**Framework**: Swift  
**Kind**: method

Returns a value that is offset the specified distance from this value.

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
func advanced(by n: Int) -> Int
```

#### Return Value

A value that is offset from this value by `n`.

#### Discussion

Use the `advanced(by:)` method in generic code to offset a value by a specified distance. If you’re working directly with numeric values, use the addition operator (`+`) instead of this method.

For a value `x`, a distance `n`, and a value `y = x.advanced(by: n)`, `x.distance(to: y) == n`.

## Parameters

- `n`: The distance to advance this value.

## See Also

- [init()](int/init.md)
  Creates a new value equal to zero.
- [init(integerLiteral: Self)](int/init(integerliteral:).md)
- [typealias IntegerLiteralType](int/integerliteraltype.md)
  A type that represents an integer literal.
- [func distance(to: Int) -> Int](int/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [typealias Stride](int/stride.md)
  A type that represents the distance between two values.
- [var hashValue: Int](int/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/advanced(by:))*