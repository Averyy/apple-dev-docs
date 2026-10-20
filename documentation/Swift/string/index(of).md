# index(of:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Returns the first index where the specified value appears in the collection.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift - Deprecated in 5.0 (renamed: firstIndex(of:))

## Declaration

```swift
func index(of element: Self.Element) -> Self.Index?
```

Available when `Element` conforms to `Equatable`.

## See Also

### Infrequently Used Functionality
- [init(NSString)](./init%28_%29-5a5lw.md)
- [init(stringInterpolation: DefaultStringInterpolation)](./init%28stringinterpolation%29.md)
  Creates a new instance from an interpolated string literal.
- [init(stringLiteral: String)](./init%28stringliteral%29.md)
  Creates an instance initialized to the given string value.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](./init%28unicodescalarliteral%29.md)
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](./init%28extendedgraphemeclusterliteral%29.md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for the `String` instance.
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?](./withcontiguousstorageifavailable%28_%29.md)
  Executes a closure on the sequence’s contiguous storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/index(of:))*