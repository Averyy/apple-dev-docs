# configuration

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

The configuration of the model set during initialization.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
var configuration: MLModelConfiguration { get }
```

```objc
@property (nonatomic, readonly) MLModelConfiguration * configuration;
```

## See Also

### Inspecting a model
- [static var availableComputeDevices: [MLComputeDevice]](./availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.
- [var modelDescription: MLModelDescription](./modeldescription.md)
  Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.
- [class MLModelDescription](../mlmodeldescription.md)
  Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.
- [func parameterValue(for: MLParameterKey) throws -> Any](./parametervalue%28for%29.md)
  Returns a model parameter value for a key.
- [class MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.
- [availableComputeDevices](./availablecomputedevices-42uzt.md)
  The list of available compute devices that the model’s prediction can use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/configuration)*