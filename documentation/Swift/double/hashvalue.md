# hashValue

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

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
- [func distance(to: Double) -> Double](./distance%28to%29.md)
  Returns the distance from this value to the given value, expressed as a stride.
- [typealias Stride](./stride.md)
  A type that represents the distance between two values.
- [func write<Target>(to: inout Target)](./write%28to%29.md)
  Writes a textual representation of this instance into the given output stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/hashvalue)*