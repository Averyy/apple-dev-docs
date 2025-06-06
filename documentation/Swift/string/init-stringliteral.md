# init(stringLiteral:)

**Framework**: Swift  
**Kind**: init

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

#### Discussion

Do not call this initializer directly. It is used by the compiler when you initialize a string using a string literal. For example:

```swift
let nextStop = "Clark & Lake"
```

This assignment to the `nextStop` constant calls this string literal initializer behind the scenes.

## See Also

- [func index(of: Self.Element) -> Self.Index?](string/index(of:).md)
  Returns the first index where the specified value appears in the collection.
- [init(NSString)](string/init(_:)-5a5lw.md)
- [init(stringInterpolation: DefaultStringInterpolation)](string/init(stringinterpolation:).md)
  Creates a new instance from an interpolated string literal.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](string/init(unicodescalarliteral:).md)
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](string/init(extendedgraphemeclusterliteral:).md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](string/customplaygroundquicklook.md)
  A custom playground Quick Look for the `String` instance.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](string/withcontiguousstorageifavailable(_:).md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(stringliteral:))*