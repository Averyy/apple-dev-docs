# MLModel

**Framework**: Core ML  
**Kind**: class  
**Role**: Class

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

```objc
@interface MLModel : NSObject
```

## Mentions

- [Downloading and Compiling a Model on the User’s Device](./downloading-and-compiling-a-model-on-the-user-s-device.md)
- [Encrypting a Model in Your App](./encrypting-a-model-in-your-app.md)

## Overview

[`MLModel`](./mlmodel.md) encapsulates a model’s prediction methods, configuration, and model description.

In most cases, you can use Core ML without accessing the [`MLModel`](./mlmodel.md) class directly. Instead, use the programmer-friendly wrapper class that Xcode automatically generates when you add a model (see [Integrating a Core ML Model into Your App](./integrating-a-core-ml-model-into-your-app.md)). If your app needs the [`MLModel`](./mlmodel.md) interface, use the wrapper class’s `model` property.

With the [`MLModel`](./mlmodel.md) interface, you can:

- Make a prediction with your app’s custom [`MLFeatureProvider`](./mlfeatureprovider.md) by calling [`prediction(from:)`](./mlmodel/prediction%28from%29-9y2aa.md) or [`prediction(from:options:)`](./mlmodel/prediction%28from,options%29-81mr6.md).
- Make multiple predictions with your app’s custom [`MLBatchProvider`](./mlbatchprovider.md) by calling [`predictions(fromBatch:)`](./mlmodel/predictions%28frombatch%29.md) or [`predictions(from:options:)`](./mlmodel/predictions%28from,options%29.md).
- Inspect your model’s [`metadata`](./mlmodeldescription/metadata.md) and [`MLFeatureDescription`](./mlfeaturedescription.md) instances through [`modelDescription`](./mlmodel/modeldescription.md).

If your app downloads and compiles a model on the user’s device, you must use the [`MLModel`](./mlmodel.md) class directly to make predictions. See [Downloading and Compiling a Model on the User’s Device](./downloading-and-compiling-a-model-on-the-user-s-device.md).

> ❗ **Important**:  Use an [`MLModel`](./mlmodel.md) instance on one thread or one dispatch queue at a time. Do this by either serializing method calls to the model, or by creating a separate model instance for each thread and dispatch queue.

## Topics

### Loading a model
- [class func load(contentsOf: URL, configuration: MLModelConfiguration) async throws -> MLModel](./mlmodel/load%28contentsof,configuration%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(MLModelAsset, configuration: MLModelConfiguration, completionHandler: (MLModel?, (any Error)?) -> Void)](./mlmodel/load%28_,configuration,completionhandler%29.md)
  Construct a model asynchronously from a compiled model asset.
- [class func load(contentsOf: URL, configuration: MLModelConfiguration, completionHandler: (Result<MLModel, any Error>) -> Void)](./mlmodel/load%28contentsof,configuration,completionhandler%29.md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [convenience init(contentsOf: URL) throws](./mlmodel/init%28contentsof%29.md)
  Creates a Core ML model instance from a compiled model file.
- [convenience init(contentsOf: URL, configuration: MLModelConfiguration) throws](./mlmodel/init%28contentsof,configuration%29.md)
  Creates a Core ML model instance from a compiled model file and a custom configuration.
- [convenience init(contentsOfURL: URL) throws](./mlmodel/init%28contentsofurl%29.md)
- [convenience init(contentsOfURL: URL, configuration: MLModelConfiguration) throws](./mlmodel/init%28contentsofurl,configuration%29.md)
- [+ loadContentsOfURL:configuration:completionHandler:](./mlmodel/loadcontentsofurl_configuration_completionhandler_.md)
  Creates a Core ML model instance asynchronously from a compiled model file, a custom configuration, and a completion handler.
- [- predictionFromFeatures:completionHandler:](./mlmodel/predictionfromfeatures_completionhandler_.md)
  Generates a prediction asynchronously from the feature values within the input feature provider.
- [- predictionFromFeatures:options:completionHandler:](./mlmodel/predictionfromfeatures_options_completionhandler_.md)
  Generates a prediction asynchronously from the feature values within the input feature provider using the prediction options.
- [- predictionFromFeatures:usingState:options:completionHandler:](./mlmodel/predictionfromfeatures_usingstate_options_completionhandler_.md)
  Run a stateful prediction asynchronously.
### Compiling a model
- [class compileModel(at:)](./mlmodel/compilemodel%28at%29.md)
- [class func compileModel(at: URL, completionHandler: (Result<URL, any Error>) -> Void)](./mlmodel/compilemodel%28at,completionhandler%29.md)
  Compile a model for a device.
### Making predictions
- [func prediction(from:)](./mlmodel/prediction%28from%29.md)
- [func prediction(from:options:)](./mlmodel/prediction%28from,options%29.md)
- [func predictions(fromBatch: any MLBatchProvider) throws -> any MLBatchProvider](./mlmodel/predictions%28frombatch%29.md)
  Generates predictions for each input feature provider within the batch provider.
- [func predictions(from: any MLBatchProvider, options: MLPredictionOptions) throws -> any MLBatchProvider](./mlmodel/predictions%28from,options%29.md)
  Generates a prediction for each input feature provider within the batch provider using the prediction options.
- [func prediction(from:using:)](./mlmodel/prediction%28from,using%29.md)
- [func prediction(from:using:options:)](./mlmodel/prediction%28from,using,options%29.md)
- [class MLPredictionOptions](./mlpredictionoptions.md)
  The options available when making a prediction.
- [Background Inference](../BundleResources/entitlements/com.apple.developer.background-tasks.continued-processing.inference.md)
  An entitlement that lets a background task run inference on the Neural Engine.
### Making state
- [func makeState() -> MLState](./mlmodel/makestate%28%29.md)
  Creates a new state object.
- [- newState](./mlmodel/newstate.md)
  Creates a new state object.
### Inspecting a model
- [static var availableComputeDevices: [MLComputeDevice]](./mlmodel/availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.
- [var configuration: MLModelConfiguration](./mlmodel/configuration.md)
  The configuration of the model set during initialization.
- [var modelDescription: MLModelDescription](./mlmodel/modeldescription.md)
  Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.
- [class MLModelDescription](./mlmodeldescription.md)
  Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.
- [func parameterValue(for: MLParameterKey) throws -> Any](./mlmodel/parametervalue%28for%29.md)
  Returns a model parameter value for a key.
- [class MLParameterKey](./mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.
- [availableComputeDevices](./mlmodel/availablecomputedevices-42uzt.md)
  The list of available compute devices that the model’s prediction can use.
### Supporting types
- [class MLModelConfiguration](./mlmodelconfiguration.md)
  The settings for creating or updating a machine learning model.
- [struct MLOptimizationHints](./mloptimizationhints-swift.struct.md)
- [class MLKey](./mlkey.md)
  An abstract base class for machine learning key types.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Core ML models
- [Getting a Core ML Model](./getting-a-core-ml-model.md)
  Obtain a Core ML model to use in your app.
- [Updating a Model File to a Model Package](./updating-a-model-file-to-a-model-package.md)
  Convert a Core ML model file into a model package in Xcode.
- [Integrating a Core ML Model into Your App](./integrating-a-core-ml-model-into-your-app.md)
  Add a simple model to an app, pass input data to the model, and process the model’s predictions.
- [Model Customization](./model-customization.md)
  Expand and modify your model with new layers.
- [Model Personalization](./model-personalization.md)
  Update your model to adapt to new data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel)*