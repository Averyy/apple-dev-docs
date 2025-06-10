# MLComputePolicy

**Framework**: Core ML  
**Kind**: struct

The compute policy determining what compute device, or compute devices, to execute ML workloads on.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MLComputePolicy
```

## Topics

### Initializers
- [init(MLComputeUnits)](mlcomputepolicy/init(_:).md)
  Creates a new compute policy using the given compute units.
### Type Properties
- [static var cpuAndGPU: MLComputePolicy](mlcomputepolicy/cpuandgpu.md)
  Execute ML workloads using the GPU if available, otherwise falling back to the CPU.
- [static var cpuOnly: MLComputePolicy](mlcomputepolicy/cpuonly.md)
  Execute ML workloads using the CPU.
### Default Implementations
- [CustomReflectable Implementations](mlcomputepolicy/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](mlcomputepolicy/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MLComputePlan](mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.
- [enum MLModelStructure](mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
- [func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R](withmltensorcomputepolicy(_:_:)-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
- [func withMLTensorComputePolicy<Result>(MLComputePolicy, () throws -> Result) rethrows -> Result](withmltensorcomputepolicy(_:_:)-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputepolicy)*