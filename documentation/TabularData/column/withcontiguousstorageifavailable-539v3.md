# withContiguousStorageIfAvailable(_:)

**Framework**: TabularData  
**Kind**: method

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

#### Discussion

Use the version of this method that uses a buffer of non-optional elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/withcontiguousstorageifavailable(_:)-539v3)*