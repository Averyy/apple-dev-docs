# init(stringInterpolation:)

**Framework**: Swift  
**Kind**: init

Creates a new instance from an interpolated string literal.

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
init(stringInterpolation: DefaultStringInterpolation)
```

#### Discussion

Do not call this initializer directly. It is used by the compiler when you create a string using string interpolation. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

```swift
let price = 2
let number = 3
let message = """
              If one cookie costs \(price) dollars, \
              \(number) cookies cost \(price * number) dollars.
              """
print(message)
// Prints "If one cookie costs 2 dollars, 3 cookies cost 6 dollars."
```

## See Also

- [func index(of: Self.Element) -> Self.Index?](string/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [init(NSString)](string/init(_:)-5a5lw.md)
- [init(stringLiteral: String)](string/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](string/init(unicodescalarliteral:).md)
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](string/init(extendedgraphemeclusterliteral:).md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](string/customplaygroundquicklook.md)
  A custom playground Quick Look for the `String` instance.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](string/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(stringinterpolation:))*