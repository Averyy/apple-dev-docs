# CMBufferCallbacks

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A structure that stores the callbacks that perform buffer operations.

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
struct CMBufferCallbacks
```

```c
typedef struct { ... } CMBufferCallbacks;
```

#### Overview

With the exception of `isDataReady`, all these callbacks must always return the same result for the same arguments.

A buffer’s duration, timestamps, or position relative to other buffers must not appear to change while it is in the queue. Once `isDataReady` has returned true for a given `CMBuffer`, it must always return true for that `CMBuffer`.

Durations must always be positive.

## Topics

### Properties
- [var compare: CMBufferCompareCallback?](./cmbuffercallbacks/compare.md)
  This callback is called multiple times from [`CMBufferQueueEnqueue(_:buffer:)`](./cmbufferqueueenqueue%28_,buffer%29.md), to perform an insertion sort.
- [typealias CMBufferCompareCallback](./cmbuffercomparecallback.md)
  Callback that compares one `CMBuffer` with another.
- [typealias CMBufferGetBooleanCallback](./cmbuffergetbooleancallback.md)
  Callback that returns a Boolean value from a `CMBuffer`.
- [typealias CMBufferGetTimeCallback](./cmbuffergettimecallback.md)
  Callback that returns a `CMTime` from a `CMBuffer`.
- [var dataBecameReadyNotification: Unmanaged<CFString>?](./cmbuffercallbacks/databecamereadynotification.md)
  If triggers of type `kCMBufferQueueTrigger_WhenDataBecomesReady` are installed, the queue will listen for this notification on the head buffer.
- [var getDecodeTimeStamp: CMBufferGetTimeCallback?](./cmbuffercallbacks/getdecodetimestamp.md)
  Client callback that returns a `CMTime` from a `CMBuffer`.
- [var getDuration: CMBufferGetTimeCallback](./cmbuffercallbacks/getduration.md)
  This callback is called (once) during enqueue and dequeue operations to update the total duration of the queue.
- [var getPresentationTimeStamp: CMBufferGetTimeCallback?](./cmbuffercallbacks/getpresentationtimestamp.md)
  Client callback that returns a `CMTime` from a `CMBuffer`.
- [var getSize: CMBufferGetSizeCallback?](./cmbuffercallbacks/getsize.md)
- [var isDataReady: CMBufferGetBooleanCallback?](./cmbuffercallbacks/isdataready.md)
  This callback is called from [`CMBufferQueueDequeueIfDataReady(_:)`](./cmbufferqueuedequeueifdataready%28_%29.md), to ask if the buffer that is about to be dequeued is ready.
- [var refcon: UnsafeMutableRawPointer?](./cmbuffercallbacks/refcon.md)
  Contextual data to be passed to all callbacks.
- [var version: UInt32](./cmbuffercallbacks/version.md)
  The callback version.
### Initializers
- [init(version: UInt32, refcon: UnsafeMutableRawPointer?, getDecodeTimeStamp: CMBufferGetTimeCallback?, getPresentationTimeStamp: CMBufferGetTimeCallback?, getDuration: CMBufferGetTimeCallback, isDataReady: CMBufferGetBooleanCallback?, compare: CMBufferCompareCallback?, dataBecameReadyNotification: Unmanaged<CFString>?, getSize: CMBufferGetSizeCallback?)](./cmbuffercallbacks/init%28version,refcon,getdecodetimestamp,getpresentationtimestamp,getduration,isdataready,compare,databecamereadynotification,getsize%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Creating a Queue
- [func CMBufferQueueCreateWithHandlers(CFAllocator?, CMItemCount, OpaquePointer, UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](./cmbufferqueuecreatewithhandlers%28_,_,_,_%29.md)
  Creates a buffer queue with handlers to inspect buffers.
- [func CMBufferQueueCreate(allocator: CFAllocator?, capacity: CMItemCount, callbacks: UnsafePointer<CMBufferCallbacks>, queueOut: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](./cmbufferqueuecreate%28allocator,capacity,callbacks,queueout%29.md)
  Creates a buffer queue with callbacks to inspect buffers.
- [CMBufferHandlers](./cmbufferhandlers.md)
  A structure that stores the handlers that perform buffer operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbuffercallbacks)*