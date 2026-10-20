# init(validationData:algorithm:language:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates model parameters.

**Availability**:
- macOS 10.14+ - Deprecated in 10.15

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
init(validationData: [(tokens: [MLWordTagger.Token], labels: [String])], algorithm: MLWordTagger.ModelAlgorithmType = .crf(revision: 1), language: NLLanguage? = nil)
```

## Parameters

- `validationData`: The validation data of token and label pairs.
- `algorithm`: The algorithm type.
- `language`: The language of the text to tag.

## See Also

### Deprecated
- [init(validationData: MLDataTable?, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?, tokenColumnValidationData: String?, labelColumnValidationData: String?)](./init%28validationdata,algorithm,language,tokencolumnvalidationdata,labelcolumnvalidationdata%29.md)
  Creates model parameters.
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  The word tagger’s validation dataset as a data table.
- [var tokenColumnValidationData: String?](./tokencolumnvalidationdata.md)
  The name of the column containing the tokens in the validation data table.
- [var labelColumnValidationData: String?](./labelcolumnvalidationdata.md)
  The name of the column containing the token labels in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/init(validationdata:algorithm:language:))*