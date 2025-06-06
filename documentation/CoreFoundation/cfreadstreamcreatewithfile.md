# CFReadStreamCreateWithFile(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a readable stream for a file.

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
func CFReadStreamCreateWithFile(_ alloc: CFAllocator!, _ fileURL: CFURL!) -> CFReadStream!
```

#### Return Value

The new readable stream object, or `NULL` on failure. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

#### Discussion

You must open the stream, using [`CFReadStreamOpen(_:)`](cfreadstreamopen(_:).md), before reading from it.

## Parameters

- `alloc`: The allocator to use to allocate memory for the new object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `fileURL`: The URL of the file to read. The URL must use the file scheme.

## See Also

- [func CFReadStreamCreateWithBytesNoCopy(CFAllocator!, UnsafePointer<UInt8>!, CFIndex, CFAllocator!) -> CFReadStream!](cfreadstreamcreatewithbytesnocopy(_:_:_:_:).md)
  Creates a readable stream for a block of memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfreadstreamcreatewithfile(_:_:))*