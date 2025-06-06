# write(_:retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Writes the contents of a buffer at the current file offset.

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
func write(_ buffer: UnsafeRawBufferPointer, retryOnInterrupt: Bool = true) throws -> Int
```

## Mentions

- [Adopting Swift File Operations](adopting-file-operations.md)

#### Return Value

The number of bytes that were written.

#### Discussion

After writing, this method increments the file’s offset by the number of bytes written. To change the file’s offset, call the [`seek(offset:from:)`](filedescriptor/seek(offset:from:).md) method.

The corresponding C function is `write`.

## Parameters

- `buffer`: The region of memory that contains the data being written.
- `retryOnInterrupt`: Whether to retry the write operation   if it throws  .   The default is  .   Pass   to try only once and throw an error upon interruption.

## See Also

- [func write(toAbsoluteOffset: Int64, UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/write(toabsoluteoffset:_:retryoninterrupt:).md)
  Writes the contents of a buffer at the specified offset.
- [func writeAll<S>(S) throws -> Int](filedescriptor/writeall(_:).md)
  Writes a sequence of bytes to the current offset and then updates the offset.
- [func writeAll<S>(toAbsoluteOffset: Int64, S) throws -> Int](filedescriptor/writeall(toabsoluteoffset:_:).md)
  Writes a sequence of bytes to the given offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/write(_:retryoninterrupt:))*