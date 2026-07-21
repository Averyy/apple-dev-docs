# preferredComputeUnitKind

**Framework**: Core AI  
**Kind**: property

The preferred compute unit kind, if one was specified.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var preferredComputeUnitKind: ComputeUnitKind? { get }
```

#### Discussion

When set, the specialization process maximizes use of this compute unit kind. Fallback to other kinds in [`allowedComputeUnitKinds`](specializationoptions/allowedcomputeunitkinds.md) may still occur for operations or operation patterns that are incompatible with the preferred kind. Operation patterns refer to groups of operations that are fused or transformed together during specialization; an operation that is individually compatible with the preferred unit kind may be part of a fused pattern that is not.

## See Also

- [var allowedComputeUnitKinds: Set<ComputeUnitKind>](specializationoptions/allowedcomputeunitkinds.md)
  The set of compute units the specialized model can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/specializationoptions/preferredcomputeunitkind)*