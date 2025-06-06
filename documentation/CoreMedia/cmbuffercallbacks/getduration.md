# getDuration

**Framework**: Core Media  
**Kind**: property

This callback is called (once) during enqueue and dequeue operations to update the total duration of the queue.

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
var getDuration: CMBufferGetTimeCallback
```

#### Discussion

This must not be `NULL`.

## See Also

- [var compare: CMBufferCompareCallback?](cmbuffercallbacks/compare.md)
  This callback is called multiple times from [`CMBufferQueueEnqueue(_:buffer:)`](cmbufferqueueenqueue(_:buffer:).md), to perform an insertion sort.
- [typealias CMBufferCompareCallback](cmbuffercomparecallback.md)
  Callback that compares one `CMBuffer` with another.
- [typealias CMBufferGetBooleanCallback](cmbuffergetbooleancallback.md)
  Callback that returns a Boolean value from a `CMBuffer`.
- [typealias CMBufferGetTimeCallback](cmbuffergettimecallback.md)
  Callback that returns a `CMTime` from a `CMBuffer`.
- [var dataBecameReadyNotification: Unmanaged<CFString>?](cmbuffercallbacks/databecamereadynotification.md)
  If triggers of type `kCMBufferQueueTrigger_WhenDataBecomesReady` are installed, the queue will listen for this notification on the head buffer.
- [var getDecodeTimeStamp: CMBufferGetTimeCallback?](cmbuffercallbacks/getdecodetimestamp.md)
  Client callback that returns a `CMTime` from a `CMBuffer`.
- [var getPresentationTimeStamp: CMBufferGetTimeCallback?](cmbuffercallbacks/getpresentationtimestamp.md)
  Client callback that returns a `CMTime` from a `CMBuffer`.
- [var getSize: CMBufferGetSizeCallback?](cmbuffercallbacks/getsize.md)
- [var isDataReady: CMBufferGetBooleanCallback?](cmbuffercallbacks/isdataready.md)
  This callback is called from [`CMBufferQueueDequeueIfDataReady(_:)`](cmbufferqueuedequeueifdataready(_:).md), to ask if the buffer that is about to be dequeued is ready.
- [var refcon: UnsafeMutableRawPointer?](cmbuffercallbacks/refcon.md)
  Contextual data to be passed to all callbacks.
- [var version: UInt32](cmbuffercallbacks/version.md)
  The callback version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/getduration)*