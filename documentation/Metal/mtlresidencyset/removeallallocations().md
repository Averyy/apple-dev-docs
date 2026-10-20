# removeAllAllocations()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) removeAllAllocations;
```

#### Discussion

Finalize the removal of these resource allocations, and all others changes you stage, by calling a residency set’s [`commit()`](./commit%28%29.md) method.

## See Also

### Removing allocations
- [func removeAllocation(any MTLAllocation)](./removeallocation%28_%29.md)
  Stages a single resource to leave the residency set’s list of allocations.
- [func removeAllocations([any MTLAllocation])](./removeallocations%28_%29.md)
  Stages multiple resources to leave the residency set’s list of allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresidencyset/removeallallocations())*