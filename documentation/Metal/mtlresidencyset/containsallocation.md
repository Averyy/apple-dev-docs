# containsAllocation(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func containsAllocation(_ anAllocation: any MTLAllocation) -> Bool
```

## Parameters

- `anAllocation`: A resource allocation, such as an  ,  , or  .

## See Also

- [var label: String?](mtlresidencyset/label.md)
  An optional name that can help you identify the residency set.
- [var device: any MTLDevice](mtlresidencyset/device.md)
  The Metal device that owns the residency set.
- [var allAllocations: [any MTLAllocation]](mtlresidencyset/allallocations.md)
  The residency set’s current list of resource allocations.
- [var allocationCount: Int](mtlresidencyset/allocationcount.md)
  The number of resource allocations in the residency set.
- [var allocatedSize: UInt64](mtlresidencyset/allocatedsize.md)
  The amount of resident memory, in bytes, the residency set’s resource allocations consume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/containsallocation(_:))*