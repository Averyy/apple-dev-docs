# MLComputePlan

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

A class describing the plan for executing a model.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```objc
@interface MLComputePlan : NSObject
```

#### Overview

The application can use the plan to estimate the necessary cost and resources of the model before running the predictions.

```
// Load the compute plan of an ML Program model.
[MLComputePlan loadContentsOfURL:modelURL configuration:configuration completionHandler:^(MLComputePlan * _Nullable computePlan, NSError * _Nullable error) {
   if (!computePlan) {
       // Handle error.
       return;
   }
   MLModelStructureProgram *program = computePlan.modelStructure.program;
   if (!program) {
       [NSException raise:NSInternalInconsistencyException format:@"Unexpected model type."];
   }

   MLModelStructureFunction *mainFunction = program.functions["main"];
   if (!mainFunction) {
       [NSException raise:NSInternalInconsistencyException format:@"Missing main function."];
   }

   NSArray<MLModelStructureProgramOperation *> *operations = mainFunction.block.operations;
   for (MLModelStructureProgramOperation *operation in operations) {
       // Get the compute device usage for the operation.
       MLComputeDeviceUsage *computeDeviceUsage = [computePlan computeDeviceUsageForMLProgramOperation:operation];
       // Get the estimated cost of executing the operation.
       MLComputePlanCost *estimatedCost = [computePlan estimatedCostOfMLProgramOperation:operation];

   }
}];
```

## Topics

### Loading a compute plan
- [+ loadContentsOfURL:configuration:completionHandler:](./mlcomputeplan-85vdw/loadcontentsofurl_configuration_completionhandler_.md)
  Construct the compute plan of a model asynchronously given the location of its on-disk representation.
- [+ loadModelAsset:configuration:completionHandler:](./mlcomputeplan-85vdw/loadmodelasset_configuration_completionhandler_.md)
  Construct the compute plan of a model asynchronously given the model asset.
### Getting the model structure
- [modelStructure](./mlcomputeplan-85vdw/modelstructure.md)
  The model structure.
### Getting the device usage
- [- computeDeviceUsageForMLProgramOperation:](./mlcomputeplan-85vdw/computedeviceusageformlprogramoperation_.md)
  Returns The anticipated compute devices that would be used for executing an ML Program operation.
- [- computeDeviceUsageForNeuralNetworkLayer:](./mlcomputeplan-85vdw/computedeviceusageforneuralnetworklayer_.md)
  Returns the anticipated compute devices that would be used for executing a NeuralNetwork layer.
- [MLComputePlanDeviceUsage](./mlcomputeplandeviceusage.md)
  The anticipated compute devices to use for executing a layer or operation.
### Getting the estimated cost
- [- estimatedCostOfMLProgramOperation:](./mlcomputeplan-85vdw/estimatedcostofmlprogramoperation_.md)
  Returns the estimated cost of executing an ML Program operation.
- [MLComputePlanCost](./mlcomputeplancost.md)
  A class that represents the estimated cost of executing a layer or operation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Compute plan
- [MLComputePlanCost](./mlcomputeplancost.md)
  A class that represents the estimated cost of executing a layer or operation.
- [MLComputePlanDeviceUsage](./mlcomputeplandeviceusage.md)
  The anticipated compute devices to use for executing a layer or operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlcomputeplan-85vdw)*