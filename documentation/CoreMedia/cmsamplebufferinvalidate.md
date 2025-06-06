# CMSampleBufferInvalidate(_:)

**Framework**: Core Media  
**Kind**: func

Invalidates a sample buffer by calling its invalidation callback.

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
func CMSampleBufferInvalidate(_ sbuf: CMSampleBuffer) -> OSStatus
```

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

An invalid sample buffer can’t be used — all accessors will return [`kCMSampleBufferError_Invalidated`](kcmsamplebuffererror_invalidated.md).

> ❗ **Important**:  You shouldn’t invalidate a sample buffer that another module may be accessing concurrently.

 You shouldn’t invalidate a sample buffer that another module may be accessing concurrently.

## Parameters

- `sbuf`: The sample buffer to invalidate.

## See Also

- [func CMSampleBufferSetInvalidateHandler(CMSampleBuffer, invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus](cmsamplebuffersetinvalidatehandler(_:invalidatehandler:).md)
  Sets the sample buffer’s invalidation handler.
- [func CMSampleBufferIsValid(CMSampleBuffer) -> Bool](cmsamplebufferisvalid(_:).md)
  Returns a Boolean value that indicates whether a sample buffer is valid.
- [func CMSampleBufferSetInvalidateCallback(CMSampleBuffer, callback: CMSampleBufferInvalidateCallback, refcon: UInt64) -> OSStatus](cmsamplebuffersetinvalidatecallback(_:callback:refcon:).md)
  Sets the sample buffer’s invalidation callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferinvalidate(_:))*