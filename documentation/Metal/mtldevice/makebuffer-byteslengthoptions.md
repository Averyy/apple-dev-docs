# makeBuffer(bytes:length:options:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Allocates a new buffer of a given length and initializes its contents by copying existing data into it.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(bytes pointer: UnsafeRawPointer, length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

## Mentions

- [Copying Data to a Private Resource](copying-data-to-a-private-resource.md)

#### Return Value

A new [`MTLBuffer`](mtlbuffer.md) instance if the method completes successfully; otherwise `nil`.

## Parameters

- `pointer`: A pointer to the starting memory address the method copies the initialization data from.
- `length`: The size of the new buffer, in bytes, and the number of bytes the method copies from  .
- `options`: An   instance that sets the buffer’s storage and hazard-tracking modes. See   and   for more information.

## See Also

- [var maxBufferLength: Int](mtldevice/maxbufferlength.md)
  The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtldevice/makebuffer(length:options:).md)
  Creates a buffer the method clears with zero values.
- [func makeBuffer(bytesNoCopy: UnsafeMutableRawPointer, length: Int, options: MTLResourceOptions, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?) -> (any MTLBuffer)?](mtldevice/makebuffer(bytesnocopy:length:options:deallocator:).md)
  Creates a buffer that wraps an existing contiguous memory allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makebuffer(bytes:length:options:))*