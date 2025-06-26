# resolveCounterRange(_:)

**Framework**: Metal  
**Kind**: method

Resolves heap data on the CPU timeline.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func resolveCounterRange(_ range: Range<Int>) throws -> Data?
```

#### Discussion

This method resolves heap data in the CPU timeline. Your app needs to ensure the GPU work has completed in order to retrieve the data correctly. You can alternatively resolve the heap data in the GPU timeline by calling [`resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:`](mtl4commandbuffer/resolvecounterheap:withrange:intobuffer:atoffset:waitfence:updatefence:.md).

- Returns a newly allocated autoreleased NSData containing tightly packed resolved heap counter values.

> **Note**: When resolving counters in the CPU timeline, signaling an instance of [`MTLSharedEvent`](mtlsharedevent.md) after any workloads write counters (and waiting on that signal on the CPU) is sufficient to ensure synchronization.

## Parameters

- `range`: The range in the heap to resolve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4counterheap/resolvecounterrange(_:)-8y97c)*