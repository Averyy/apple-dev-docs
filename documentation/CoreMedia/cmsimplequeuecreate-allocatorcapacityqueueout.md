# CMSimpleQueueCreate(allocator:capacity:queueOut:)

**Framework**: Core Media  
**Kind**: func

Creates a queue that has the specified capacity.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMSimpleQueueCreate(allocator: CFAllocator?, capacity: Int32, queueOut: UnsafeMutablePointer<CMSimpleQueue?>) -> OSStatus
```

#### Return Value

A result code. See [`Simple Queue Error Codes`](simple-queue-errors.md).

#### Discussion

On return, the caller owns the returned `CMSimpleQueue`, and must release it when done with it.

## Parameters

- `allocator`: Allocator used to allocate storage for the queue.
- `capacity`: Capacity of the queue (maximum number of elements holdable at any given time). Required (must not be  ). Must be a positive value.
- `queueOut`: On output, a reference to the newly created queue. Must not be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsimplequeuecreate(allocator:capacity:queueout:))*