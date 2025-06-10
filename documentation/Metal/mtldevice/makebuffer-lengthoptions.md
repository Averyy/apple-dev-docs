# makeBuffer(length:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a buffer the method clears with zero values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

## Mentions

- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)
- [Setting Resource Storage Modes](setting-resource-storage-modes.md)

#### Return Value

A new [`MTLBuffer`](mtlbuffer.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `length`: The size of the new buffer, in bytes.
- `options`: An   instance that sets the buffer’s storage and hazard-tracking modes. See   and   for more information.

## See Also

- [var maxBufferLength: Int](mtldevice/maxbufferlength.md)
  The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [func makeBuffer(bytes: UnsafeRawPointer, length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtldevice/makebuffer(bytes:length:options:).md)
  Allocates a new buffer of a given length and initializes its contents by copying existing data into it.
- [func makeBuffer(bytesNoCopy: UnsafeMutableRawPointer, length: Int, options: MTLResourceOptions, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?) -> (any MTLBuffer)?](mtldevice/makebuffer(bytesnocopy:length:options:deallocator:).md)
  Creates a buffer that wraps an existing contiguous memory allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makebuffer(length:options:))*