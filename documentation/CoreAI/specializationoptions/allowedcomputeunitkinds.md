# allowedComputeUnitKinds

**Framework**: Core AI  
**Kind**: property

The set of compute units the specialized model can use.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var allowedComputeUnitKinds: Set<ComputeUnitKind> { get }
```

#### Discussion

The model may use all or any subset of the kinds in this set during inference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/specializationoptions/allowedcomputeunitkinds)*