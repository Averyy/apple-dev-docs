# init(validationData:algorithm:language:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates parameters for a text classifier with validation data in a set of labeled directories.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
init(validationData: MLTextClassifier.DataSource, algorithm: MLTextClassifier.ModelAlgorithmType = .maxEnt(revision: 1), language: NLLanguage? = nil)
```

**Other overloads**:

```swift
init(validationData: [String : [String]], algorithm: MLTextClassifier.ModelAlgorithmType = .maxEnt(revision: 1), language: NLLanguage? = nil)
```

## Parameters

- `validationData`: A data source of the labeled directories the text classifier uses for validation data during training.
- `algorithm`: An algorithm type for the text classifier.
- `language`: The language of the text to classify.

## See Also

### Deprecated
- [init(validationData: MLDataTable?, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?, textColumnValidationData: String?, labelColumnValidationData: String?)](./init%28validationdata,algorithm,language,textcolumnvalidationdata,labelcolumnvalidationdata%29.md)
  Creates parameters for a text classifier with validation data in a data table.
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  The validation data.
- [var textColumnValidationData: String?](./textcolumnvalidationdata.md)
  The name of the text column in the validation data table.
- [var labelColumnValidationData: String?](./labelcolumnvalidationdata.md)
  The name of the label column in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:))*