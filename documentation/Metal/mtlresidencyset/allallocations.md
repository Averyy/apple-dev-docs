# allAllocations

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The residency set’s current list of resource allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var allAllocations: [any MTLAllocation] { get }
```

#### Discussion

This property is an array of resource allocations, and its elements can be an arbitrary mix of [`MTLBuffer`](mtlbuffer.md), [`MTLTexture`](mtltexture.md), and [`MTLHeap`](mtlheap.md) instances.

The residency set updates the property’s value when you call the [`commit()`](mtlresidencyset/commit().md) method.

## See Also

- [var label: String?](mtlresidencyset/label.md)
  An optional name that can help you identify the residency set.
- [var device: any MTLDevice](mtlresidencyset/device.md)
  The Metal device that owns the residency set.
- [func containsAllocation(any MTLAllocation) -> Bool](mtlresidencyset/containsallocation(_:).md)
  Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [var allocationCount: Int](mtlresidencyset/allocationcount.md)
  The number of resource allocations in the residency set.
- [var allocatedSize: UInt64](mtlresidencyset/allocatedsize.md)
  The amount of resident memory, in bytes, the residency set’s resource allocations consume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/allallocations)*