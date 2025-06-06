# CMBufferQueueCreate(allocator:capacity:callbacks:queueOut:)

**Framework**: Core Media  
**Kind**: func

Creates a buffer queue with callbacks to inspect buffers.

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
func CMBufferQueueCreate(allocator: CFAllocator?, capacity: CMItemCount, callbacks: UnsafePointer<CMBufferCallbacks>, queueOut: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

On return, the caller owns the returned `CMBufferQueue`, and must release it when done with it.

## Parameters

- `allocator`: The allocator to use for allocating the   object. Pass   to use the default allocator.
- `capacity`: Maximum number of buffers in the queue.  Pass 0 to create a queue that will grow as needed.
- `callbacks`: Callbacks the queue should use to interrogate the buffer objects.  This struct is copied internally, so the client can pass a pointer to a temporary struct on the stack.
- `queueOut`: On Output, the newly created  .

## See Also

- [func CMBufferQueueCreateWithHandlers(CFAllocator?, CMItemCount, OpaquePointer, UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](cmbufferqueuecreatewithhandlers(_:_:_:_:).md)
  Creates a buffer queue with handlers to inspect buffers.
- [struct CMBufferCallbacks](cmbuffercallbacks.md)
  A structure that stores the callbacks that perform buffer operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuecreate(allocator:capacity:callbacks:queueout:))*