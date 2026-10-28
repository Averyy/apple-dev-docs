# withContiguousStorageIfAvailable(_:)

**Framework**: Swift  
**Kind**: method  
**Role**: Instance Method

Executes a closure on the sequence’s contiguous storage.

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
func withContiguousStorageIfAvailable<R>(_ body: (UnsafeBufferPointer<Self.Element>) throws -> R) rethrows -> R?
```

## Return Value

The value returned from `body`, unless the sequence doesn’t support contiguous storage, in which case the method ignores `body` and returns `nil`.

## Discussion

This method calls `body(buffer)`, where `buffer` is a pointer to the collection’s contiguous storage. If the contiguous storage doesn’t exist, the collection creates it. If the collection doesn’t support an internal representation in a form of contiguous storage, the method doesn’t call `body` — it immediately returns `nil`.

The optimizer can often eliminate bounds- and uniqueness-checking within an algorithm. When that fails, however, invoking the same algorithm on the `buffer` argument may let you trade safety for speed.

Successive calls to this method may provide a different pointer on each call. Don’t store `buffer` outside of this method.

A `Collection` that provides its own implementation of this method must provide contiguous storage to its elements in the same order as they appear in the collection. This guarantees that it’s possible to generate contiguous mutable storage to any of its subsequences by slicing `buffer` with a range formed from the distances to the subsequence’s `startIndex` and `endIndex`, respectively.

## Parameters

- `body`: A closure that receives an `UnsafeBufferPointer` to the sequence’s contiguous storage.

## See Also

### Infrequently Used Functionality
- [func index(of: Self.Element) -> Self.Index?](./index%28of%29.md)
  Returns the first index where the specified value appears in the collection.
- [init(NSString)](./init%28_%29-5a5lw.md)
- [init(stringInterpolation: DefaultStringInterpolation)](./init%28stringinterpolation%29.md)
  Creates a new instance from an interpolated string literal.
- [init(stringLiteral: String)](./init%28stringliteral%29.md)
  Creates an instance initialized to the given string value.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](./init%28unicodescalarliteral%29.md)
- [init(extendedGraphemeClusterLiteral: Self.StringLiteralType)](./init%28extendedgraphemeclusterliteral%29.md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./customplaygroundquicklook.md)
  A custom playground Quick Look for the `String` instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/withcontiguousstorageifavailable(_:))*