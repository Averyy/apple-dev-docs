# allowedComputeUnitKinds

**Framework**: Core AI  
**Kind**: property

The set of compute units the specialized model can use.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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