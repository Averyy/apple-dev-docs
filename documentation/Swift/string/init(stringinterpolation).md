# init(stringInterpolation:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

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

## Discussion

You don’t need to call this initializer directly. It’s used by the compiler when you create a string using string interpolation. Instead, use string interpolation to create a new string by including values, literals, variables, or expressions enclosed in parentheses, prefixed by a backslash (`\(`…`)`).

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

### Infrequently Used Functionality
- [func index(of: Self.Element) -> Self.Index?](./index%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [init(NSString)](./init%28_%29-5a5lw.md)
- [init(stringLiteral: String)](./init%28stringliteral%29.md)
  Creates an instance initialized to the given string value.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](./init%28unicodescalarliteral%29.md)
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](./init%28extendedgraphemeclusterliteral%29.md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for the `String` instance.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousstorageifavailable%28_%29.md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(stringinterpolation:))*