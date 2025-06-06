# withContiguousMutableStorageIfAvailable(_:)

**Framework**: TabularData  
**Kind**: method

Call `body(buffer)`, where `buffer` provides access to the non-optional contiguous mutable storage of the entire column. If the column contains missing values, `body` is not called and `nil` is returned.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
mutating func withContiguousMutableStorageIfAvailable<R>(_ body: (inout UnsafeMutableBufferPointer<WrappedElement>) throws -> R) rethrows -> R?
```

#### Return Value

The value returned by `body`, or `nil`.

#### Discussion

The optimizer can often eliminate bounds- and uniqueness-checking within an algorithm. When that fails, however, invoking the same algorithm on `body`’s argument may let you trade safety for speed.

> **Note**: `buffer` must not be replaced by `body`.

`buffer` must not be replaced by `body`.

## Parameters

- `body`: A closure to be executed using the elements of this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/column/withcontiguousmutablestorageifavailable(_:)-9j9p8)*