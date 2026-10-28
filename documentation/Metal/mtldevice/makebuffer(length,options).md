# makeBuffer(length:options:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a buffer the method clears with zero values.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

```objc
- (id<MTLBuffer>) newBufferWithLength:(NSUInteger) length options:(MTLResourceOptions) options;
```

## Mentions

- [Copying data to a private resource](../copying-data-to-a-private-resource.md)
- [Setting resource storage modes](../setting-resource-storage-modes.md)

## Return Value

A new [`MTLBuffer`](../mtlbuffer.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `length`: The size of the new buffer, in bytes.
- `options`: An [`MTLResourceOptions`](../mtlresourceoptions.md) instance that sets the buffer’s storage and hazard-tracking modes. See [Resource fundamentals](../resource-fundamentals.md) and [Setting resource storage modes](../setting-resource-storage-modes.md) for more information.

## See Also

### Creating buffers
- [var maxBufferLength: Int](./maxbufferlength.md)
  The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [func makeBuffer(bytes: UnsafeRawPointer, length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](./makebuffer%28bytes,length,options%29.md)
  Allocates a new buffer of a given length and initializes its contents by copying existing data into it.
- [func makeBuffer(bytesNoCopy: UnsafeMutableRawPointer, length: Int, options: MTLResourceOptions, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)?) -> (any MTLBuffer)?](./makebuffer%28bytesnocopy,length,options,deallocator%29.md)
  Creates a buffer that wraps an existing contiguous memory allocation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makebuffer(length:options:))*