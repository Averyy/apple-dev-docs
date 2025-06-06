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
func advanced(by amount: Float) -> Float
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

O(1)

## See Also

- [init()](float/init.md)
- [init(integerLiteral: Int64)](float/init(integerliteral:).md)
  Creates an instance initialized to the specified integer value.
- [init(floatLiteral: Float)](float/init(floatliteral:).md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Self)](float/init(integerliteral:)-6hc7h.md)
- [func distance(to: Float) -> Float](float/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func write<Target>(to: inout Target)](float/write(to:).md)
  Writes a textual representation of this instance into the given output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/advanced(by:))*