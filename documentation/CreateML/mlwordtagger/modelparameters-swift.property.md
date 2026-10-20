# modelParameters

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The configuration parameters that the word tagger used for training during initialization.

**Availability**:
- macOS 10.14+

## Declaration

```swift
let modelParameters: MLWordTagger.ModelParameters
```

## See Also

### Creating and training a word tagger
- [init(trainingData: [(tokens: [MLWordTagger.Token], labels: [String])], parameters: MLWordTagger.ModelParameters) throws](./init%28trainingdata,parameters%29.md)
  Creates a word tagger.
- [init(trainingData:tokenColumn:labelColumn:parameters:)](./init%28trainingdata,tokencolumn,labelcolumn,parameters%29.md)
  Creates a word tagger.
- [MLWordTagger.Token](./token.md)
  The token type of a word tagger, which is a string.
- [MLWordTagger.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that specify model training parameters and validation data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlwordtagger/modelparameters-swift.property)*