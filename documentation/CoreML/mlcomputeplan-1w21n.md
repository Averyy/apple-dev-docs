# MLComputePlan

**Framework**: Core ML  
**Kind**: class

A class representing the compute plan of a model.

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
class MLComputePlan
```

#### Overview

The application can use the compute plan to estimate the necessary cost and resources of the model before running the predictions.

```None
// Load the compute plan of an ML Program model.
let computePlan = try await MLComputePlan.load(contentsOf: modelURL, configuration: configuration)
guard case let .program(program) = computePlan.modelStructure else {
   fatalError("Unexpected model type.")
}
 // Get the main function.
guard let mainFunction = program.functions["main"] else {
   fatalError("Missing main function.")
}

let operations = mainFunction.block.operations
for operation in operations {
   // Get the compute device usage for the operation.
   let computeDeviceUsage = computePlan.deviceUsage(for: operation)
   // Get the estimated cost of executing the operation.
   let estimatedCost = computePlan.estimatedCost(of: operation)
}
```

## Topics

### Instance Properties
- [let modelStructure: MLModelStructure](mlcomputeplan-1w21n/modelstructure.md)
- [modelStructure](mlcomputeplan-85vdw/modelstructure.md)
### Instance Methods
- [func deviceUsage(for: MLModelStructure.NeuralNetwork.Layer) -> MLComputePlan.DeviceUsage?](mlcomputeplan-1w21n/deviceusage(for:)-9em1q.md)
- [func deviceUsage(for: MLModelStructure.Program.Operation) -> MLComputePlan.DeviceUsage?](mlcomputeplan-1w21n/deviceusage(for:)-7cdlm.md)
- [func estimatedCost(of: MLModelStructure.Program.Operation) -> MLComputePlan.Cost?](mlcomputeplan-1w21n/estimatedcost(of:).md)
- [- computeDeviceUsageForMLProgramOperation:](mlcomputeplan-85vdw/computedeviceusageformlprogramoperation:.md)
- [- computeDeviceUsageForNeuralNetworkLayer:](mlcomputeplan-85vdw/computedeviceusageforneuralnetworklayer:.md)
- [- estimatedCostOfMLProgramOperation:](mlcomputeplan-85vdw/estimatedcostofmlprogramoperation:.md)
### Type Methods
- [static func load(asset: MLModelAsset, configuration: MLModelConfiguration) async throws -> MLComputePlan](mlcomputeplan-1w21n/load(asset:configuration:).md)
- [static func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLComputePlan](mlcomputeplan-1w21n/load(contentsof:configuration:).md)
### Structures
- [MLComputePlan.Cost](mlcomputeplan-1w21n/cost.md)
- [MLComputePlan.DeviceUsage](mlcomputeplan-1w21n/deviceusage.md)
- [+ loadContentsOfURL:configuration:completionHandler:](mlcomputeplan-85vdw/loadcontentsofurl:configuration:completionhandler:.md)
- [+ loadModelAsset:configuration:completionHandler:](mlcomputeplan-85vdw/loadmodelasset:configuration:completionhandler:.md)

## See Also

- [enum MLModelStructure](mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
- [struct MLComputePolicy](mlcomputepolicy.md)
  The compute policy determining what compute device, or compute devices, to execute ML workloads on.
- [func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R](withmltensorcomputepolicy(_:_:)-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
- [func withMLTensorComputePolicy<Result>(MLComputePolicy, () throws -> Result) rethrows -> Result](withmltensorcomputepolicy(_:_:)-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-1w21n)*