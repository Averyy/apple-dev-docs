# write(toAbsoluteOffset:_:retryOnInterrupt:)

**Framework**: System  
**Kind**: method  
**Role**: Instance Method

Writes the contents of a buffer at the specified offset.

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
func write(toAbsoluteOffset offset: Int64, _ buffer: UnsafeRawBufferPointer, retryOnInterrupt: Bool = true) throws -> Int
```

## Mentions

- [Adopting Swift File Operations](../adopting-file-operations.md)

#### Return Value

The number of bytes that were written.

#### Discussion

Unlike [`write(_:retryOnInterrupt:)`](./write%28_,retryoninterrupt%29.md), this method leaves the file’s existing offset unchanged.

The corresponding C function is `pwrite`.

## Parameters

- `offset`: The file offset where writing begins.
- `buffer`: The region of memory that contains the data being written.
- `retryOnInterrupt`: Whether to retry the write operation if it throws [`interrupted`](../errno/interrupted.md). The default is `true`. Pass `false` to try only once and throw an error upon interruption.

## See Also

### Writing To A File
- [func write(UnsafeRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](./write%28_,retryoninterrupt%29.md)
  Writes the contents of a buffer at the current file offset.
- [func writeAll<S>(S) throws -> Int](./writeall%28_%29.md)
  Writes a sequence of bytes to the current offset and then updates the offset.
- [func writeAll<S>(toAbsoluteOffset: Int64, S) throws -> Int](./writeall%28toabsoluteoffset,_%29.md)
  Writes a sequence of bytes to the given offset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/write(toabsoluteoffset:_:retryoninterrupt:))*