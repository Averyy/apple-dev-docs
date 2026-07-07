# ComputeUnitKind

**Framework**: Core AI  
**Kind**: enum

A type of hardware compute unit available for model inference.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum ComputeUnitKind
```

#### Overview

You use compute unit kinds with [`SpecializationOptions`](specializationoptions.md) to control which hardware the framework targets when specializing a model. By default, specialization uses all available compute units on the device.

## Topics

### Defining compute unit types
- [ComputeUnitKind.cpu](computeunitkind/cpu.md)
  The central processing unit.
- [ComputeUnitKind.gpu](computeunitkind/gpu.md)
  The graphics processing unit.
- [ComputeUnitKind.neuralEngine](computeunitkind/neuralengine.md)
  The Neural Engine.
### Checking availability
- [static var availableKinds: Set<ComputeUnitKind>](computeunitkind/availablekinds.md)
  The compute unit kinds available on the current device.

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
- [struct SpecializationOptions](specializationoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/computeunitkind)*