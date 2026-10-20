# init(trainingData:tokenColumn:labelColumn:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a word tagger.

**Availability**:
- macOS 13.0+

## Declaration

```swift
init(trainingData: DataFrame, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

**Other overloads**:

```swift
init(trainingData: MLDataTable, tokenColumn: String, labelColumn: String, parameters: MLWordTagger.ModelParameters = ModelParameters(validationData: nil)) throws
```

## Parameters

- `trainingData`: A data frame specifying training data.
- `tokenColumn`: The name of the token column in the training data frame.
- `labelColumn`: The name of the label column in the training data frame.
- `parameters`: The model parameters.

## See Also

### Creating and training a word tagger
- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](./init%28trainingdata,parameters%29.md)
  Creates a word tagger.
- [MLWordTagger.Token](./token.md)
  The token type of a word tagger, which is a string.
- [MLWordTagger.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.
- [let modelParameters: MLWordTagger.ModelParameters](./modelparameters-swift.property.md)
  The configuration parameters that the word tagger used for training during initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/init(trainingdata:tokencolumn:labelcolumn:parameters:))*