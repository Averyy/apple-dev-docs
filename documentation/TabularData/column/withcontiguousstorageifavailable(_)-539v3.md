# withContiguousStorageIfAvailable(_:)

**Framework**: TabularData  
**Kind**: method  
**Role**: Instance Method

This method always returns `nil` without calling `body`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
func withContiguousStorageIfAvailable<R>(_ body: (UnsafeBufferPointer<WrappedElement?>) throws -> R) rethrows -> R?
```

## Discussion

Use the version of this method that uses a buffer of non-optional elements.

## See Also

### Allocating contiguous storage
- [func withContiguousStorageIfAvailable<R>((UnsafeBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](./withcontiguousstorageifavailable%28_%29-6nbz3.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<WrappedElement>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29-9j9p8.md)
  Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous mutable storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.
- [func withContiguousMutableStorageIfAvailable<R>((inout UnsafeMutableBufferPointer<WrappedElement?>) throws -> R) rethrows -> R?](./withcontiguousmutablestorageifavailable%28_%29-77itz.md)
  This method always returns `nil` without calling `body`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/withcontiguousstorageifavailable(_:)-539v3)*