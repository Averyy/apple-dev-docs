# MLModelDescription

**Framework**: Core ML  
**Kind**: class

Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.

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
class MLModelDescription
```

## Topics

### Accessing Feature Descriptions
- [var inputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/inputdescriptionsbyname.md)
  A dictionary of input feature descriptions, which the model keys by the input’s name.
- [var outputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/outputdescriptionsbyname.md)
  A dictionary of output feature descriptions, which the model keys by the output’s name.
- [class MLFeatureDescription](mlfeaturedescription.md)
  The name, type, and constraints of an input or output feature.
### Accessing Metadata
- [var classLabels: [Any]?](mlmodeldescription/classlabels.md)
  An array of labels, which can be either strings or a numbers, for classifier models.
- [var metadata: [MLModelMetadataKey : Any]](mlmodeldescription/metadata.md)
  A dictionary of the model’s creation information, such as its description, author, version, and license.
- [struct MLModelMetadataKey](mlmodelmetadatakey.md)
  The set of keys the model uses to store values in its metadata dictionary.
### Accessing Prediction Names
- [var predictedFeatureName: String?](mlmodeldescription/predictedfeaturename.md)
  The name of the primary prediction feature output description.
- [var predictedProbabilitiesName: String?](mlmodeldescription/predictedprobabilitiesname.md)
  The name of the feature output description for all probabilities of a prediction.
### Accessing Update Descriptions
- [var isUpdatable: Bool](mlmodeldescription/isupdatable.md)
  A Boolean value that indicates whether you can update the model with additional training.
- [var trainingInputDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/traininginputdescriptionsbyname.md)
  A dictionary of the training input feature descriptions, which the model keys by the input’s name.
- [var parameterDescriptionsByKey: [MLParameterKey : MLParameterDescription]](mlmodeldescription/parameterdescriptionsbykey.md)
  A dictionary of the descriptions for the model’s parameters.
- [class MLParameterDescription](mlparameterdescription.md)
  A description of a model parameter that includes a default value and a constraint, if applicable.
### Instance Properties
- [var stateDescriptionsByName: [String : MLFeatureDescription]](mlmodeldescription/statedescriptionsbyname.md)
  Description of the state features.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [static var availableComputeDevices: [MLComputeDevice]](mlmodel/availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.
- [var configuration: MLModelConfiguration](mlmodel/configuration.md)
  The configuration of the model set during initialization.
- [var modelDescription: MLModelDescription](mlmodel/modeldescription.md)
  Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.
- [func parameterValue(for: MLParameterKey) throws -> Any](mlmodel/parametervalue(for:).md)
  Returns a model parameter value for a key.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodeldescription)*