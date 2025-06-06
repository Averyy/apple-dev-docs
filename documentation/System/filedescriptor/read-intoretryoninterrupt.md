# read(into:retryOnInterrupt:)

**Framework**: System  
**Kind**: method

Reads bytes at the current file offset into a buffer.

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
func read(into buffer: UnsafeMutableRawBufferPointer, retryOnInterrupt: Bool = true) throws -> Int
```

## Mentions

- [Adopting Swift File Operations](adopting-file-operations.md)

#### Return Value

The number of bytes that were read.

#### Discussion

The doc://com.apple.documentation/documentation/swift/unsafemutablerawbufferpointer/count-95usp property of `buffer` determines the maximum number of bytes that are read into that buffer.

After reading, this method increments the file’s offset by the number of bytes read. To change the file’s offset, call the [`seek(offset:from:)`](filedescriptor/seek(offset:from:).md) method.

The corresponding C function is `read`.

## Parameters

- `buffer`: The region of memory to read into.
- `retryOnInterrupt`: Whether to retry the read operation   if it throws  .   The default is  .   Pass   to try only once and throw an error upon interruption.

## See Also

- [func read(fromAbsoluteOffset: Int64, into: UnsafeMutableRawBufferPointer, retryOnInterrupt: Bool) throws -> Int](filedescriptor/read(fromabsoluteoffset:into:retryoninterrupt:).md)
  Reads bytes at the specified offset into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/system/filedescriptor/read(into:retryoninterrupt:))*