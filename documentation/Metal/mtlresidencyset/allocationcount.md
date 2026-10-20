# allocationCount

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The number of resource allocations in the residency set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var allocationCount: Int { get }
```

```objc
@property (readonly) NSUInteger allocationCount;
```

#### Discussion

The value is the number of elements in [`allAllocations`](./allallocations.md). The residency set updates the property’s value when you call the [`commit()`](./commit%28%29.md) method.

## See Also

### Inspecting a residency set
- [var label: String?](./label.md)
  An optional name that can help you identify the residency set.
- [var device: any MTLDevice](./device.md)
  The Metal device that owns the residency set.
- [func containsAllocation(any MTLAllocation) -> Bool](./containsallocation%28_%29.md)
  Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [var allAllocations: [any MTLAllocation]](./allallocations.md)
  The residency set’s current list of resource allocations.
- [var allocatedSize: UInt64](./allocatedsize.md)
  The amount of resident memory, in bytes, the residency set’s resource allocations consume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/allocationcount)*