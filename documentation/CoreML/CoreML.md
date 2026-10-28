# Core ML

**Framework**: Core ML  
**Kind**: module  
**Role**: Framework

Integrate machine learning models into your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Overview

Use [Core ML](./CoreML.md) to integrate machine learning models into your app. [Core ML](./CoreML.md) provides a unified representation for all models. Your app uses [Core ML](./CoreML.md) APIs and user data to make predictions, and to train or fine-tune models, all on a person’s device.

![Flow diagram going from left to right. Starting on the left is a Core ML model file icon. Next, in the center is the Core ML framework icon, and on the right is a generic app icon, labeled “your app”.](https://developer.apple.com/tutorials/images/com.apple.coreml/media-3901331@2x.png)

A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data. Models can accomplish a wide variety of tasks that would be difficult or impractical to write in code. For example, you can train a model to categorize photos, or detect specific objects within a photo directly from its pixels.

You build and train a model with the [Create ML app](https://developer.apple.com/machine-learning/create-ml/) bundled with Xcode. Models trained using [Create ML](../CreateML/CreateML.md) are in the [Core ML](./CoreML.md) model format and are ready to use in your app. Alternatively, you can use a wide variety of other machine learning libraries and then use [Core ML Tools](https://coremltools.readme.io) to convert the model into the [Core ML](./CoreML.md) format. Once a model is on a person’s device, you can use [Core ML](./CoreML.md) to retrain or fine-tune it on-device, with that person’s data.

[Core ML](./CoreML.md) optimizes on-device performance by leveraging the CPU, GPU, and Neural Engine while minimizing its memory footprint and power consumption. Running a model strictly on a person’s device removes any need for a network connection, which helps keep a person’s data private and your app responsive.

The framework is the foundation for domain-specific frameworks and functionality. It supports [Vision](../Vision/Vision.md) for analyzing images, [Natural Language](../NaturalLanguage/NaturalLanguage.md) for processing text, [Speech](../Speech/Speech.md) for converting audio to text, and [Sound Analysis](../SoundAnalysis/SoundAnalysis.md) for identifying sounds in audio. [Core ML](./CoreML.md) itself builds on top of low-level primitives like [Accelerate](../Accelerate/Accelerate.md) and [BNNS](../Accelerate/bnns-library.md), as well as [Metal Performance Shaders](../MetalPerformanceShaders/MetalPerformanceShaders.md).

![A block diagram of the machine learning stack. The top layer is a single block labeled “Your app,” which spans the entire width of the block diagram. The second layer has four blocks labeled “Vision,” “Natural Language,” “Speech,” and “Sound Analysis.” The third layer is labeled “Core ML,” which also spans the entire width. The fourth and final layer has two blocks, “Accelerate and BNNS” and “Metal Performance Shaders.”](https://developer.apple.com/tutorials/images/com.apple.coreml/media-3330367@2x.png)

If your app integrates AI models using the latest architectures and inference techniques, see [Core AI](../CoreAI/CoreAI.md).

## Topics

### Core ML models
- [Getting a Core ML Model](./getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](./updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](./integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [class MLModel](./mlmodel.md)
  An encapsulation of all the details of your machine learning model.
- [Model Customization](./model-customization.md)
  Expand and modify your model with new layers.
- [Model Personalization](./model-personalization.md)
  Update your model to adapt to new data.
### Model inputs and outputs
- [Making Predictions with a Sequence of Inputs](./making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.
- [class MLFeatureValue](./mlfeaturevalue.md)
  A generic wrapper around an underlying value and the value’s type.
- [struct MLSendableFeatureValue](./mlsendablefeaturevalue.md)
  A sendable feature value.
- [protocol MLFeatureProvider](./mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.
- [class MLDictionaryFeatureProvider](./mldictionaryfeatureprovider.md)
  A convenience wrapper for the given dictionary of data.
- [protocol MLBatchProvider](./mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLArrayBatchProvider](./mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.
- [class MLModelAsset](./mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.
### App integration
- [Downloading and Compiling a Model on the User’s Device](./downloading-and-compiling-a-model-on-the-user-s-device.md)
  Install Core ML models on the user’s device dynamically at runtime.
- [Model Integration Samples](./model-integration-samples.md)
  Integrate tabular, image, and text classifcation models into your app.
### Model encryption
- [Generating a Model Encryption Key](./generating-a-model-encryption-key.md)
  Create a model encryption key to encrypt a compiled model or model archive.
- [Encrypting a Model in Your App](./encrypting-a-model-in-your-app.md)
  Encrypt your app’s built-in model at compile time by adding a compiler flag.
### Compute devices
- [enum MLComputeDevice](./mlcomputedevice.md)
  Compute devices for framework operations.
- [class MLCPUComputeDevice](./mlcpucomputedevice.md)
  An object that represents a CPU compute device.
- [class MLGPUComputeDevice](./mlgpucomputedevice.md)
  An object that represents a GPU compute device.
- [class MLNeuralEngineComputeDevice](./mlneuralenginecomputedevice.md)
  An object that represents a Neural Engine compute device.
- [protocol MLComputeDeviceProtocol](./mlcomputedeviceprotocol.md)
  An interface that represents a compute device type.
- [MLAllComputeDevices](./mlallcomputedevices.md)
  Returns an array that contains all of the compute devices that are accessible.
### Compute plan
- [class MLComputePlan](./mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.
- [enum MLModelStructure](./mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
- [struct MLComputePolicy](./mlcomputepolicy.md)
  The compute policy determining what compute device, or compute devices, to execute ML workloads on.
- [func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R](./withmltensorcomputepolicy%28_,_%29-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
- [func withMLTensorComputePolicy<Result>(MLComputePolicy, () throws -> Result) rethrows -> Result](./withmltensorcomputepolicy%28_,_%29-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
- [MLComputePlan](./mlcomputeplan-85vdw.md)
  A class describing the plan for executing a model.
- [MLComputePlanCost](./mlcomputeplancost.md)
  A class that represents the estimated cost of executing a layer or operation.
- [MLComputePlanDeviceUsage](./mlcomputeplandeviceusage.md)
  The anticipated compute devices to use for executing a layer or operation.
### Model state
- [class MLState](./mlstate.md)
  Handle to the state buffers.
- [class MLStateConstraint](./mlstateconstraint.md)
  Constraint of a state feature value.
### Model tensor
- [struct MLTensor](./mltensor.md)
  A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.
- [protocol MLTensorScalar](./mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.
- [protocol MLTensorRangeExpression](./mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.
- [func pointwiseMin(_:_:)](./pointwisemin%28_,_%29.md)
  Computes the element-wise minimum of two tensors.
- [func pointwiseMax(_:_:)](./pointwisemax%28_,_%29.md)
  Computes the element-wise minimum between two tensors.
- [func withMLTensorComputePolicy(_:_:)](./withmltensorcomputepolicy%28_,_%29.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
### Model structure
- [enum MLModelStructure](./mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
- [MLModelStructure](./mlmodelstructure-c.class.md)
  A class representing the structure of a model.
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
### Model errors
- [struct MLModelError](./mlmodelerror-swift.struct.md)
  Information about a Core ML model error.
- [MLModelError.Code](./mlmodelerror-swift.struct/code.md)
  Information about a Core ML model error.
- [let MLModelErrorDomain: String](./mlmodelerrordomain.md)
  The domain for Core ML errors.
### Model deployments
- [class MLModelCollection](./mlmodelcollection.md)
  A set of Core ML models from a model deployment.
### Optimization
- [Analyzing a Core ML model’s performance in Xcode](./analyzing-a-core-ml-model-s-performance-in-xcode.md)
  Measure how your model runs on your Mac or a connected device by generating a performance report in Xcode.
- [MLOptimizationHints](./mloptimizationhints-c.class.md)
  MLOptimizationHints
### Reference
- [CoreML Enumerations](./coreml-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreML)*