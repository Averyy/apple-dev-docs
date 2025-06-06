# CMBufferValidationHandler

**Framework**: Core Media  
**Kind**: typealias

A type alias for a handler that tests whether a buffer is in a valid state to add to a queue.

**Availability**:
- iOS 12.2+
- iPadOS 12.2+
- Mac Catalyst 13.1+
- macOS 10.14.4+
- tvOS 12.2+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
typealias CMBufferValidationHandler = (CMBufferQueue, CMBuffer) -> OSStatus
```

## See Also

- [func CMBufferQueueSetValidationHandler(CMBufferQueue, CMBufferValidationHandler) -> OSStatus](cmbufferqueuesetvalidationhandler(_:_:).md)
  A validation handler for the queue to call before enqueuing buffers.
- [func CMBufferQueueSetValidationCallback(CMBufferQueue, callback: CMBufferValidationCallback, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueuesetvalidationcallback(_:callback:refcon:).md)
  A validation callback for the queue to call before enqueuing buffers.
- [typealias CMBufferValidationCallback](cmbuffervalidationcallback.md)
  A type alias for a callback that tests whether a buffer is in a valid state to add to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffervalidationhandler)*