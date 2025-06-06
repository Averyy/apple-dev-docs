# init(bytesNoCopy:count:deallocator:)

**Framework**: Foundation  
**Kind**: init

Creates a data buffer with memory content without copying the bytes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(bytesNoCopy bytes: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)
```

#### Discussion

If the result is mutated and is not a unique reference, then the `Data` will still follow copy-on-write semantics. In this case, the copy will use its own deallocator. Therefore, it is usually best to only use this initializer when you either enforce immutability with `let` or ensure that no other references to the underlying data are formed.

## Parameters

- `bytes`: A pointer to the bytes.
- `count`: The size of the bytes.
- `deallocator`: Specifies the mechanism to free the indicated buffer, or  .

## See Also

- [init()](data/init.md)
  Creates an empty data buffer.
- [init<S>(S)](data/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)](data/init(buffer:)-75sng.md)
  Creates a data buffer with copied memory content using a buffer pointer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](data/init(buffer:)-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytes: UnsafeRawPointer, count: Int)](data/init(bytes:count:).md)
  Creates data with copied memory content.
- [init(capacity: Int)](data/init(capacity:).md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(bytesnocopy:count:deallocator:))*