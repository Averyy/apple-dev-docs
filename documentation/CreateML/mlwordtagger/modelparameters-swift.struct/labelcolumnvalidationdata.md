# labelColumnValidationData

**Framework**: Create ML  
**Kind**: property

The name of the column containing the token labels in the validation data table.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var labelColumnValidationData: String? { get set }
```

## See Also

- [init(validationData: MLDataTable?, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?, tokenColumnValidationData: String?, labelColumnValidationData: String?)](mlwordtagger/modelparameters-swift.struct/init(validationdata:algorithm:language:tokencolumnvalidationdata:labelcolumnvalidationdata:).md)
  Creates model parameters.
- [init(validationData: [(tokens: [MLWordTagger.Token], labels: [String])], algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](mlwordtagger/modelparameters-swift.struct/init(validationdata:algorithm:language:).md)
  Creates model parameters.
- [var validationData: MLDataTable?](mlwordtagger/modelparameters-swift.struct/validationdata-swift.property.md)
  The word tagger’s validation dataset as a data table.
- [var tokenColumnValidationData: String?](mlwordtagger/modelparameters-swift.struct/tokencolumnvalidationdata.md)
  The name of the column containing the tokens in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/labelcolumnvalidationdata)*