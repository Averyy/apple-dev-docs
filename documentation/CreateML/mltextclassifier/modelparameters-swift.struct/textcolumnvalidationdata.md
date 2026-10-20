# textColumnValidationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The name of the text column in the validation data table.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
var textColumnValidationData: String? { get set }
```

## See Also

### Deprecated
- [init(validationData:algorithm:language:)](./init%28validationdata,algorithm,language%29.md)
  Creates parameters for a text classifier with validation data in a set of labeled directories.
- [init(validationData: MLDataTable?, algorithm: MLTextClassifier.ModelAlgorithmType, language: NLLanguage?, textColumnValidationData: String?, labelColumnValidationData: String?)](./init%28validationdata,algorithm,language,textcolumnvalidationdata,labelcolumnvalidationdata%29.md)
  Creates parameters for a text classifier with validation data in a data table.
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  The validation data.
- [var labelColumnValidationData: String?](./labelcolumnvalidationdata.md)
  The name of the label column in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltextclassifier/modelparameters-swift.struct/textcolumnvalidationdata)*