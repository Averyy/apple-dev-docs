# MLModelStructure

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

A class representing the structure of a model.

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
@interface MLModelStructure : NSObject
```

## Overview

```
// Load the model structure.
[MLModelStructure loadContentsOfURL:modelURL completionHandler:^(MLModelStructure * _Nullable modelStructure, NSError * _Nullable error) {
   if (!modelStructure) {
       // Handle error.
       return;
   }
   if (modelStructure.neuralNetwork) {
       // Examine Neural network model.
   } else if (modelStructure.program) {
       // Examine ML Program model.
   } else if (modelStructure.pipeline) {
       // Examine Pipeline model.
   } else {
       // The model type is something else.
   }
}];
```

## Topics

### Model structures
- [neuralNetwork](./mlmodelstructure-c.class/neuralnetwork.md)
  If the model is of NeuralNetwork type then it is the structure of the NeuralNetwork otherwise `nil`.
- [pipeline](./mlmodelstructure-c.class/pipeline.md)
  If the model is of Pipeline type then it is the structure of the Pipeline otherwise `nil`.
- [program](./mlmodelstructure-c.class/program.md)
  If the model is of ML Program type then it is the structure of the ML Program otherwise `nil`.
### Loading a model structure
- [+ loadContentsOfURL:completionHandler:](./mlmodelstructure-c.class/loadcontentsofurl_completionhandler_.md)
  Construct the model structure asynchronously given the location of its on-disk representation.
- [+ loadModelAsset:completionHandler:](./mlmodelstructure-c.class/loadmodelasset_completionhandler_.md)
  Construct the model structure asynchronously  given the model asset.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Model structure
- [MLModelStructureNeuralNetwork](./mlmodelstructureneuralnetwork.md)
  A class representing the structure of a NeuralNetwork model.
- [MLModelStructureNeuralNetworkLayer](./mlmodelstructureneuralnetworklayer.md)
  A class representing a layer in a NeuralNetwork.
- [MLModelStructurePipeline](./mlmodelstructurepipeline.md)
  A class representing the structure of a Pipeline model.
- [MLModelStructureProgram](./mlmodelstructureprogram.md)
  A class representing the structure of an ML Program model.
- [MLModelStructureProgramArgument](./mlmodelstructureprogramargument.md)
  A class representing an argument in the Program.
- [MLModelStructureProgramBinding](./mlmodelstructureprogrambinding.md)
  A class representing a binding in the Program
- [MLModelStructureProgramBlock](./mlmodelstructureprogramblock.md)
  A class representing a block in the Program.
- [MLModelStructureProgramFunction](./mlmodelstructureprogramfunction.md)
  A class representing a function in the Program.
- [MLModelStructureProgramNamedValueType](./mlmodelstructureprogramnamedvaluetype.md)
  A class representing a named value type in a Program.
- [MLModelStructureProgramOperation](./mlmodelstructureprogramoperation.md)
  A class representing an Operation in a Program.
- [MLModelStructureProgramValue](./mlmodelstructureprogramvalue.md)
  A class representing a constant value in the Program.
- [MLModelStructureProgramValueType](./mlmodelstructureprogramvaluetype.md)
  A class representing the type of a value or a variable in the Program.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodelstructure-c.class)*