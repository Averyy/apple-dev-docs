# init(validationData:algorithm:language:tokenColumnValidationData:labelColumnValidationData:)

**Framework**: Create ML  
**Kind**: init

Creates model parameters.

**Availability**:
- macOS 10.14+

## Declaration

```swift
init(validationData: MLDataTable?, algorithm: MLWordTagger.ModelAlgorithmType = .crf(revision: 1), language: NLLanguage? = nil, tokenColumnValidationData: String? = nil, labelColumnValidationData: String? = nil)
```

## Parameters

- `validationData`: The validation data table.
- `algorithm`: The algorithm type.
- `language`: The language of the text to tag.
- `tokenColumnValidationData`: The name of the column containing the tokens in the validation data table.
- `labelColumnValidationData`: The optional name of the column containing the token labels in the validation data table.

## See Also

- [init(validationData: [(tokens: [MLWordTagger.Token], labels: [String])], algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](mlwordtagger/modelparameters-swift.struct/init(validationdata:algorithm:language:).md)
  Creates model parameters.
- [var validationData: MLDataTable?](mlwordtagger/modelparameters-swift.struct/validationdata-swift.property.md)
  The word tagger’s validation dataset as a data table.
- [var tokenColumnValidationData: String?](mlwordtagger/modelparameters-swift.struct/tokencolumnvalidationdata.md)
  The name of the column containing the tokens in the validation data table.
- [var labelColumnValidationData: String?](mlwordtagger/modelparameters-swift.struct/labelcolumnvalidationdata.md)
  The name of the column containing the token labels in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/init(validationdata:algorithm:language:tokencolumnvalidationdata:labelcolumnvalidationdata:))*