# writeAll(toAbsoluteOffset:_:)

**Framework**: System  
**Kind**: method

Writes a sequence of bytes to the given offset.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@discardableResult
func writeAll<S>(toAbsoluteOffset offset: Int64, _ sequence: S) throws -> Int where S : Sequence, S.Element == UInt8
```

#### Return Value

The number of bytes written, equal to the number of elements in `sequence`.

#### Discussion

This method either writes the entire contents of `sequence`, or throws an error if only part of the content was written. Unlike [`writeAll(_:)`](filedescriptor/writeall(_:).md), this method preserves the file descriptor’s existing offset.

If `sequence` doesn’t implement the [`withContiguousStorageIfAvailable(_:)`](https://developer.apple.com/documentation/Swift/Sequence/withContiguousStorageIfAvailable(_:)-4don7) method, temporary space will be allocated as needed.

## Parameters

- `offset`: The file offset where writing begins.
- `sequence`: The bytes to write.

## See Also

- [func write(UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/write(_:retryoninterrupt:).md)
  Writes the contents of a buffer at the current file offset.
- [func write(toAbsoluteOffset: Int64, UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/write(toabsoluteoffset:_:retryoninterrupt:).md)
  Writes the contents of a buffer at the specified offset.
- [func writeAll<S>(S) throws -> Int](filedescriptor/writeall(_:).md)
  Writes a sequence of bytes to the current offset and then updates the offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/writeall(toabsoluteoffset:_:))*