# CMBufferValidationCallback

**Framework**: Core Media  
**Kind**: typealias

A type alias for a callback that tests whether a buffer is in a valid state to add to a queue.

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
typealias CMBufferValidationCallback = (CMBufferQueue, CMBuffer, UnsafeMutableRawPointer?) -> OSStatus
```

#### Discussion

[`CMBufferQueueEnqueue(_:buffer:)`](cmbufferqueueenqueue(_:buffer:).md) will call this function to validate buffers.

Return `noErr` if the buffer is in a valid state to add.

Return a nonzero error code if the buffer should be rejected; [`CMBufferQueueEnqueue(_:buffer:)`](cmbufferqueueenqueue(_:buffer:).md) will return this error to the caller. If you do not have a more descriptive error code, use `kCMBufferQueueError_InvalidBuffer`.

##### Callback Parameters

## See Also

- [func CMBufferQueueSetValidationHandler(CMBufferQueue, CMBufferValidationHandler) -> OSStatus](cmbufferqueuesetvalidationhandler(_:_:).md)
  A validation handler for the queue to call before enqueuing buffers.
- [typealias CMBufferValidationHandler](cmbuffervalidationhandler.md)
  A type alias for a handler that tests whether a buffer is in a valid state to add to a queue.
- [func CMBufferQueueSetValidationCallback(CMBufferQueue, callback: CMBufferValidationCallback, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueuesetvalidationcallback(_:callback:refcon:).md)
  A validation callback for the queue to call before enqueuing buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffervalidationcallback)*