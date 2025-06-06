# MLWordTagger.Token

**Framework**: Create ML  
**Kind**: typealias

The token type of a word tagger, which is a string.

**Availability**:
- macOS 10.14+

## Declaration

```swift
typealias Token = String
```

## See Also

- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:parameters:).md)
  Creates a word tagger.
- [init(trainingData: MLDataTable, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:)-97qtg.md)
  Creates a word tagger.
- [init(trainingData: DataFrame, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:)-9fci2.md)
  Creates a word tagger.
- [MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.property.md)
  The configuration parameters that the word tagger used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/token)*