# CFReadStreamCreateWithBytesNoCopy(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a readable stream for a block of memory.

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
func CFReadStreamCreateWithBytesNoCopy(_ alloc: CFAllocator!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex, _ bytesDeallocator: CFAllocator!) -> CFReadStream!
```

```c
extern CFReadStreamRefCFReadStreamCreateWithBytesNoCopy(CFAllocatorRef alloc, const UInt8 *bytes, CFIndex length, CFAllocatorRef bytesDeallocator);
```

## Return Value

The new read stream, or `NULL` on failure. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

You must open the stream, using [`CFReadStreamOpen(_:)`](./cfreadstreamopen%28_%29.md), before reading from it.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `bytes`: The memory buffer to read. This memory must exist for the lifetime of the new stream.
- `length`: The size of `bytes`.
- `bytesDeallocator`: The allocator to use to deallocate `bytes` when the stream is deallocated. Pass kCFAllocatorNull to prevent the stream from deallocating `bytes`.

## See Also

### Creating a Read Stream
- [func CFReadStreamCreateWithFile(CFAllocator!, CFURL!) -> CFReadStream!](./cfreadstreamcreatewithfile%28_,_%29.md)
  Creates a readable stream for a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamcreatewithbytesnocopy(_:_:_:_:))*