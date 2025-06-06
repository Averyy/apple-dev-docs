# CFWriteStreamCreateWithBuffer(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a writable stream for a fixed-size block of memory.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFWriteStreamCreateWithBuffer(_ alloc: CFAllocator!, _ buffer: UnsafeMutablePointer<UInt8>!, _ bufferCapacity: CFIndex) -> CFWriteStream!
```

#### Return Value

A new write stream, or `NULL` on failure. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

When `buffer` is filled after writing `bufferCapacity` bytes, the stream is exhausted and its status becomes [`CFStreamStatus.atEnd`](cfstreamstatus/atend.md).

You must open the stream, using [`CFWriteStreamOpen(_:)`](cfwritestreamopen(_:).md), before writing to it.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `buffer`: The memory buffer into which to write data. This buffer must exist for the lifetime of the stream.
- `bufferCapacity`: The size of   and the maximum number of bytes that can be written.

## See Also

- [func CFWriteStreamCreateWithAllocatedBuffers(CFAllocator!, CFAllocator!) -> CFWriteStream!](cfwritestreamcreatewithallocatedbuffers(_:_:).md)
  Creates a writable stream for a growable block of memory.
- [func CFWriteStreamCreateWithFile(CFAllocator!, CFURL!) -> CFWriteStream!](cfwritestreamcreatewithfile(_:_:).md)
  Creates a writable stream for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamcreatewithbuffer(_:_:_:))*