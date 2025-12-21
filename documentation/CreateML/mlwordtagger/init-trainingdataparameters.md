# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a word tagger.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: An array of tuples containing the tokens and their labels.
- `parameters`: The model parameters.

## See Also

- [init(trainingData:tokenColumn:labelColumn:parameters:)](mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:).md)
  Creates a word tagger.
- [MLWordTagger.Token](mlwordtagger/token.md)
  The token type of a word tagger, which is a string.
- [MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLWordTagger.ModelParameters](mlwordtagger/modelparameters-swift.property.md)
  The configuration parameters that the word tagger used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/init(trainingdata:parameters:))*