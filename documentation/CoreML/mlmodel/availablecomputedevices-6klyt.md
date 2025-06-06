# availableComputeDevices

**Framework**: Core ML  
**Kind**: property

The list of available compute devices that the model’s prediction methods use.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var availableComputeDevices: [MLComputeDevice] { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/availablecomputedevices-6klyt)*