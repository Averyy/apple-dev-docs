# init(preferredComputeUnitKind:)

**Framework**: Core AI  
**Kind**: init

Creates options with a preferred compute unit kind.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(preferredComputeUnitKind: ComputeUnitKind)
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

#### Discussion

The specialization process maximizes use of the specified compute unit kind, falling back to other allowed compute units for incompatible operations.

## Parameters

- `preferredComputeUnitKind`: The compute unit kind the specialized model should prefer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/specializationoptions/init(preferredcomputeunitkind:))*