# atomicMemoryFence(ordering:)

**Framework**: Synchronization  
**Kind**: func

Establishes a memory ordering without associating it with a particular atomic operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func atomicMemoryFence(ordering: AtomicUpdateOrdering)
```

#### Discussion

- A relaxed fence has no effect.
- An acquiring fence ties to any preceding atomic operation that reads a value, and synchronizes with any releasing operation whose value was read.
- A releasing fence ties to any subsequent atomic operation that modifies a value, and synchronizes with any acquiring operation that reads the result.
- An acquiring and releasing fence is a combination of an acquiring and a releasing fence.
- A sequentially consistent fence behaves like an acquiring and releasing fence, and ensures that the fence itself is part of the single, total ordering for all sequentially consistent operations.

This operation corresponds to `std::atomic_thread_fence` in C++.

Be aware that Thread Sanitizer does not support fences and may report false-positive races for data protected by a fence.

## See Also

- [struct AtomicLoadOrdering](atomicloadordering.md)
  Specifies the memory ordering semantics of an atomic load operation.
- [struct AtomicStoreOrdering](atomicstoreordering.md)
  Specifies the memory ordering semantics of an atomic store operation.
- [struct AtomicUpdateOrdering](atomicupdateordering.md)
  Specifies the memory ordering semantics of an atomic read-modify-write operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicmemoryfence(ordering:))*