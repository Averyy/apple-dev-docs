# init(buffer:offset:size:)

**Framework**: RealityKit  
**Kind**: init

Creates a slice referencing a sub-range of the given buffer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(buffer: LowLevelBufferResource, offset: Int, size: Int) throws(LowLevelRenderContextError)
```

#### Discussion

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if `offset` or `size` fall outside the buffer’s allocated capacity.

## Parameters

- `buffer`: The buffer this slice references.
- `offset`: The byte offset into `buffer` at which this slice begins.
- `size`: The size of this slice, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelbufferslice/init(buffer:offset:size:))*