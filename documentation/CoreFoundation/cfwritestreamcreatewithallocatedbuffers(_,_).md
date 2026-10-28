# CFWriteStreamCreateWithAllocatedBuffers(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a writable stream for a growable block of memory.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFWriteStreamCreateWithAllocatedBuffers(_ alloc: CFAllocator!, _ bufferAllocator: CFAllocator!) -> CFWriteStream!
```

```c
extern CFWriteStreamRefCFWriteStreamCreateWithAllocatedBuffers(CFAllocatorRef alloc, CFAllocatorRef bufferAllocator);
```

## Return Value

A new write stream. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

New buffers are allocated using `bufferAllocator` as bytes are written to the stream. At any point, you can recover the bytes thus far written by asking for the property kCFStreamPropertyDataWritten with [`CFWriteStreamCopyProperty(_:_:)`](./cfwritestreamcopyproperty%28_,_%29.md).

You must open the stream, using [`CFWriteStreamOpen(_:)`](./cfwritestreamopen%28_%29.md), before writing to it.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `bufferAllocator`: The allocator to use to allocate memory for the stream’s memory buffers. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

## See Also

### Creating a Write Stream
- [func CFWriteStreamCreateWithBuffer(CFAllocator!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFWriteStream!](./cfwritestreamcreatewithbuffer%28_,_,_%29.md)
  Creates a writable stream for a fixed-size block of memory.
- [func CFWriteStreamCreateWithFile(CFAllocator!, CFURL!) -> CFWriteStream!](./cfwritestreamcreatewithfile%28_,_%29.md)
  Creates a writable stream for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamcreatewithallocatedbuffers(_:_:))*