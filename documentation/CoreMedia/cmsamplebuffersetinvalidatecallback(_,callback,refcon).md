# CMSampleBufferSetInvalidateCallback(_:callback:refcon:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Sets the sample buffer’s invalidation callback.

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
func CMSampleBufferSetInvalidateCallback(_ sbuf: CMSampleBuffer, callback invalidateCallback: CMSampleBufferInvalidateCallback, refcon invalidateRefCon: UInt64) -> OSStatus
```

```c
extern OSStatus CMSampleBufferSetInvalidateCallback(CMSampleBufferRef sbuf, CMSampleBufferInvalidateCallback invalidateCallback, uint64_t invalidateRefCon);
```

## Return Value

A result code. See [Sample Buffer Error Codes](./sample-buffer-errors.md).

## Discussion

A sample buffer can only have one invalidation callback. The invalidation callback *isn’t* called during ordinary sample buffer finalization.

## Parameters

- `sbuf`: The sample buffer being modified.
- `invalidateCallback`: Reference to a function to be called during `CMSampleBufferInvalidate`.
- `invalidateRefCon`: Reference constant to be passed to `invalidateCallback`.

## Topics

### Callbacks
- [typealias CMSampleBufferInvalidateCallback](./cmsamplebufferinvalidatecallback.md)
  Client callback called by [`CMSampleBufferInvalidate(_:)`](./cmsamplebufferinvalidate%28_%29.md).

## See Also

### Invalidating Sample Buffers
- [func CMSampleBufferSetInvalidateHandler(CMSampleBuffer, invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus](./cmsamplebuffersetinvalidatehandler%28_,invalidatehandler%29.md)
  Sets the sample buffer’s invalidation handler.
- [func CMSampleBufferInvalidate(CMSampleBuffer) -> OSStatus](./cmsamplebufferinvalidate%28_%29.md)
  Invalidates a sample buffer by calling its invalidation callback.
- [func CMSampleBufferIsValid(CMSampleBuffer) -> Bool](./cmsamplebufferisvalid%28_%29.md)
  Returns a Boolean value that indicates whether a sample buffer is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetinvalidatecallback(_:callback:refcon:))*