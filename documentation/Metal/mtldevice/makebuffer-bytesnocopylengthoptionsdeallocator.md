# makeBuffer(bytesNoCopy:length:options:deallocator:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a buffer that wraps an existing contiguous memory allocation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length: Int, options: MTLResourceOptions = [], deallocator: ((UnsafeMutableRawPointer, Int) -> Void)? = nil) -> (any MTLBuffer)?
```

#### Return Value

A new [`MTLBuffer`](mtlbuffer.md) instance if the method completes successfully; otherwise `nil`.

#### Discussion

> ❗ **Important**:  The existing memory allocation needs to exist within a single virtual memory (VM) region.

## Parameters

- `pointer`: A page-aligned pointer to the starting memory address.
- `length`: The size of the new buffer, in bytes, that results in a page-aligned region of memory.
- `options`: An   instance that sets the buffer’s storage and hazard-tracking modes. See   and   for more information.
- `deallocator`: A block the framework invokes when it deallocates the buffer so that your app can release the underlying memory; otherwise   to opt out.

## See Also

- [var maxBufferLength: Int](mtldevice/maxbufferlength.md)
  The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtldevice/makebuffer(length:options:).md)
  Creates a buffer the method clears with zero values.
- [func makeBuffer(bytes: UnsafeRawPointer, length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](mtldevice/makebuffer(bytes:length:options:).md)
  Allocates a new buffer of a given length and initializes its contents by copying existing data into it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makebuffer(bytesnocopy:length:options:deallocator:))*