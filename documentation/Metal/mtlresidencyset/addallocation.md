# addAllocation(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Stages a single resource to join the residency set’s list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func addAllocation(_ allocation: any MTLAllocation)
```

## Mentions

- [Simplifying GPU Resource Management with Residency Sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Discussion

Finalize the inclusion of these resource allocations, and all other changes you stage, by calling a residency set’s [`commit()`](mtlresidencyset/commit().md) method.

## Parameters

- `allocation`: A resource allocation, such as an  ,  , or  .

## See Also

- [func addAllocations([any MTLAllocation])](mtlresidencyset/addallocations(_:).md)
  Stages multiple resources to join the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/addallocation(_:))*