# CMBufferHandlers

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A structure that stores the handlers that perform buffer operations.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
typedef struct { ... } CMBufferHandlers;
```

## Topics

### Buffer Handlers
- [compare](./cmbufferhandlers/compare.md)
  A handler callback the queue uses to perform an insertion sort of the queue.
- [typealias CMBufferCompareHandler](./cmbuffercomparehandler.md)
- [getDuration](./cmbufferhandlers/getduration.md)
- [getDecodeTimeStamp](./cmbufferhandlers/getdecodetimestamp.md)
- [getPresentationTimeStamp](./cmbufferhandlers/getpresentationtimestamp.md)
- [typealias CMBufferGetTimeHandler](./cmbuffergettimehandler.md)
- [getSize](./cmbufferhandlers/getsize.md)
- [typealias CMBufferGetSizeHandler](./cmbuffergetsizehandler.md)
- [isDataReady](./cmbufferhandlers/isdataready.md)
- [typealias CMBufferGetBooleanHandler](./cmbuffergetbooleanhandler.md)
- [dataBecameReadyNotification](./cmbufferhandlers/databecamereadynotification.md)
- [version](./cmbufferhandlers/version.md)
  The version number.

## See Also

### Creating a Queue
- [func CMBufferQueueCreateWithHandlers(CFAllocator?, CMItemCount, OpaquePointer, UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](./cmbufferqueuecreatewithhandlers%28_,_,_,_%29.md)
  Creates a buffer queue with handlers to inspect buffers.
- [func CMBufferQueueCreate(allocator: CFAllocator?, capacity: CMItemCount, callbacks: UnsafePointer<CMBufferCallbacks>, queueOut: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](./cmbufferqueuecreate%28allocator,capacity,callbacks,queueout%29.md)
  Creates a buffer queue with callbacks to inspect buffers.
- [struct CMBufferCallbacks](./cmbuffercallbacks.md)
  A structure that stores the callbacks that perform buffer operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferhandlers)*