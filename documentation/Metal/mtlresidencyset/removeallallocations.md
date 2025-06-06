# removeAllAllocations()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Stages all the resources in the residency set to leave its list of allocations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func removeAllAllocations()
```

#### Discussion

Finalize the removal of these resource allocations, and all others changes you stage, by calling a residency set’s [`commit()`](mtlresidencyset/commit().md) method.

## See Also

- [func removeAllocation(any MTLAllocation)](mtlresidencyset/removeallocation(_:).md)
  Stages a single resource to leave the residency set’s list of allocations.
- [func removeAllocations([any MTLAllocation])](mtlresidencyset/removeallocations(_:).md)
  Stages multiple resources to leave the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/removeallallocations())*