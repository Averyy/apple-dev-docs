# CMBufferQueueSetValidationCallback(_:callback:refcon:)

**Framework**: Core Media  
**Kind**: func

A validation callback for the queue to call before enqueuing buffers.

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
func CMBufferQueueSetValidationCallback(_ queue: CMBufferQueue, callback: CMBufferValidationCallback, refcon: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

A result code. See `Result Codes`.

## Parameters

- `queue`:   that will use the validation callback.
- `callback`: Callback that will validate each buffer enqueued.
- `refcon`: Context refcon for validation callback.

## See Also

- [func CMBufferQueueSetValidationHandler(CMBufferQueue, CMBufferValidationHandler) -> OSStatus](cmbufferqueuesetvalidationhandler(_:_:).md)
  A validation handler for the queue to call before enqueuing buffers.
- [typealias CMBufferValidationHandler](cmbuffervalidationhandler.md)
  A type alias for a handler that tests whether a buffer is in a valid state to add to a queue.
- [typealias CMBufferValidationCallback](cmbuffervalidationcallback.md)
  A type alias for a callback that tests whether a buffer is in a valid state to add to a queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuesetvalidationcallback(_:callback:refcon:))*