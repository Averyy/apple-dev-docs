# makeCounterHeap(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new counter heap configured from a counter heap descriptor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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