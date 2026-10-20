# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An optional name that can help you identify the residency set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
var label: String? { get }
```

```objc
@property (readonly, nullable) NSString * label;
```

#### Discussion

The value of this property comes from the [`label`](../mtlresidencysetdescriptor/label.md) property of the [`MTLResidencySetDescriptor`](../mtlresidencysetdescriptor.md) instance you use to create the residency set with [`makeResidencySet(descriptor:)`](../mtldevice/makeresidencyset%28descriptor%29.md).

## See Also

### Inspecting a residency set
- [var device: any MTLDevice](./device.md)
  The Metal device that owns the residency set.
- [func containsAllocation(any MTLAllocation) -> Bool](./containsallocation%28_%29.md)
  Returns a Boolean value that indicates whether the residency set contains a specific resource allocation.
- [var allAllocations: [any MTLAllocation]](./allallocations.md)
  The residency set’s current list of resource allocations.
- [var allocationCount: Int](./allocationcount.md)
  The number of resource allocations in the residency set.
- [var allocatedSize: UInt64](./allocatedsize.md)
  The amount of resident memory, in bytes, the residency set’s resource allocations consume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/label)*