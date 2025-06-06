# hashValue

**Framework**: Swift  
**Kind**: property

The hash value.

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
var hashValue: Int { get }
```

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

`hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

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
- [func advanced(by: Double) -> Double](double/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Double) -> Double](double/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [typealias Stride](double/stride.md)
  A type that represents the distance between two values.
- [func write<Target>(to: inout Target)](double/write(to:).md)
  Writes a textual representation of this instance into the given output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/hashvalue)*