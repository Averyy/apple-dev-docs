# Core ML

**Framework**: Core ML  
**Kind**: module

Integrate machine learning models into your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

#### Overview

Use [`Core ML`](CoreML.md) to integrate machine learning models into your app. [`Core ML`](CoreML.md) provides a unified representation for all models. Your app uses [`Core ML`](CoreML.md) APIs and user data to make predictions, and to train or fine-tune models, all on a person’s device.

![Flow diagram going from left to right. Starting on the left is a Core ML model file icon. Next, in the center is the Core ML framework icon, and on the right is a generic app icon, labeled “your app”.](https://docs-assets.developer.apple.com/published/ae17ffa70ecbce075dc4b57539ec6dde/media-3901331%402x.png)

A model is the result of applying a machine learning algorithm to a set of training data. You use a model to make predictions based on new input data. Models can accomplish a wide variety of tasks that would be difficult or impractical to write in code. For example, you can train a model to categorize photos, or detect specific objects within a photo directly from its pixels.

You build and train a model with the [`Create ML app`](https://developer.apple.comhttps://developer.apple.com/machine-learning/create-ml/) bundled with Xcode. Models trained using [`Create ML`](https://developer.apple.com/documentation/CreateML) are in the [`Core ML`](CoreML.md) model format and are ready to use in your app. Alternatively, you can use a wide variety of other machine learning libraries and then use [`Core ML Tools`](https://developer.apple.comhttps://coremltools.readme.io) to convert the model into the [`Core ML`](CoreML.md) format. Once a model is on a person’s device, you can use [`Core ML`](CoreML.md) to retrain or fine-tune it on-device, with that person’s data.

[`Core ML`](CoreML.md) optimizes on-device performance by leveraging the CPU, GPU, and Neural Engine while minimizing its memory footprint and power consumption. Running a model strictly on a person’s device removes any need for a network connection, which helps keep a person’s data private and your app responsive.

The framework is the foundation for domain-specific frameworks and functionality. It supports [`Vision`](https://developer.apple.com/documentation/Vision) for analyzing images, [`Natural Language`](https://developer.apple.com/documentation/NaturalLanguage) for processing text, [`Speech`](https://developer.apple.com/documentation/Speech) for converting audio to text, and [`Sound Analysis`](https://developer.apple.com/documentation/SoundAnalysis) for identifying sounds in audio. [`Core ML`](CoreML.md) itself builds on top of low-level primitives like [`Accelerate`](https://developer.apple.com/documentation/Accelerate) and [`BNNS`](https://developer.apple.com/documentation/Accelerate/bnns-library), as well as [`Metal Performance Shaders`](https://developer.apple.com/documentation/MetalPerformanceShaders).

![A block diagram of the machine learning stack. The top layer is a single block labeled “Your app,” which spans the entire width of the block diagram. The second layer has four blocks labeled “Vision,” “Natural Language,” “Speech,” and “Sound Analysis.” The third layer is labeled “Core ML,” which also spans the entire width. The fourth and final layer has two blocks, “Accelerate and BNNS” and “Metal Performance Shaders.”](https://docs-assets.developer.apple.com/published/2ab0327b082af0332b528cc4171ee629/media-3330367%402x.png)

## Topics

### Core ML models
- [Getting a Core ML Model](getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [class MLModel](mlmodel.md)
  An encapsulation of all the details of your machine learning model.
- [Model Customization](model-customization.md)
  Expand and modify your model with new layers.
- [Model Personalization](model-personalization.md)
  Update your model to adapt to new data.
### Model inputs and outputs
- [Making Predictions with a Sequence of Inputs](making-predictions-with-a-sequence-of-inputs.md)
  Integrate a recurrent neural network model to process sequences of inputs.
- [class MLFeatureValue](mlfeaturevalue.md)
  A generic wrapper around an underlying value and the value’s type.
- [struct MLSendableFeatureValue](mlsendablefeaturevalue.md)
  A sendable feature value.
- [protocol MLFeatureProvider](mlfeatureprovider.md)
  An interface that represents a collection of values for either a model’s input or its output.
- [class MLDictionaryFeatureProvider](mldictionaryfeatureprovider.md)
  A convenience wrapper for the given dictionary of data.
- [protocol MLBatchProvider](mlbatchprovider.md)
  An interface that represents a collection of feature providers.
- [class MLArrayBatchProvider](mlarraybatchprovider.md)
  A convenience wrapper for batches of feature providers.
- [class MLModelAsset](mlmodelasset.md)
  An abstraction of a compiled Core ML model asset.
### App integration
- [Downloading and Compiling a Model on the User’s Device](downloading-and-compiling-a-model-on-the-user-s-device.md)
  Install Core ML models on the user’s device dynamically at runtime.
- [Model Integration Samples](model-integration-samples.md)
  Integrate tabular, image, and text classifcation models into your app.
### Model encryption
- [Generating a Model Encryption Key](generating-a-model-encryption-key.md)
  Create a model encryption key to encrypt a compiled model or model archive.
- [Encrypting a Model in Your App](encrypting-a-model-in-your-app.md)
  Encrypt your app’s built-in model at compile time by adding a compiler flag.
### Compute devices
- [enum MLComputeDevice](mlcomputedevice.md)
  Compute devices for framework operations.
- [class MLCPUComputeDevice](mlcpucomputedevice.md)
  An object that represents a CPU compute device.
- [class MLGPUComputeDevice](mlgpucomputedevice.md)
  An object that represents a GPU compute device.
- [class MLNeuralEngineComputeDevice](mlneuralenginecomputedevice.md)
  An object that represents a Neural Engine compute device.
- [protocol MLComputeDeviceProtocol](mlcomputedeviceprotocol.md)
  An interface that represents a compute device type.
### Compute plan
- [class MLComputePlan](mlcomputeplan-1w21n.md)
  A class representing the compute plan of a model.
- [enum MLModelStructure](mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
- [struct MLComputePolicy](mlcomputepolicy.md)
  The compute policy determining what compute device, or compute devices, to execute ML workloads on.
- [func withMLTensorComputePolicy<R>(MLComputePolicy, () async throws -> R) async rethrows -> R](withmltensorcomputepolicy(_:_:)-8stx9.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
- [func withMLTensorComputePolicy<Result>(MLComputePolicy, () throws -> Result) rethrows -> Result](withmltensorcomputepolicy(_:_:)-6z33x.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
### Model state
- [class MLState](mlstate.md)
  Handle to the state buffers.
- [class MLStateConstraint](mlstateconstraint.md)
  Constraint of a state feature value.
### Model tensor
- [struct MLTensor](mltensor.md)
  A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.
- [protocol MLTensorScalar](mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.
- [protocol MLTensorRangeExpression](mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.
- [func pointwiseMin(_:_:)](pointwisemin(_:_:).md)
  Computes the element-wise minimum of two tensors.
- [func pointwiseMax(_:_:)](pointwisemax(_:_:).md)
  Computes the element-wise minimum between two tensors.
- [func withMLTensorComputePolicy(_:_:)](withmltensorcomputepolicy(_:_:).md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.
### Model structure
- [enum MLModelStructure](mlmodelstructure-swift.enum.md)
  An enum representing the structure of a model.
### Model errors
- [struct MLModelError](mlmodelerror-swift.struct.md)
  Information about a Core ML model error.
- [MLModelError.Code](mlmodelerror-swift.struct/code.md)
  Information about a Core ML model error.
- [let MLModelErrorDomain: String](mlmodelerrordomain.md)
  The domain for Core ML errors.
### Model deployments
- [class MLModelCollection](mlmodelcollection.md)
  A set of Core ML models from a model deployment.
### Reference
- [CoreML Enumerations](coreml-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreML)*