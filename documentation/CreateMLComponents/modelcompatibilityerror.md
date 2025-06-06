# ModelCompatibilityError

**Framework**: Create ML Components  
**Kind**: enum

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
- [ModelCompatibilityError.incompatibleInputCount(expected:actual:)](modelcompatibilityerror/incompatibleinputcount(expected:actual:).md)
  An error that indicates that the number of model inputs is wrong.
- [case incompatibleInputDataFormat(expected: MLFeatureType, actual: MLFeatureType)](modelcompatibilityerror/incompatibleinputdataformat(expected:actual:).md)
  An error that indicates that the input data has the wrong format.
- [ModelCompatibilityError.incompatibleInputMultiArrayDataType(_:)](modelcompatibilityerror/incompatibleinputmultiarraydatatype(_:).md)
  An error that indicates that the input multi array has the wrong value type.
- [ModelCompatibilityError.incompatibleLabelType](modelcompatibilityerror/incompatiblelabeltype.md)
  An error that indicates that the label has the wrong type.
- [ModelCompatibilityError.incompatibleMetadataKey(name:)](modelcompatibilityerror/incompatiblemetadatakey(name:).md)
  An error that indicates that the metadata key has the wrong type.
- [ModelCompatibilityError.incompatibleOutputCount(expected:actual:)](modelcompatibilityerror/incompatibleoutputcount(expected:actual:).md)
  An error that indicates that the number of model outputs is wrong.
- [case incompatibleOutputDataFormat(expected: MLFeatureType, actual: MLFeatureType)](modelcompatibilityerror/incompatibleoutputdataformat(expected:actual:).md)
  An error that indicates that the output data has the wrong format.
- [ModelCompatibilityError.missingInput(name:)](modelcompatibilityerror/missinginput(name:).md)
  An error that indicates that the input is missing from the model.
- [ModelCompatibilityError.missingLabel](modelcompatibilityerror/missinglabel.md)
  An error that indicates that the label output is missing from the model.
- [ModelCompatibilityError.missingLabelProbabilities](modelcompatibilityerror/missinglabelprobabilities.md)
  An error that indicates that the label probabilities output is missing from the model.
- [ModelCompatibilityError.missingOutput(name:)](modelcompatibilityerror/missingoutput(name:).md)
  An error that indicates that the output is missing from the model.
- [ModelCompatibilityError.missingPredictedFeature](modelcompatibilityerror/missingpredictedfeature.md)
  An error that indicates that the regressor model output is missing.
- [var errorDescription: String?](modelcompatibilityerror/errordescription.md)
  A localized message describing what error occurred.
### Operators
- [static func == (ModelCompatibilityError, ModelCompatibilityError) -> Bool](modelcompatibilityerror/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [CustomDebugStringConvertible Implementations](modelcompatibilityerror/customdebugstringconvertible-implementations.md)
- [Equatable Implementations](modelcompatibilityerror/equatable-implementations.md)
- [Error Implementations](modelcompatibilityerror/error-implementations.md)
- [LocalizedError Implementations](modelcompatibilityerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum AudioPreprocessingError](audiopreprocessingerror.md)
  Audio preprocessing errors.
- [enum AudioReaderError](audioreadererror.md)
  Audio reader errors.
- [enum CompatibilityError](compatibilityerror.md)
  A compatibility error.
- [enum ConcatenationError](concatenationerror.md)
  Errors thrown when concatenating numeric values.
- [enum DatasetError](dataseterror.md)
  Dataset processing errors.
- [enum EstimatorEncodingError](estimatorencodingerror.md)
  An estimator encoding error.
- [enum ModelUpdateError](modelupdateerror.md)
  An updatable model error.
- [enum OptimizationError](optimizationerror.md)
  An optimization error.
- [enum PipelineDataError](pipelinedataerror.md)
  Errors related to pipeline data affinity problems.
- [enum SerializationError](serializationerror.md)
  A serialization error.
- [enum TabularPipelineDataError](tabularpipelinedataerror.md)
  Errors related to tabular pipeline data affinity problems.
- [enum VideoReaderError](videoreadererror.md)
  Video loader errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/modelcompatibilityerror)*