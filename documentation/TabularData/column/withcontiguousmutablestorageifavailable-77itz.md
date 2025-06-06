# withContiguousMutableStorageIfAvailable(_:)

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
mutating func withContiguousMutableStorageIfAvailable<R>(_ body: (inout UnsafeMutableBufferPointer<WrappedElement?>) throws -> R) rethrows -> R?
```

#### Discussion

Use the version of this method that uses a buffer of non-optional elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/withcontiguousmutablestorageifavailable(_:)-77itz)*