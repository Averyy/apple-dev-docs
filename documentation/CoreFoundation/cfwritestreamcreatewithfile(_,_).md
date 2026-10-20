# CFWriteStreamCreateWithFile(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Creates a writable stream for a file.

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
func CFWriteStreamCreateWithFile(_ alloc: CFAllocator!, _ fileURL: CFURL!) -> CFWriteStream!
```

```c
extern CFWriteStreamRefCFWriteStreamCreateWithFile(CFAllocatorRef alloc, CFURLRef fileURL);
```

#### Return Value

The new write stream, or `NULL` on failure. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

The stream overwrites an existing file unless you set the kCFStreamPropertyAppendToFile to kCFBooleanTrue with [`CFWriteStreamSetProperty(_:_:_:)`](./cfwritestreamsetproperty%28_,_,_%29.md), in which case the stream appends data to the file.

You must open the stream, using [`CFWriteStreamOpen(_:)`](./cfwritestreamopen%28_%29.md), before writing to it.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `fileURL`: The URL of the file to which to write. The URL must use a file scheme.

## See Also

### Creating a Write Stream
- [func CFWriteStreamCreateWithAllocatedBuffers(CFAllocator!, CFAllocator!) -> CFWriteStream!](./cfwritestreamcreatewithallocatedbuffers%28_,_%29.md)
  Creates a writable stream for a growable block of memory.
- [func CFWriteStreamCreateWithBuffer(CFAllocator!, UnsafeMutablePointer<UInt8>!, CFIndex) -> CFWriteStream!](./cfwritestreamcreatewithbuffer%28_,_,_%29.md)
  Creates a writable stream for a fixed-size block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfwritestreamcreatewithfile(_:_:))*