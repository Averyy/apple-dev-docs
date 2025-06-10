# makeBuffer(length:options:placementSparsePageSize:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new placement sparse buffer of a specific length.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = [], placementSparsePageSize: MTLSparsePageSize) -> (any MTLBuffer)?
```

#### Return Value

A [`MTLBuffer`](mtlbuffer.md) instance, or `nil` if the function failed.

#### Discussion

This method creates a new placement sparse [`MTLBuffer`](mtlbuffer.md) of a specific length. You assign memory to placement sparse buffers using a [`MTLHeap`](mtlheap.md) of type [`MTLHeapType.placement`](mtlheaptype/placement.md).

## Parameters

- `length`: The size of the  , in bytes.
- `options`: A   instance that establishes the buffer’s storage modes.
- `placementSparsePageSize`:   to use for the placement sparse buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makebuffer(length:options:placementsparsepagesize:))*