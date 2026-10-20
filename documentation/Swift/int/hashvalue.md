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

#### Discussion

Hash values are not guaranteed to be equal across different executions of your program. Do not save hash values to use during a future execution.

> ❗ **Important**: `hashValue` is deprecated as a `Hashable` requirement. To conform to `Hashable`, implement the `hash(into:)` requirement instead. The compiler provides an implementation for `hashValue` for you.

## See Also

### Infrequently Used Functionality
- [init()](./init%28%29.md)
  Creates a new value equal to zero.
- [init(integerLiteral: Self)](./init%28integerliteral%29.md)
- [typealias IntegerLiteralType](./integerliteraltype.md)
  A type that represents an integer literal.
- [func distance(to: Int) -> Int](./distance%28to%29.md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func advanced(by: Int) -> Int](./advanced%28by%29.md)
  Returns a value that is offset the specified distance from this value.
- [typealias Stride](./stride.md)
  A type that represents the distance between two values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/hashvalue)*