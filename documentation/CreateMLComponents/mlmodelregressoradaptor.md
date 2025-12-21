# MLModelRegressorAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A transformer that uses a Core ML model as a regressor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
struct MLModelRegressorAdaptor<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Topics

### Creating an adaptor
- [init(model: MLModel) throws](mlmodelregressoradaptor/init(model:).md)
  Creates a MLModel regressor adaptor from a model.
- [init(contentsOf: URL, configuration: MLModelConfiguration) throws](mlmodelregressoradaptor/init(contentsof:configuration:).md)
  Creates a model adaptor from a CoreML model URL.
### Getting the model
- [let model: MLModel](mlmodelregressoradaptor/model.md)
  The CoreML model.
### Performing the prediction
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> Double](mlmodelregressoradaptor/applied(to:eventhandler:).md)
  Performs a prediction from a single input.

## Relationships

### Conforms To
- [Regressor](regressor.md)
- [Transformer](transformer.md)

## See Also

- [struct MLModelTransformerAdaptor](mlmodeltransformeradaptor.md)
  A transformer that uses a Core ML model.
- [struct MLModelClassifierAdaptor](mlmodelclassifieradaptor.md)
  A transformer that uses a Core ML model as a classifier.
- [struct ModelMetadata](modelmetadata.md)
  User info keys that specify useful information about a model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelregressoradaptor)*