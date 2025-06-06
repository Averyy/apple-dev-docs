# modelParameters

**Framework**: Create ML  
**Kind**: property

The configuration parameters that the word tagger used for training during initialization.

**Availability**:
- macOS 10.14+

## Declaration

```swift
let modelParameters: MLWordTagger.ModelParameters
```

## See Also

- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:parameters:).md)
  Creates a word tagger.
- [init(trainingData: MLDataTable, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:)-97qtg.md)
  Creates a word tagger.
- [init(trainingData: DataFrame, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters) throws](mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:)-9fci2.md)
  Creates a word tagger.
- [MLWordTagger.Token](mlwordtagger/token.md)
  The token type of a word tagger, which is a string.
- [MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.property)*