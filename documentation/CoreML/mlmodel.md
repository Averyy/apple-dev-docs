# MLModel

**Framework**: Core ML  
**Kind**: class

An encapsulation of all the details of your machine learning model.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class MLModel
```

## Mentions

- [Downloading and Compiling a Model on the User’s Device](downloading-and-compiling-a-model-on-the-user-s-device.md)
- [Encrypting a Model in Your App](encrypting-a-model-in-your-app.md)

#### Overview

[`MLModel`](mlmodel.md) encapsulates a model’s prediction methods, configuration, and model description.

In most cases, you can use Core ML without accessing the [`MLModel`](mlmodel.md) class directly. Instead, use the programmer-friendly wrapper class that Xcode automatically generates when you add a model (see [`Integrating a Core ML Model into Your App`](integrating-a-core-ml-model-into-your-app.md)). If your app needs the [`MLModel`](mlmodel.md) interface, use the wrapper class’s `model` property.

With the [`MLModel`](mlmodel.md) interface, you can:

- Make a prediction with your app’s custom [`MLFeatureProvider`](mlfeatureprovider.md) by calling [`prediction(from:)`](mlmodel/prediction(from:)-9y2aa.md) or [`prediction(from:options:)`](mlmodel/prediction(from:options:)-81mr6.md).
- Make multiple predictions with your app’s custom [`MLBatchProvider`](mlbatchprovider.md) by calling [`predictions(fromBatch:)`](mlmodel/predictions(frombatch:).md) or [`predictions(from:options:)`](mlmodel/predictions(from:options:).md).
- Inspect your model’s [`metadata`](mlmodeldescription/metadata.md) and [`MLFeatureDescription`](mlfeaturedescription.md) instances through [`modelDescription`](mlmodel/modeldescription.md).

If your app downloads and compiles a model on the user’s device, you must use the [`MLModel`](mlmodel.md) class directly to make predictions. See [`Downloading and Compiling a Model on the User’s Device`](downloading-and-compiling-a-model-on-the-user-s-device.md).

> ❗ **Important**:  Use an [`MLModel`](mlmodel.md) instance on one thread or one dispatch queue at a time. Do this by either serializing method calls to the model, or by creating a separate model instance for each thread and dispatch queue.

## Topics

### Loading a Model
- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](mlmodel/load(contentsof:configuration:).md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](mlmodel/load(_:configuration:completionhandler:).md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(contentsOf: URL, configuration: MLModelConfiguration, completionHandler: (Result<MLModel, any Error>) -> Void)](mlmodel/load(contentsof:configuration:completionhandler:).md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [convenience init(contentsOf: URL) throws](mlmodel/init(contentsof:).md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](mlmodel/init(contentsof:configuration:).md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](mlmodel/init(contentsofurl:).md)
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](mlmodel/init(contentsofurl:configuration:).md)
### Compiling a Model
- [class func compileModel(at: URL) async throws -> URL](mlmodel/compilemodel(at:)-45ao6.md)
  Compile a model for a device.
- [class func compileModel(at: URL, completionHandler: (Result<URL, any Error>) -> Void)](mlmodel/compilemodel(at:completionhandler:).md)
  Compile a model for a device.
- [class func compileModel(at: URL) async throws -> URL](mlmodel/compilemodel(at:)-3nea.md)
  Compile a model for a device.
- [class func compileModel(at: URL) throws -> URL](mlmodel/compilemodel(at:)-6442s.md)
  Compiles a model on the device to update the model in your app.
### Making Predictions
- [func prediction(from: any MLFeatureProvider) throws -> any MLFeatureProvider](mlmodel/prediction(from:)-9y2aa.md)
  Generates a prediction from the feature values within the input feature provider.
- [func prediction(from: [String : MLTensor]) async throws -> [String : MLTensor]](mlmodel/prediction(from:)-7vsm8.md)
  Run a prediction on a model.
- [func prediction(from: any MLFeatureProvider, options: MLPredictionOptions) throws -> any MLFeatureProvider](mlmodel/prediction(from:options:)-81mr6.md)
  Generates a prediction from the feature values within the input feature provider using the prediction options.
- [func prediction(from: any MLFeatureProvider, options: MLPredictionOptions) async throws -> any MLFeatureProvider](mlmodel/prediction(from:options:)-3vg03.md)
  Generates a prediction asynchronously from the feature values within the input feature provider using the prediction options.
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](mlmodel/predictions(frombatch:).md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](mlmodel/predictions(from:options:).md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from: [String : MLTensor], using: MLState) async throws -> [String : MLTensor]](mlmodel/prediction(from:using:)-6whkh.md)
  Run a stateful prediction on a model.
- [func prediction(from: any MLFeatureProvider, using: MLState) throws -> any MLFeatureProvider](mlmodel/prediction(from:using:)-97bu1.md)
  Run a stateful prediction synchronously.
- [func prediction(from: any MLFeatureProvider, using: MLState, options: MLPredictionOptions) async throws -> any MLFeatureProvider](mlmodel/prediction(from:using:options:)-8b4qa.md)
  Run a stateful prediction on a model asynchronously.
- [func prediction(from: any MLFeatureProvider, using: MLState, options: MLPredictionOptions) throws -> any MLFeatureProvider](mlmodel/prediction(from:using:options:)-v4wp.md)
  Run a stateful prediction synchronously with options.
- [class MLPredictionOptions](mlpredictionoptions.md)
  The options available when making a prediction.
### Inspecting a Model
- [static var availableComputeDevices: [MLComputeDevice]](mlmodel/availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.
- [var configuration: MLModelConfiguration](mlmodel/configuration.md)
  The configuration of the model set during initialization.
- [var modelDescription: MLModelDescription](mlmodel/modeldescription.md)
  Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.
- [class MLModelDescription](mlmodeldescription.md)
  Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.
- [func parameterValue(for: MLParameterKey) throws -> Any](mlmodel/parametervalue(for:).md)
  Returns a model parameter value for a key.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.
### Supporting Types
- [class MLModelConfiguration](mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [struct MLOptimizationHints](mloptimizationhints-swift.struct.md)
- [class MLKey](mlkey.md)
  An abstract base class for machine learning key types.
### Instance Methods
- [func makeState() -> MLState](mlmodel/makestate.md)
  Creates a new state object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Getting a Core ML Model](getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [Model Customization](model-customization.md)
  Expand and modify your model with new layers.
- [Model Personalization](model-personalization.md)
  Update your model to adapt to new data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel)*