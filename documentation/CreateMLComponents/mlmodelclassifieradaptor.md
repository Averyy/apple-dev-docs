# MLModelClassifierAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A transformer that uses a Core ML model as a classifier.

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
struct MLModelClassifierAdaptor<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Topics

### Creating a transformer
- [init(model: MLModel) throws](mlmodelclassifieradaptor/init(model:).md)
  Creates a MLModel classifier adaptor from a model.
- [init(contentsOf: URL, configuration: MLModelConfiguration) throws](mlmodelclassifieradaptor/init(contentsof:configuration:).md)
  Creates a model adaptor from a CoreML model URL.
### Getting the model
- [let model: MLModel](mlmodelclassifieradaptor/model.md)
  The CoreML model.
### Performing the transformation
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> ClassificationDistribution<MLModelClassifierAdaptor<Scalar>.Label>](mlmodelclassifieradaptor/applied(to:eventhandler:).md)
  Performs a prediction from a single input.
- [MLModelClassifierAdaptor.Label](mlmodelclassifieradaptor/label.md)
  The classifier label type.
### Type Aliases
- [MLModelClassifierAdaptor.Input](mlmodelclassifieradaptor/input.md)
  The input type.
- [MLModelClassifierAdaptor.Output](mlmodelclassifieradaptor/output.md)
  The output type.
### Default Implementations
- [Transformer Implementations](mlmodelclassifieradaptor/transformer-implementations.md)

## Relationships

### Conforms To
- [Classifier](classifier.md)
- [Transformer](transformer.md)

## See Also

- [struct MLModelTransformerAdaptor](mlmodeltransformeradaptor.md)
  A transformer that uses a Core ML model.
- [struct MLModelRegressorAdaptor](mlmodelregressoradaptor.md)
  A transformer that uses a Core ML model as a regressor.
- [struct ModelMetadata](modelmetadata.md)
  User info keys that specify useful information about a model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelclassifieradaptor)*