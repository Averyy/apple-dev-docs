# ModelCompatibilityError.missingInput(name:)

**Framework**: Create ML Components  
**Kind**: case

An error that indicates that the input is missing from the model.

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
case missingInput(name: String)
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/modelcompatibilityerror/missinginput(name:))*