# MLModelStructure

**Framework**: Core ML  
**Kind**: enum

An enum representing the structure of a model.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.0+
- watchOS 10.4+

## Declaration

```swift
enum MLModelStructure
```

#### Overview

```None
// Load the model structure.
let modelStructure = await try MLModelStructure.load(contentsOf: modelURL)
switch modelStructure {
case .program(let program):
   // Examine ML Program model.
case .neuralNetwork(let neuralNetwork):
   // Examine Neural network model
case .pipeline(let pipeline)
   // Examine Pipeline model
default:
   // The model type is something else.
}
```

## Topics

### Enumeration Cases
- [case neuralNetwork(MLModelStructure.NeuralNetwork)](mlmodelstructure-swift.enum/neuralnetwork(_:).md)
- [case pipeline(MLModelStructure.Pipeline)](mlmodelstructure-swift.enum/pipeline(_:).md)
- [case program(MLModelStructure.Program)](mlmodelstructure-swift.enum/program(_:).md)
- [MLModelStructure.unsupported](mlmodelstructure-swift.enum/unsupported.md)
### Type Methods
- [static func load(asset: MLModelAsset) async throws -> MLModelStructure](mlmodelstructure-swift.enum/load(asset:).md)
- [static func load(contentsOf: URL) async throws -> MLModelStructure](mlmodelstructure-swift.enum/load(contentsof:).md)
### Structures
- [MLModelStructure.NeuralNetwork](mlmodelstructure-swift.enum/neuralnetwork.md)
- [MLModelStructure.Pipeline](mlmodelstructure-swift.enum/pipeline.md)
- [MLModelStructure.Program](mlmodelstructure-swift.enum/program.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MLComputePlan](mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.
- [struct MLComputePolicy](mlcomputepolicy.md)
  The compute policy determining what compute device, or compute devices, to execute ML workloads on.
- [func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R](withmltensorcomputepolicy(_:_:)-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
- [func withMLTensorComputePolicy<Result>(MLComputePolicy, () throws -> Result) rethrows -> Result](withmltensorcomputepolicy(_:_:)-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-swift.enum)*