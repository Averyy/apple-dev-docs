# MLModelTransformerAdaptor

**Framework**: Create ML Components  
**Kind**: struct

A transformer that uses a Core ML model.

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
struct MLModelTransformerAdaptor<Scalar> where Scalar : MLShapedArrayScalar, Scalar : BinaryFloatingPoint
```

## Topics

### Creating an adaptor
- [init(model: MLModel) throws](mlmodeltransformeradaptor/init(model:).md)
  Creates a model adaptor from an MLModel.
- [init(contentsOf: URL, configuration: MLModelConfiguration) throws](mlmodeltransformeradaptor/init(contentsof:configuration:).md)
  Creates a model adaptor from a CoreML model URL.
### Getting the model
- [let model: MLModel](mlmodeltransformeradaptor/model.md)
  The CoreML model.
### Performing the transformation
- [func applied(to: MLShapedArray<Scalar>, eventHandler: EventHandler?) async throws -> MLShapedArray<Scalar>](mlmodeltransformeradaptor/applied(to:eventhandler:).md)
  Performs a transformation on a single input.
### Type Aliases
- [MLModelTransformerAdaptor.Input](mlmodeltransformeradaptor/input.md)
  The input type.
- [MLModelTransformerAdaptor.Output](mlmodeltransformeradaptor/output.md)
  The output type.
### Default Implementations
- [Transformer Implementations](mlmodeltransformeradaptor/transformer-implementations.md)

## Relationships

### Conforms To
- [Transformer](transformer.md)

## See Also

- [struct MLModelClassifierAdaptor](mlmodelclassifieradaptor.md)
  A transformer that uses a Core ML model as a classifier.
- [struct MLModelRegressorAdaptor](mlmodelregressoradaptor.md)
  A transformer that uses a Core ML model as a regressor.
- [struct ModelMetadata](modelmetadata.md)
  User info keys that specify useful information about a model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodeltransformeradaptor)*