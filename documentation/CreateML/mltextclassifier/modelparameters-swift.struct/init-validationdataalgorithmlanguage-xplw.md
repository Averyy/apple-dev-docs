# init(validationData:algorithm:language:)

**Framework**: Create ML  
**Kind**: init

Creates parameters for a text classifier with validation data in a dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(validationData: [String : [String]], algorithm: MLTextClassifier.ModelAlgorithmType = .maxEnt(revision: 1), language: NLLanguage? = nil)
```

#### Discussion

- validationData: A dictionary the text classifier uses for validation data during training. - algorithm: An algorithm type for the classifier.
- language: The language of the text to classify.

## See Also

- [init(validationData: MLDataTable?, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?, textColumnValidationData: String?, labelColumnValidationData: String?)](mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:textcolumnvalidationdata:labelcolumnvalidationdata:).md)
  Creates parameters for a text classifier with validation data in a data table.
- [init(validationData: MLTextClassifier.DataSource, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?)](mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:)-95vq7.md)
  Creates parameters for a text classifier with validation data in a set of labeled directories.
- [var validationData: MLDataTable?](mltextclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  The validation data.
- [var textColumnValidationData: String?](mltextclassifier/modelparameters-swift.struct/textcolumnvalidationdata.md)
  The name of the text column in the validation data table.
- [var labelColumnValidationData: String?](mltextclassifier/modelparameters-swift.struct/labelcolumnvalidationdata.md)
  The name of the label column in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/init(validationdata:algorithm:language:)-xplw)*