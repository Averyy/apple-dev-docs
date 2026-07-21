# SpecializationOptions

**Framework**: Core AI  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct SpecializationOptions
```

## Mentions

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)

## Topics

### Using preset options
- [static let `default`: SpecializationOptions](specializationoptions/default.md)
  Options that allow the model to use all available compute units.
- [static let cpuOnly: SpecializationOptions](specializationoptions/cpuonly.md)
  Options that restrict compute to the CPU only.
### Creating custom options
- [init(preferredComputeUnitKind: ComputeUnitKind)](specializationoptions/init(preferredcomputeunitkind:).md)
  Creates options with a preferred compute unit kind.
### Configuring compute units
- [var allowedComputeUnitKinds: Set<ComputeUnitKind>](specializationoptions/allowedcomputeunitkinds.md)
  The set of compute units the specialized model can use.
- [var preferredComputeUnitKind: ComputeUnitKind?](specializationoptions/preferredcomputeunitkind.md)
  The preferred compute unit kind, if one was specified.
### Configuring specialization behavior
- [var expectFrequentReshapes: Bool](specializationoptions/expectfrequentreshapes.md)
  Setting to allow more optimal specialization if the model performs frequent reshapes based on usage

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Managing model specialization and caching](managing-model-specialization-and-caching.md)
  Configure model specialization, manage cached assets, and reduce your app’s storage footprint.
- [Compiling Core AI models ahead of time](compiling-core-ai-models-ahead-of-time.md)
  Reduce on-device specialization time by compiling Core AI models at build time.
- [class AIModelCache](aimodelcache.md)
  A cache that stores the specialized model artifacts for inference.
- [enum ComputeUnitKind](computeunitkind.md)
  A type of hardware compute unit available for model inference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/specializationoptions)*