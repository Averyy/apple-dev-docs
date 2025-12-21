# MLParameterKey

**Framework**: Core ML  
**Kind**: class

The keys for the parameter dictionary in a model configuration or a model update context.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class MLParameterKey
```

#### Overview

Use an [`MLParameterKey`](mlparameterkey.md) to retrieve a model’s parameter value using:

- The model’s [`parameterValue(for:)`](mlmodel/parametervalue(for:).md) method
- The [`parameters`](mlmodelconfiguration/parameters.md) dictionary of an [`MLModelConfiguration`](mlmodelconfiguration.md)
- The [`parameters`](mlupdatecontext/parameters.md) dictionary of an [`MLUpdateContext`](mlupdatecontext.md)

> **Note**:  To access the parameter of a specific model within a pipeline model, use the parameter key’s [`scoped(to:)`](mlparameterkey/scoped(to:).md) method with the model’s name.

##### Overriding Model and Layer Parameters

To override a model’s default parameter values:

1. Create an [`MLModelConfiguration`](mlmodelconfiguration.md) instance.
2. Use an [`MLParameterKey`](mlparameterkey.md) for each parameter to set its value in the model configuration’s [`parameters`](mlmodelconfiguration/parameters.md) dictionary.
3. Create a new model instance using [`init(contentsOf:configuration:)`](mlmodel/init(contentsof:configuration:).md) with your custom model configuration.

##### Configuring Update Parameters

To configure the update parameters for an [`MLUpdateTask`](mlupdatetask.md):

1. Create an [`MLModelConfiguration`](mlmodelconfiguration.md) instance.
2. Use an [`MLParameterKey`](mlparameterkey.md) for each parameter to set its value in the model configuration’s [`parameters`](mlmodelconfiguration/parameters.md) dictionary.
3. Create a new update task with your custom model configuration.

See [`Personalizing a Model with On-Device Updates`](personalizing-a-model-with-on-device-updates.md).

## Topics

### Scoping parameter keys
- [func scoped(to: String) -> MLParameterKey](mlparameterkey/scoped(to:).md)
  Creates a copy of a parameter key and adds the scope to it.
### Accessing model parameters
- [class var numberOfNeighbors: MLParameterKey](mlparameterkey/numberofneighbors.md)
  The key you use to access the number of neighbors that adjusts the affinity of a k-nearest-neighbor model.
- [class var linkedModelFileName: MLParameterKey](mlparameterkey/linkedmodelfilename.md)
  The key you use to access the linked model’s filename.
- [class var linkedModelSearchPath: MLParameterKey](mlparameterkey/linkedmodelsearchpath.md)
  The key you use to access the linked model’s search path.
### Accessing neural network layer parameters
- [class var weights: MLParameterKey](mlparameterkey/weights.md)
  The key you use to access the weights of a layer in a neural network model.
- [class var biases: MLParameterKey](mlparameterkey/biases.md)
  The key you use to access the biases of a layer in a neural network model.
### Accessing model update parameters
- [class var learningRate: MLParameterKey](mlparameterkey/learningrate.md)
  The key you use to access the optimizer’s learning rate parameter.
- [class var momentum: MLParameterKey](mlparameterkey/momentum.md)
  The key you use to access the stochastic gradient descent (SGD) optimizer’s momentum parameter.
- [class var miniBatchSize: MLParameterKey](mlparameterkey/minibatchsize.md)
  The key you use to access the optimizer’s mini batch-size parameter.
- [class var beta1: MLParameterKey](mlparameterkey/beta1.md)
  The key you use to access the Adam optimizer’s first beta parameter.
- [class var beta2: MLParameterKey](mlparameterkey/beta2.md)
  The key you use to access the Adam optimizer’s second beta parameter.
- [class var eps: MLParameterKey](mlparameterkey/eps.md)
  The key you use to access the Adam optimizer’s epsilon parameter.
- [class var epochs: MLParameterKey](mlparameterkey/epochs.md)
  The key you use to access the optimizer’s epochs parameter.
- [class var shuffle: MLParameterKey](mlparameterkey/shuffle.md)
  The key you use to access the shuffle parameter, a Boolean value that determines whether the model randomizes the data between epochs.
- [class var seed: MLParameterKey](mlparameterkey/seed.md)
  The key you use to access the seed parameter that initializes the random number generator for the shuffle option.

## Relationships

### Inherits From
- [MLKey](mlkey.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlparameterkey)*