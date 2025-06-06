# addAllocations(_:)

**Framework**: Metal  
**Kind**: method

Stages multiple resources to join the residency set’s list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+

## Declaration

```swift
func addAllocations(_ allocations: [any MTLAllocation])
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Finalize the inclusion of these resource allocations, and all other changes you stage, by calling a residency set’s [`commit()`](mtlresidencyset/commit().md) method.

## Parameters

- `allocations`: An array of resource allocations, whose elements can be an arbitrarily mix of  ,  , and   instances.

## See Also

- [func addAllocation(any MTLAllocation)](mtlresidencyset/addallocation(_:).md)
  Stages a single resource to join the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/addallocations(_:))*