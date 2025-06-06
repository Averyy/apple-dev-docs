# init(_:)

**Framework**: Foundation  
**Kind**: init

Creates a new instance of a collection containing the elements of a sequence.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init<S>(_ elements: S) where S : Sequence, Self.Element == S.Element
```

## Parameters

- `elements`: The sequence of elements for the new collection.

## See Also

- [init()](data/init.md)
  Creates an empty data buffer.
- [init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)](data/init(buffer:)-75sng.md)
  Creates a data buffer with copied memory content using a buffer pointer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](data/init(buffer:)-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytes: UnsafeRawPointer, count: Int)](data/init(bytes:count:).md)
  Creates data with copied memory content.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](data/init(bytesnocopy:count:deallocator:).md)
  Creates a data buffer with memory content without copying the bytes.
- [init(capacity: Int)](data/init(capacity:).md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(_:))*