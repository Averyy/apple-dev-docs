# CMSampleBufferSetInvalidateCallback(_:callback:refcon:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

A result code. See [`Sample Buffer Error Codes`](sample-buffer-errors.md).

#### Discussion

A sample buffer can only have one invalidation callback. The invalidation callback  called during ordinary sample buffer finalization.

## Parameters

- `sbuf`: The sample buffer being modified.
- `invalidateCallback`: Reference to a function to be called during  .
- `invalidateRefCon`: Reference constant to be passed to  .

## Topics

### Callbacks
- [typealias CMSampleBufferInvalidateCallback](cmsamplebufferinvalidatecallback.md)
  Client callback called by [`CMSampleBufferInvalidate(_:)`](cmsamplebufferinvalidate(_:).md).

## See Also

- [func CMSampleBufferSetInvalidateHandler(CMSampleBuffer, invalidateHandler: CMSampleBufferInvalidateHandler) -> OSStatus](cmsamplebuffersetinvalidatehandler(_:invalidatehandler:).md)
  Sets the sample buffer’s invalidation handler.
- [func CMSampleBufferInvalidate(CMSampleBuffer) -> OSStatus](cmsamplebufferinvalidate(_:).md)
  Invalidates a sample buffer by calling its invalidation callback.
- [func CMSampleBufferIsValid(CMSampleBuffer) -> Bool](cmsamplebufferisvalid(_:).md)
  Returns a Boolean value that indicates whether a sample buffer is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffersetinvalidatecallback(_:callback:refcon:))*