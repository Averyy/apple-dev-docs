# CMSampleBufferIsValid(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a sample buffer is valid.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSampleBufferIsValid(_ sbuf: CMSampleBuffer) -> Bool
```

```c
extern Boolean CMSampleBufferIsValid(CMSampleBufferRef sbuf);
```

## Return Value

A Boolean indicating whether the sample buffer is still valid.

## Discussion

Returns false if `sbuf` is `NULL` or `CMSampleBufferInvalidate` was called, true otherwise. Doesn’t perform any kind of exhaustive validation of the sample buffer.

## Parameters

- `sbuf`: The `CMSampleBuffer` being interrogated.

## See Also

### Invalidating Sample Buffers
- [func CMSampleBufferSetInvalidateHandler(CMSampleBuffer, invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus](./cmsamplebuffersetinvalidatehandler%28_,invalidatehandler%29.md)
  Sets the sample buffer’s invalidation handler.
- [func CMSampleBufferInvalidate(CMSampleBuffer) -> OSStatus](./cmsamplebufferinvalidate%28_%29.md)
  Invalidates a sample buffer by calling its invalidation callback.
- [func CMSampleBufferSetInvalidateCallback(CMSampleBuffer, callback: CMSampleBufferInvalidateCallback, refcon: UInt64) -> OSStatus](./cmsamplebuffersetinvalidatecallback%28_,callback,refcon%29.md)
  Sets the sample buffer’s invalidation callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferisvalid(_:))*