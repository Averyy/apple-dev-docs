# makeBuffer(length:options:offset:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a buffer at a specified offset on the heap.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = [], offset: Int) -> (any MTLBuffer)?
```

```objc
- (id<MTLBuffer>) newBufferWithLength:(NSUInteger) length options:(MTLResourceOptions) options offset:(NSUInteger) offset;
```

## Return Value

A new buffer, or `nil` if the heap is not a placement heap.

## Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [`MTLHeapType.placement`](../mtlheaptype/placement.md)
- The buffer’s storage mode option needs to match the heap’s [`storageMode`](./storagemode.md) property
- The buffer’s CPU cache mode option needs to match the heap’s [`cpuCacheMode`](./cpucachemode.md) property

Use the [`heapBufferSizeAndAlign(length:options:)`](../mtldevice/heapbuffersizeandalign%28length,options%29.md) method to determine the required size and alignment. If you don’t align the buffer correctly or it extends past the end of the heap, the behavior is undefined.

> **Note**:  The new buffer can implicitly alias the underlying memory of other resources already in the heap within the overlapping half-open range of `[offset, offset + requiredSize)`.

## Parameters

- `length`: The size of the buffer, in bytes.
- `options`: Options that describe the properties of the buffer.
- `offset`: The distance, in bytes, to place the buffer relative to the start of the heap.

## See Also

### Creating buffers from a heap
- [func makeBuffer(length: Int, options: MTLResourceOptions) -> (any MTLBuffer)?](./makebuffer%28length,options%29.md)
  Creates a buffer on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/makebuffer(length:options:offset:))*