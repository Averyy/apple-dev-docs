# CMSampleBufferIsValid(_:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A Boolean indicating whether the sample buffer is still valid.

#### Discussion

Returns false if `sbuf` is `NULL` or `CMSampleBufferInvalidate` was called, true otherwise. Doesn’t perform any kind of exhaustive validation of the sample buffer.

## Parameters

- `sbuf`: The   being interrogated.

## See Also

- [func CMSampleBufferSetInvalidateHandler(CMSampleBuffer, invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus](cmsamplebuffersetinvalidatehandler(_:invalidatehandler:).md)
  Sets the sample buffer’s invalidation handler.
- [func CMSampleBufferInvalidate(CMSampleBuffer) -> OSStatus](cmsamplebufferinvalidate(_:).md)
  Invalidates a sample buffer by calling its invalidation callback.
- [func CMSampleBufferSetInvalidateCallback(CMSampleBuffer, callback: CMSampleBufferInvalidateCallback, refcon: UInt64) -> OSStatus](cmsamplebuffersetinvalidatecallback(_:callback:refcon:).md)
  Sets the sample buffer’s invalidation callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebufferisvalid(_:))*