# makeCounterHeap(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new counter heap configured from a counter heap descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func makeCounterHeap(descriptor: MTL4CounterHeapDescriptor) throws -> any MTL4CounterHeap
```

#### Return Value

A [`MTL4CounterHeap`](mtl4counterheap.md) instance, or `nil` if the function failed.

## Parameters

- `descriptor`:   instance that configures the   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makecounterheap(descriptor:))*