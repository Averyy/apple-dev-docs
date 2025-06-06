# CMBufferQueueCreateWithHandlers(_:_:_:_:)

**Framework**: Core Media  
**Kind**: func

Creates a buffer queue with handlers to inspect buffers.

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
func CMBufferQueueCreateWithHandlers(_ allocator: CFAllocator?, _ capacity: CMItemCount, _ handlers: OpaquePointer, _ queueOut: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus
```

## See Also

- [func CMBufferQueueCreate(allocator: CFAllocator?, capacity: CMItemCount, callbacks: UnsafePointer<CMBufferCallbacks>, queueOut: UnsafeMutablePointer<CMBufferQueue?>) -> OSStatus](cmbufferqueuecreate(allocator:capacity:callbacks:queueout:).md)
  Creates a buffer queue with callbacks to inspect buffers.
- [struct CMBufferCallbacks](cmbuffercallbacks.md)
  A structure that stores the callbacks that perform buffer operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmbufferqueuecreatewithhandlers(_:_:_:_:))*