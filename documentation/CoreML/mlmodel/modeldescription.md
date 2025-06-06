# modelDescription

**Framework**: Core ML  
**Kind**: property

Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.

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
var modelDescription: MLModelDescription { get }
```

## See Also

- [static var availableComputeDevices: [MLComputeDevice]](mlmodel/availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.
- [var configuration: MLModelConfiguration](mlmodel/configuration.md)
  The configuration of the model set during initialization.
- [class MLModelDescription](mlmodeldescription.md)
  Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.
- [func parameterValue(for: MLParameterKey) throws -> Any](mlmodel/parametervalue(for:).md)
  Returns a model parameter value for a key.
- [class MLParameterKey](mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/modeldescription)*