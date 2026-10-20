# tokenColumnValidationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The name of the column containing the tokens in the validation data table.

**Availability**:
- macOS 10.14+ - Deprecated in 10.15

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
var tokenColumnValidationData: String? { get set }
```

## See Also

### Deprecated
- [init(validationData: MLDataTable?, algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?, tokenColumnValidationData: String?, labelColumnValidationData: String?)](./init%28validationdata,algorithm,language,tokencolumnvalidationdata,labelcolumnvalidationdata%29.md)
  Creates model parameters.
- [init(validationData: [(tokens: [MLWordTagger.Token], labels: [String])], algorithm: MLWordTagger.ModelAlgorithmType, language: NLLanguage?)](./init%28validationdata,algorithm,language%29.md)
  Creates model parameters.
- [var validationData: MLDataTable?](./validationdata-swift.property.md)
  The word tagger’s validation dataset as a data table.
- [var labelColumnValidationData: String?](./labelcolumnvalidationdata.md)
  The name of the column containing the token labels in the validation data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.struct/tokencolumnvalidationdata)*