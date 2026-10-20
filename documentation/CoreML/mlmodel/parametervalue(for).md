# parameterValue(for:)

**Framework**: Core ML  
**Kind**: method  
**Role**: Instance Method

Returns a model parameter value for a key.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func parameterValue(for key: MLParameterKey) throws -> Any
```

```objc
- (id) parameterValueForKey:(MLParameterKey *) key error:(NSError **) error;
```

## Parameters

- `key`: The key to a model parameter value.

## See Also

### Inspecting a model
- [static var availableComputeDevices: [MLComputeDevice]](./availablecomputedevices-6klyt.md)
  The list of available compute devices that the model’s prediction methods use.
- [var configuration: MLModelConfiguration](./configuration.md)
  The configuration of the model set during initialization.
- [var modelDescription: MLModelDescription](./modeldescription.md)
  Model information you use at runtime during development, which Xcode also displays in its Core ML model editor view.
- [class MLModelDescription](../mlmodeldescription.md)
  Information about a model, primarily the input and output format for each feature the model expects, and optional metadata.
- [class MLParameterKey](../mlparameterkey.md)
  The keys for the parameter dictionary in a model configuration or a model update context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmodel/parametervalue(for:))*