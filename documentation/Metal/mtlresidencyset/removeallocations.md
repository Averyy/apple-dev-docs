# removeAllocations(_:)

**Framework**: Metal  
**Kind**: method

Stages multiple resources to leave the residency set’s list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+

## Declaration

```swift
func removeAllocations(_ allocations: [any MTLAllocation])
```

#### Discussion

Finalize the removal of these resource allocations, and all other changes you stage, by calling a residency set’s [`commit()`](mtlresidencyset/commit().md) method.

## Parameters

- `allocations`: An array of resource allocations, whose elements can be an arbitrarily mix of  ,  , and   instances.

## See Also

- [func removeAllAllocations()](mtlresidencyset/removeallallocations.md)
  Stages all the resources in the residency set to leave its list of allocations.
- [func removeAllocation(any MTLAllocation)](mtlresidencyset/removeallocation(_:).md)
  Stages a single resource to leave the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/removeallocations(_:))*