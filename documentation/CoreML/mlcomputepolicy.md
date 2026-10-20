# MLComputePolicy

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

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

### Compute policies
- [static var cpuAndGPU: MLComputePolicy](./mlcomputepolicy/cpuandgpu.md)
  Execute ML workloads using the GPU if available, otherwise falling back to the CPU.
- [static var cpuOnly: MLComputePolicy](./mlcomputepolicy/cpuonly.md)
  Execute ML workloads using the CPU.
### Creating a compute policy
- [init(MLComputeUnits)](./mlcomputepolicy/init%28_%29.md)
  Creates a new compute policy using the given compute units.
### Default Implementations
- [CustomReflectable Implementations](./mlcomputepolicy/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./mlcomputepolicy/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Compute plan
- [class MLComputePlan](./mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.
- [enum MLModelStructure](./mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
- [func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R](./withmltensorcomputepolicy%28_,_%29-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
- [func withMLTensorComputePolicy<Result>(MLComputePolicy, () throws -> Result) rethrows -> Result](./withmltensorcomputepolicy%28_,_%29-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputepolicy)*