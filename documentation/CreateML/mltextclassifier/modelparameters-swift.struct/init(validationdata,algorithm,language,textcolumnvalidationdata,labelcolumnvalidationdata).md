# init(validationData:algorithm:language:textColumnValidationData:labelColumnValidationData:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates parameters for a text classifier with validation data in a data table.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
init(validationData: MLDataTable? = nil, algorithm: MLTextClassifier.ModelAlgorithmType = .maxEnt(revision: 1), language: NLLanguage? = nil, textColumnValidationData: String? = nil, labelColumnValidationData: String? = nil)
```

## Parameters

- `validationData`: A data table the text classifier uses for validation data during training.
- `algorithm`: An algorithm type for the classifier.
- `language`: The language of the text to classify.
- `textColumnValidationData`: The name of the text column in the validation data table.
- `labelColumnValidationData`: The name of the label column in the validation data table.

## See Also

### Deprecated
- [init(validationData:algorithm:language:)](./init%28validationdata,algorithm,language%29.md)
  Creates parameters for a text classifier with validation data in a set of labeled directories.
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  The validation data.
- [var textColumnValidationData: String?](./textcolumnvalidationdata.md)
  The name of the text column in the validation data table.
- [var labelColumnValidationData: String?](./labelcolumnvalidationdata.md)
  The name of the label column in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:textcolumnvalidationdata:labelcolumnvalidationdata:))*