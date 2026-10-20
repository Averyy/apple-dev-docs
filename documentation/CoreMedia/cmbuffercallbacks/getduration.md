# getDuration

**Framework**: Core Media  
**Kind**: property  
**Role**: Instance Property

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

```c
CMBufferGetTimeCallback getDuration;
```

#### Discussion

This must not be `NULL`.

## See Also

### Properties
- [var compare: CMBufferCompareCallback?](./compare.md)
  This callback is called multiple times from [`CMBufferQueueEnqueue(_:buffer:)`](../cmbufferqueueenqueue%28_,buffer%29.md), to perform an insertion sort.
- [typealias CMBufferCompareCallback](../cmbuffercomparecallback.md)
  Callback that compares one `CMBuffer` with another.
- [typealias CMBufferGetBooleanCallback](../cmbuffergetbooleancallback.md)
  Callback that returns a Boolean value from a `CMBuffer`.
- [typealias CMBufferGetTimeCallback](../cmbuffergettimecallback.md)
  Callback that returns a `CMTime` from a `CMBuffer`.
- [var dataBecameReadyNotification: Unmanaged<CFString>?](./databecamereadynotification.md)
  If triggers of type `kCMBufferQueueTrigger_WhenDataBecomesReady` are installed, the queue will listen for this notification on the head buffer.
- [var getDecodeTimeStamp: CMBufferGetTimeCallback?](./getdecodetimestamp.md)
  Client callback that returns a `CMTime` from a `CMBuffer`.
- [var getPresentationTimeStamp: CMBufferGetTimeCallback?](./getpresentationtimestamp.md)
  Client callback that returns a `CMTime` from a `CMBuffer`.
- [var getSize: CMBufferGetSizeCallback?](./getsize.md)
- [var isDataReady: CMBufferGetBooleanCallback?](./isdataready.md)
  This callback is called from [`CMBufferQueueDequeueIfDataReady(_:)`](../cmbufferqueuedequeueifdataready%28_%29.md), to ask if the buffer that is about to be dequeued is ready.
- [var refcon: UnsafeMutableRawPointer?](./refcon.md)
  Contextual data to be passed to all callbacks.
- [var version: UInt32](./version.md)
  The callback version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks/getduration)*