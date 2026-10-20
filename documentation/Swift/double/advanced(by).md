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
func advanced(by amount: Double) -> Double
```

#### Return Value

A value that is offset from this value by `n`.

#### Discussion

Use the `advanced(by:)` method in generic code to offset a value by a specified distance. If you’re working directly with numeric values, use the addition operator (`+`) instead of this method.

```swift
func addOne<T: Strideable>(to x: T) -> T
    where T.Stride: ExpressibleByIntegerLiteral
{
    return x.advanced(by: 1)
}

let x = addOne(to: 5)
// x == 6
let y = addOne(to: 3.5)
// y = 4.5
```

If this type’s `Stride` type conforms to `BinaryInteger`, then for a value `x`, a distance `n`, and a value `y = x.advanced(by: n)`, `x.distance(to: y) == n`. Using this method with types that have a noninteger `Stride` may result in an approximation. If the result of advancing by `n` is not representable as a value of this type, then a runtime error may occur.

> **Note**: O(1)

## See Also

- [init()](double/init.md)
- [init(floatLiteral: Double)](double/init(floatliteral:).md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Int64)](double/init(integerliteral:).md)
  Creates an instance initialized to the specified integer value.
- [init(integerLiteral: Self)](double/init(integerliteral:)-6hc7j.md)
- [typealias FloatLiteralType](double/floatliteraltype.md)
  A type that represents a floating-point literal.
- [typealias IntegerLiteralType](double/integerliteraltype.md)
  A type that represents an integer literal.
- [func distance(to: Double) -> Double](double/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [typealias Stride](double/stride.md)
  A type that represents the distance between two values.
- [func write<Target>(to: inout Target)](double/write(to:).md)
  Writes a textual representation of this instance into the given output stream.
- [var hashValue: Int](double/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/advanced(by:))*