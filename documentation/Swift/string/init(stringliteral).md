# init(stringLiteral:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates an instance initialized to the given string value.

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
init(stringLiteral value: String)
```

## Discussion

Do not call this initializer directly. It is used by the compiler when you initialize a string using a string literal. For example:

```swift
let nextStop = "Clark & Lake"
```

This assignment to the `nextStop` constant calls this string literal initializer behind the scenes.

## See Also

### Infrequently Used Functionality
- [func index(of: Self.Element) -> Self.Index?](./index%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [init(NSString)](./init%28_%29-5a5lw.md)
- [init(stringInterpolation: DefaultStringInterpolation)](./init%28stringinterpolation%29.md)
  Creates a new instance from an interpolated string literal.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](./init%28unicodescalarliteral%29.md)
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](./init%28extendedgraphemeclusterliteral%29.md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for the `String` instance.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousstorageifavailable%28_%29.md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(stringliteral:))*