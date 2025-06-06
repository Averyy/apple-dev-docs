# CMBufferQueueSetValidationHandler(_:_:)

**Framework**: Core Media  
**Kind**: func

A validation handler for the queue to call before enqueuing buffers.

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
func CMBufferQueueSetValidationHandler(_ queue: CMBufferQueue, _ handler: @escaping CMBufferValidationHandler) -> OSStatus
```

## See Also

- [typealias CMBufferValidationHandler](cmbuffervalidationhandler.md)
  A type alias for a handler that tests whether a buffer is in a valid state to add to a queue.
- [func CMBufferQueueSetValidationCallback(CMBufferQueue, callback: CMBufferValidationCallback, refcon: UnsafeMutableRawPointer?) -> OSStatus](cmbufferqueuesetvalidationcallback(_:callback:refcon:).md)
  A validation callback for the queue to call before enqueuing buffers.
- [typealias CMBufferValidationCallback](cmbuffervalidationcallback.md)
  A type alias for a callback that tests whether a buffer is in a valid state to add to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuesetvalidationhandler(_:_:))*