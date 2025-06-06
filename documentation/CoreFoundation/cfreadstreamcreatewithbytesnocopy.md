# CFReadStreamCreateWithBytesNoCopy(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a readable stream for a block of memory.

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
func CFReadStreamCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFReadStream!
```

#### Return Value

The new read stream, or `NULL` on failure. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You must open the stream, using [`CFReadStreamOpen(_:)`](cfreadstreamopen(_:).md), before reading from it.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `bytes`: The memory buffer to read. This memory must exist for the lifetime of the new stream.
- `length`: The size of  .
- `bytesDeallocator`: The allocator to use to deallocate   when the stream is deallocated. Pass kCFAllocatorNull to prevent the stream from deallocating  .

## See Also

- [func CFReadStreamCreateWithFile(CFAllocator!, CFURL!) -> CFReadStream!](cfreadstreamcreatewithfile(_:_:).md)
  Creates a readable stream for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamcreatewithbytesnocopy(_:_:_:_:))*