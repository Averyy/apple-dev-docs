# allowedComputeUnitKinds

**Framework**: Core AI  
**Kind**: property

The set of compute units the specialized model can use.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var allowedComputeUnitKinds: Set<ComputeUnitKind> { get }
```

#### Discussion

The model may use all or any subset of the kinds in this set during inference.

## See Also

- [var preferredComputeUnitKind: ComputeUnitKind?](specializationoptions/preferredcomputeunitkind.md)
  The preferred compute unit kind, if one was specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/specializationoptions/allowedcomputeunitkinds)*