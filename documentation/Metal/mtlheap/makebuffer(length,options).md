# makeBuffer(length:options:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a buffer on the heap.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

```objc
- (id<MTLBuffer>) newBufferWithLength:(NSUInteger) length options:(MTLResourceOptions) options;
```

## Return Value

A new buffer object backed by heap memory, or `nil` if the heap memory is full.

## Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [`MTLHeapType.automatic`](../mtlheaptype/automatic.md)
- The buffer’s storage mode option needs to match the heap’s [`storageMode`](./storagemode.md) property
- The buffer’s CPU cache mode option needs to match the heap’s [`cpuCacheMode`](./cpucachemode.md) property

## Parameters

- `length`: The size, in bytes, of the buffer.
- `options`: Options that describe the properties of the buffer.

## See Also

### Creating buffers from a heap
- [func makeBuffer(length: Int, options: MTLResourceOptions, offset: Int) -> (any MTLBuffer)?](./makebuffer%28length,options,offset%29.md)
  Creates a buffer at a specified offset on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/makebuffer(length:options:))*