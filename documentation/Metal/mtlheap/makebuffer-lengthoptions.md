# makeBuffer(length:options:)

**Framework**: Metal  
**Kind**: method  
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

#### Return Value

A new buffer object backed by heap memory, or `nil` if the heap memory is full.

#### Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [`MTLHeapType.automatic`](mtlheaptype/automatic.md)
- The buffer’s storage mode option needs to match the heap’s [`storageMode`](mtlheap/storagemode.md) property
- The buffer’s CPU cache mode option needs to match the heap’s [`cpuCacheMode`](mtlheap/cpucachemode.md) property

## Parameters

- `length`: The size, in bytes, of the buffer.
- `options`: Options that describe the properties of the buffer.

## See Also

- [func makeBuffer(length: Int, options: MTLResourceOptions, offset: Int) -> (any MTLBuffer)?](mtlheap/makebuffer(length:options:offset:).md)
  Creates a buffer at a specified offset on the heap.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlheap/makebuffer(length:options:))*