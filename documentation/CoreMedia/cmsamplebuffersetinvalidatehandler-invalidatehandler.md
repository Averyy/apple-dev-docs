# CMSampleBufferSetInvalidateHandler(_:invalidateHandler:)

**Framework**: Core Media  
**Kind**: func

Sets the sample buffer’s invalidation handler.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSampleBufferSetInvalidateHandler(_ sbuf: CMSampleBuffer, invalidateHandler: @escaping CMSampleBufferInvalidateHandler) -> OSStatus
```

#### Discussion

A sample buffer can only have one invalidation callback. The invalidation callback isn’t called during ordinary sample buffer finalization.

## Parameters

- `sbuf`: The   being modified.
- `invalidateHandler`: Block to be called during  .

## Topics

### Handlers
- [typealias CMSampleBufferInvalidateHandler](cmsamplebufferinvalidatehandler.md)
  Client callback called by [`CMSampleBufferInvalidate(_:)`](cmsamplebufferinvalidate(_:).md).

## See Also

- [func CMSampleBufferInvalidate(CMSampleBuffer) -> OSStatus](cmsamplebufferinvalidate(_:).md)
  Invalidates a sample buffer by calling its invalidation callback.
- [func CMSampleBufferIsValid(CMSampleBuffer) -> Bool](cmsamplebufferisvalid(_:).md)
  Returns a Boolean value that indicates whether a sample buffer is valid.
- [func CMSampleBufferSetInvalidateCallback(CMSampleBuffer, callback: CMSampleBufferInvalidateCallback, refcon: UInt64) -> OSStatus](cmsamplebuffersetinvalidatecallback(_:callback:refcon:).md)
  Sets the sample buffer’s invalidation callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetinvalidatehandler(_:invalidatehandler:))*