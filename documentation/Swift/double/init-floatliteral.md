# init(floatLiteral:)

**Framework**: Swift  
**Kind**: init

Creates an instance initialized to the specified floating-point value.

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
init(floatLiteral value: Double)
```

#### Discussion

Do not call this initializer directly. Instead, initialize a variable or constant using a floating-point literal. For example:

```swift
let x = 21.5
```

In this example, the assignment to the `x` constant calls this floating-point literal initializer behind the scenes.

## Parameters

- `value`: The value to create.

## See Also

- [init()](double/init.md)
- [init(integerLiteral: Int64)](double/init(integerliteral:).md)
  Creates an instance initialized to the specified integer value.
- [init(integerLiteral: Self)](double/init(integerliteral:)-6hc7j.md)
- [typealias FloatLiteralType](double/floatliteraltype.md)
  A type that represents a floating-point literal.
- [typealias IntegerLiteralType](double/integerliteraltype.md)
  A type that represents an integer literal.
- [func advanced(by: Double) -> Double](double/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Double) -> Double](double/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [typealias Stride](double/stride.md)
  A type that represents the distance between two values.
- [func write<Target>(to: inout Target)](double/write(to:).md)
  Writes a textual representation of this instance into the given output stream.
- [var hashValue: Int](double/hashvalue.md)
  The hash value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(floatliteral:))*