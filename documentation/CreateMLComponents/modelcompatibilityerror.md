# ModelCompatibilityError

**Framework**: Create ML Components  
**Kind**: enum  
**Role**: Enumeration

Errors related to CoreML model compatibility.

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
enum ModelCompatibilityError
```

## Topics

### Analyzing the error
- [ModelCompatibilityError.incompatibleInputCount(expected:actual:)](./modelcompatibilityerror/incompatibleinputcount%28expected,actual%29.md)
  An error that indicates that the number of model inputs is wrong.
- [case incompatibleInputDataFormat(expected: MLFeatureType, actual: MLFeatureType)](./modelcompatibilityerror/incompatibleinputdataformat%28expected,actual%29.md)
  An error that indicates that the input data has the wrong format.
- [ModelCompatibilityError.incompatibleInputMultiArrayDataType(_:)](./modelcompatibilityerror/incompatibleinputmultiarraydatatype%28_%29.md)
  An error that indicates that the input multi array has the wrong value type.
- [ModelCompatibilityError.incompatibleLabelType](./modelcompatibilityerror/incompatiblelabeltype.md)
  An error that indicates that the label has the wrong type.
- [ModelCompatibilityError.incompatibleMetadataKey(name:)](./modelcompatibilityerror/incompatiblemetadatakey%28name%29.md)
  An error that indicates that the metadata key has the wrong type.
- [ModelCompatibilityError.incompatibleOutputCount(expected:actual:)](./modelcompatibilityerror/incompatibleoutputcount%28expected,actual%29.md)
  An error that indicates that the number of model outputs is wrong.
- [case incompatibleOutputDataFormat(expected: MLFeatureType, actual: MLFeatureType)](./modelcompatibilityerror/incompatibleoutputdataformat%28expected,actual%29.md)
  An error that indicates that the output data has the wrong format.
- [ModelCompatibilityError.missingInput(name:)](./modelcompatibilityerror/missinginput%28name%29.md)
  An error that indicates that the input is missing from the model.
- [ModelCompatibilityError.missingLabel](./modelcompatibilityerror/missinglabel.md)
  An error that indicates that the label output is missing from the model.
- [ModelCompatibilityError.missingLabelProbabilities](./modelcompatibilityerror/missinglabelprobabilities.md)
  An error that indicates that the label probabilities output is missing from the model.
- [ModelCompatibilityError.missingOutput(name:)](./modelcompatibilityerror/missingoutput%28name%29.md)
  An error that indicates that the output is missing from the model.
- [ModelCompatibilityError.missingPredictedFeature](./modelcompatibilityerror/missingpredictedfeature.md)
  An error that indicates that the regressor model output is missing.
### Getting the debug description
- [var debugDescription: String](./modelcompatibilityerror/debugdescription.md)
  A text representation of the error.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelcompatibilityerror/customdebugstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Escapable](../Swift/escapable.md)
- [LocalizedError](../Foundation/localizederror.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Errors
- [enum AudioPreprocessingError](./audiopreprocessingerror.md)
  Audio preprocessing errors.
- [enum AudioReaderError](./audioreadererror.md)
  Audio reader errors.
- [enum CompatibilityError](./compatibilityerror.md)
  A compatibility error.
- [enum ConcatenationError](./concatenationerror.md)
  Errors thrown when concatenating numeric values.
- [enum DatasetError](./dataseterror.md)
  Dataset processing errors.
- [enum EstimatorEncodingError](./estimatorencodingerror.md)
  An estimator encoding error.
- [enum ModelUpdateError](./modelupdateerror.md)
  An updatable model error.
- [enum OptimizationError](./optimizationerror.md)
  An optimization error.
- [enum PipelineDataError](./pipelinedataerror.md)
  Errors related to pipeline data affinity problems.
- [enum SerializationError](./serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](./tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](./videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/modelcompatibilityerror)*